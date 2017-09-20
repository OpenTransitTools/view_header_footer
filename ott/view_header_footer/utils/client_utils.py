# -*- coding: utf-8 -*-

""" this is a utility to make calls into the header and footer server, and return
    strings representing the header and footer...
"""
import sys
import urllib2


def clean_str(s):
    ret_val = s
    if s and len(s) > 0:
        ret_val = s.decode('utf-8')
    return ret_val


def append_get_param(params, param_name, param_val):
    """ append a new url GET param to a string of such params, ala "?x=VAL&y=VAL&etc=..."
        NOTE: stupid crap you have to jump thru for utf-8 strings
    """
    if params is None:
        params = u""
    ret_val = params

    if param_name and param_val:
        ret_val = u"{}&{}={}".format(params, param_name, param_val.replace(" ", "%20").decode('utf-8'))
    return ret_val


def url_open(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    opener.addheaders = [('Accept-Charset', 'utf-8')]
    f = opener.open(url)
    return f


def wget_stuff(domain, port, path, is_mobile, params, def_val=""):
    ret_val = def_val

    if is_mobile:
        path = u"m/{}".format(path)

    url = u"http://{}:{}/{}?client_utils{}".format(domain, port, path, params)
    print u"downloading {0}".format(url)
    response = urllib2.urlopen(url)
    """
    #response = url_open(url)
    html = response.read()
    if html and len(html) > 0:
        ret_val = html.strip()
    """
    return ret_val


def wget_header(domain="localhost", port="14441", path="header.html", is_mobile=False,
                title=None, header=None, sub_header=None, second_header=None,
                icon_cls=None, icon_url=None,
                onload=None,
                def_val=""):
    """ utility class curl a page header from the system
    """
    params = u""
    html = u""
    if title: params = append_get_param(params, 'title', title)
    if header: params = append_get_param(params, 'header', header)
    if sub_header: params = append_get_param(params, 'sub_header', sub_header)
    if second_header: params = append_get_param(params, 'second_header', second_header)
    if icon_cls: params = append_get_param(params, 'icon_cls', icon_cls)
    if icon_url: params = append_get_param(params, 'icon_url', icon_url)
    if onload: params = append_get_param(params, 'onload', onload)
    html = wget_stuff(domain, port, path, is_mobile, params, def_val)
    return html


def wget_footer(domain="localhost", port="14441", path="footer.html", is_mobile=False, def_val=""):
    """ utility class curl a page header from the system
    """
    params = ""
    html = wget_stuff(domain, port, path, is_mobile, params, def_val)
    return html


def main():
    if len(sys.argv) >= 2:
        html = wget_header(header=sys.argv[1])
    else:
        html = wget_header()
    print html


if __name__ == '__main__':
    main()
