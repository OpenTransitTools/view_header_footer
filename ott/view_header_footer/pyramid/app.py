import os

from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import ApplicationCreated
from pyramid.events import NewRequest

from ott.view_header_footer.pyramid import views

import logging
log = logging.getLogger(__file__)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
        run with: bin/pserve pyramid.ini --reload
    """
    config = Configurator(settings=settings)

    do_static_config(config)
    config.include(views.do_view_config)
    config.scan('ott.view_header_footer.pyramid')

    return config.make_wsgi_app()


def do_static_config(config):
    """ config the static folders
    """
    cache_age = 3600

    config.add_static_view('static', 'ott.view_header_footer:static', cache_max_age=cache_age)
    config.add_static_view('html',   'ott.view_header_footer:static', cache_max_age=cache_age)
    config.add_static_view('js',     'ott.view_header_footer:static/js', cache_max_age=cache_age)
    config.add_static_view('css',    'ott.view_header_footer:static/css', cache_max_age=cache_age)
    config.add_static_view('images', 'ott.view_header_footer:static/images', cache_max_age=cache_age)

    # important ... allow .html extension on mako templates
    config.include('pyramid_mako')
    config.add_mako_renderer('.html', settings_prefix='mako.')

    # internationalization ... @see: locale/subscribers.py for more info
    """
    config.add_translation_dirs('ott.view:locale')
    config.add_subscriber('ott.view.locale.subscribers.add_renderer_globals', 'pyramid.events.BeforeRender')
    config.add_subscriber('ott.view.locale.subscribers.add_localizer', 'pyramid.events.NewRequest')
    """


@subscriber(ApplicationCreated)
def application_created_subscriber(event):
    """ what do i do?
        I'm called at startup of the Pyramid app.  
    """
    #log.info('Starting pyramid server -- visit me on http://127.0.0.1:8080')
    print event


@subscriber(NewRequest)
def new_request_subscriber(event):
    """ what do i do?
       1. entry point for a new server request
       2. configure the request context object (can insert new things like db connections or authorization 
          to pass around in this given request context)
    """
    log.debug("new request called -- request is 'started'")
    request = event.request
    request.BASE_DIR = os.path.dirname(os.path.realpath(__file__))


