import json
import urllib2


def get_json(file_path):
    """ utility class to load a static .json file
    """
    ret_val = {}
    with open(file_path) as f:
        ret_val = json.load(f)
    return ret_val


def get_url_data(url, def_val=""):
    """ utility class to load data from a url
    """
    ret_val = def_val

    print "downloading {0}".format(url)
    response = urllib2.urlopen(url.replace(" ", "%20"))
    html = response.read()
    if html:
        ret_val = html
    return ret_val


def get_file_data(file_path, def_val=""):
    """ utility class to grab data from a file
    """
    ret_val = def_val
    print "opening file {0}".format(file_path)
    with open(file_path) as f:
        ret_val = f.read()
    return ret_val


cfg = get_json('sandwich.conf')
with open(cfg.get('output'), 'w') as f:
    for c in cfg.get('inputs'):
        if c.get('url'):
            d = get_url_data(c.get('url'))
        elif c.get('file'):
            d = get_file_data(c.get('file'))
        if d:
            f.write(d)
