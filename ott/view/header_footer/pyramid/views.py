import StringIO
import re

from pyramid.request import Request
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound

from pyramid.view import view_config
from pyramid.view import notfound_view_config

from pyramid.events import NewRequest
from pyramid.events import ApplicationCreated
from pyramid.events import subscriber

from ott.utils import web_utils
from ott.utils import html_utils
from ott.utils import object_utils
from ott.utils import transit_utils

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


@view_config(route_name='example_desktop', renderer='desktop/head_foot_example.html')
@view_config(route_name='example_mobile',  renderer='mobile/head_foot_example.html')
def example(request):
    import requests
    h = web_utils.get_response("http://localhost:14141/head.html")
    f = web_utils.get_response("http://localhost:14141/foot.html")
    c = web_utils.get_response("http://maps.trimet.org/ride/ws/stop.html?id=2")
    c = requests.get("http://fieldtrip.trimet.org/fieldtrip/newRequestForm")
    ret_val = {
        'header': h,
        'footer': f,
        'content': c.text
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

@notfound_view_config(renderer='notfound.mako')
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