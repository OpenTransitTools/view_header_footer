""" this is a utility to work with the header and footer service, and download

    see the sandwich.conf .json file for inputs 
"""
import sys
import json
import urllib2


def get_local_header(domain="localhost", port="14441", path="header.html", is_mobile=False,
                     title=None, header=None, sub_header=None, second_header=None,
                     def_val=""):
    """ utility class curl a page header from the system
    """
    ret_val = def_val

    if is_mobile:
        path = "m/{}".format(path)

    params = ""
    if title:         params = "{}&title={}".format(params, title)
    if header:        params = "{}&header={}".format(params, header)
    if sub_header:    params = "{}&sub_header={}".format(params, sub_header)
    if second_header: params = "{}&second_header={}".format(params, second_header)

    url = "http://{}:{}/{}?client_utils{}".format(domain, port, path, params)
    print "downloading {0}".format(url)
    response = urllib2.urlopen(url.replace(" ", "%20"))
    html = response.read()
    if html and len(html) > 0:
        ret_val = html.strip()
    return ret_val


def main():
    if len(sys.argv) >= 2:
        html = get_local_header(header=sys.argv[1])
    else:
        html = get_local_header()
    print html


if __name__ == '__main__':
    main()
