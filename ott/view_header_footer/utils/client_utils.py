""" this is a utility to make calls into the header and footer server, and return
    strings representing the header and footer...
"""
import sys
import urllib2


def wget_stuff(domain, port, path, is_mobile, params, def_val=""):
    ret_val = def_val

    if is_mobile:
        path = "m/{}".format(path)

    url = "http://{}:{}/{}?client_utils{}".format(domain, port, path, params)
    print "downloading {0}".format(url)
    response = urllib2.urlopen(url.replace(" ", "%20"))
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
    params = ""
    if title:         params = "{}&title={}".format(params, title)
    if header:        params = "{}&header={}".format(params, header)
    if sub_header:    params = "{}&sub_header={}".format(params, sub_header)
    if second_header: params = "{}&second_header={}".format(params, second_header)
    if icon_cls:      params = "{}&icon_cls={}".format(params, icon_cls)
    if icon_url:      params = "{}&icon_url={}".format(params, icon_url)
    if onload:        params = "{}&onload={}".format(params, onload)

    html = wget_stuff(domain, port, path, is_mobile, params, def_val)
    return html


def wget_footer(domain="localhost", port="14441", path="footer.html", is_mobile=False, def_val=""):
    """ utility class curl a page header from the system
    """
    params = ""
    #if title:         params = "{}&title={}".format(params, title)

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
