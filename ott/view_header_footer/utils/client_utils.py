# -*- coding: utf-8 -*-

""" this is a utility to make calls into the header and footer server, and return
    strings representing the header and footer...
"""
import sys
import urllib2
from repoze.lru import lru_cache

import logging
log = logging.getLogger(__file__)


def clean_str(s):
    ret_val = decode(s)
    return ret_val


def decode(str, codec='utf-8'):
    try:
        ret_val = str.decode(codec)
    except:
        ret_val = str
    return ret_val


def encode(str, codec='utf-8'):
    try:
        ret_val = str.encode(codec)
    except:
        ret_val = str
    return ret_val


def append_get_param(params, param_name, param_val):
    """ append a new url GET param to a string of such params, ala "?x=VAL&y=VAL&etc=..."
        NOTE: stupid crap you have to jump thru for utf-8 strings
    """
    if params is None:
        params = u""
    ret_val = params

    if param_name and param_val:
        ret_val = u"{}&{}={}".format(params, param_name, decode(param_val.replace(" ", "%20")))
    return ret_val


def url_open(url):
    """ untested / unused downloader """
    log.info(url)
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    opener.addheaders = [('Accept-Charset', 'utf-8')]
    url = encode(url)
    f = opener.open(url)
    return f


def url_open(url):
    """ downloader that opens a URL (or IRL) """
    log.info(url)
    url = encode(url)
    response = urllib2.urlopen(url)
    return response


def wget_stuff(domain, port, path, is_mobile, params, def_val=""):
    ret_val = def_val

    if is_mobile:
        path = u"m/{}".format(path)

    url = u"http://{}:{}/{}?client_utils{}".format(domain, port, path, params)
    response = url_open(url)
    html = response.read()
    if html and len(html) > 0:
        ret_val = html.strip()

    return ret_val


def wget_header(domain="localhost", port="14441", path="header.html", is_mobile=False,
                title=None, header=None, sub_header=None, second_header=None,
                icon_cls=None, icon_url=None,
                onload=None,
                def_val=""):
    """ utility class curl a page header from the system
    """
    params = u""
    if title: params = append_get_param(params, 'title', title)
    if header: params = append_get_param(params, 'header', header)
    if sub_header: params = append_get_param(params, 'sub_header', sub_header)
    if second_header: params = append_get_param(params, 'second_header', second_header)
    if icon_cls: params = append_get_param(params, 'icon_cls', icon_cls)
    if icon_url: params = append_get_param(params, 'icon_url', icon_url)
    if onload: params = append_get_param(params, 'onload', onload)
    html = wget_stuff(domain, port, path, is_mobile, params, def_val)
    html = decode(html)
    return html


def wget_footer(domain="localhost", port="14441", path="footer.html", is_mobile=False, def_val=""):
    """ utility class curl a page header from the system
    """
    params = ""
    html = wget_stuff(domain, port, path, is_mobile, params, def_val)
    return html


@lru_cache(10000, timeout=600)
def cached_wget_header(domain="localhost", port="14441", path="header.html", is_mobile=False,
                title=None, header=None, sub_header=None, second_header=None,
                icon_cls=None, icon_url=None,
                onload=None,
                def_val=""):
    """ http://docs.repoze.org/lru/api.html#repoze.lru.lru_cache """
    return wget_header(domain, port, path, is_mobile, title, header, sub_header, second_header, icon_cls, icon_url, onload, def_val)


@lru_cache(10000, timeout=600)
def cached_wget_footer(domain="localhost", port="14441", path="footer.html", is_mobile=False, def_val=""):
    return wget_footer(domain, port, path, is_mobile, def_val)


def main():
    if len(sys.argv) >= 2:
        html = wget_header(header=sys.argv[1])
    else:
        html = wget_header()
    print html


if __name__ == '__main__':
    main()
