## -*- coding: utf-8 -*-
import os

from pyramid.request import Request
from pyramid.httpexceptions import HTTPFound

from pyramid.view import view_config
from pyramid.view import notfound_view_config

from pyramid.events import NewRequest
from pyramid.events import ApplicationCreated
from pyramid.events import subscriber

from ott.utils import web_utils
from ott.utils import html_utils

import logging
log = logging.getLogger(__file__)


def do_view_config(config):
    ''' adds the views (see below) and static directories to pyramid's config
    '''
    config.add_route('index_desktop',       '/')
    config.add_route('index_mobile',        '/m')
    config.add_route('exception_desktop',   '/exception.html')
    config.add_route('exception_mobile',    '/m/exception.html')

    config.add_route('header_desktop',      '/header.html')
    config.add_route('header_mobile',       '/m/header.html')
    config.add_route('footer_desktop',      '/footer.html')
    config.add_route('footer_mobile',       '/m/footer.html')

    config.add_route('example_desktop',     '/example.html')
    config.add_route('example_mobile',      '/m/example.html')


@view_config(route_name='header_desktop', renderer='desktop/header.html')
@view_config(route_name='header_mobile', renderer='mobile/header.html')
def header(request):
    ret_val = {}
    return ret_val


@view_config(route_name='footer_desktop', renderer='desktop/footer.html')
@view_config(route_name='footer_mobile', renderer='mobile/footer.html')
def footer(request):
    ret_val = {}
    return ret_val


@view_config(route_name='example_desktop', renderer='shared/app/example.html')
@view_config(route_name='example_mobile',  renderer='shared/app/example.html')
def example(request):
    from ott.view.header_footer.utils import sandwich

    h = "This is a special page"
    s = "with an extra special formatting"
    if is_mobile(request):
        header = "http://localhost:14141/m/header.html?header={}&second_header={}".format(h, s)
        footer = "http://localhost:14141/m/footer.html"
    else:
        header = "http://localhost:14141/header.html?header={}&second_header={}".format(h, s)
        footer = "http://localhost:14141/footer.html"

    from pyramid.path import AssetResolver
    a = AssetResolver()
    resolver = a.resolve('ott.view:templates/shared/app/example.html')
    file_path = resolver.abspath()
    cfg = {'output': file_path,
            'inputs': [
                {"url": header},
                {"text": "You are special, my friend."},
                {"url": footer},
           ]
    }
    sandwich.sandwich(cfg)
    return {}

def sexample(request):
    ht = st = ""
    #import pdb; pdb.set_trace()
    do_fieldtrip = True
    if do_fieldtrip:
        import requests
        c = requests.get("http://fieldtrip.trimet.org/fieldtrip/newRequestForm")
        c = c.text[880:]
        ht = html_utils.html_escape("Field Trip Request Form")
        st = html_utils.html_escape("Complete and return this form to request a field trip if you wish to travel on TriMet with a group of 15 or more. __Trips **must*** be scheduled and paid for (if applicable) at least two weeks in advance___. If you have any questions, please email us at fieldtrips@trimet.org or call 503-962-2424, option 4.")
    else:
        c = web_utils.get_response("http://maps.trimet.org/ride/ws/stop.html?id=2")

    ret_val = {
        'header': h,
        'footer': f,
        'content': c
    }
    return ret_val


@view_config(route_name='exception_mobile',  renderer='mobile/exception.html')
@view_config(route_name='exception_desktop', renderer='desktop/exception.html')
def handle_exception(request):
    ret_val = {}
    return ret_val

@view_config(route_name='index_desktop', renderer='index.html')
@view_config(route_name='index_mobile',  renderer='index.html')
def index_view(request):
    return {}


@subscriber(ApplicationCreated)
def application_created_subscriber(event):
    '''
       what do i do?

       1. I'm called at startup of the Pyramid app.  
       2. I could be used to make db connection (pools), etc...
    '''
    log.info('Starting pyramid server...')


@subscriber(NewRequest)
def new_request_subscriber(event):
    '''
       what do i do?

       1. entry point for a new server request
       2. configure the request context object (can insert new things like db connections or authorization to pass around in this given request context)
    '''
    log.debug("new request called -- request is 'started'")
    request = event.request
    request.add_finished_callback(cleanup)

@notfound_view_config(renderer='shared/notfound.mako')
def notfound(request):
    '''
        render the notfound.mako page anytime a request comes in that
        the app does't have mapped to a page or method
    '''
    return {}

##
## view utils
##

def cleanup(request):
    '''
       what do i do?

       1. I was configured via the new_request_subscriber(event) method
       2. I'm called via a server event (when a request is 'finished')
       3. I could do random cleanup tasks like close database connections, etc... 
    '''
    log.debug("cleanup called -- request is 'finished'")


def is_mobile(request):
    return '/m/' in request.path_url


def get_path(request, path):
    ret_val = path
    if is_mobile(request):
        ret_val = '/m' + path
    return ret_val


def forward_request(request, path, query_string=None, extra_params=None):
    # http://ride.trimet.org?mapit=I&submit&${plan['params']['map_planner']}
    # def map_url_params(self, fmt="from={frm}&to={to}&time={time}&maxHours={max_hours}&date={month}/{day}/{year}&mode={mode}&optimize={optimize}&maxWalkDistance={walk_meters:.0f}&arriveBy={arrive_depart}"):
    return HTTPFound(location=path)


def make_subrequest(request, path, query_string=None, extra_params=None):
    ''' create a subrequest to call another page in the app...
        http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/subrequest.html
    '''
    # step 1: make a new request object...
    path = get_path(request, path)
    subreq = Request.blank(path)

    # step 2: default to request's querystring as default qs
    if query_string is None:
        query_string = request.query_string

     # step 3: pre-pend any extra stuff to our querytring
    if extra_params:
        newqs = extra_params
        if len(query_string) > 0:
            newqs = newqs + "&" + query_string
        query_string = newqs

    # step 4: finish the qs crap, and call this sucker...
    subreq.query_string = query_string
    ret_val = request.invoke_subrequest(subreq)
    return ret_val
