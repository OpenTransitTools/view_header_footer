""" this is a simple command-line utility (that should work python 1.5+), which will pull different content from
    either files or urls into a single output file.  The original intent is simply a way to update a template file
    with an external header and footer derived from the view_header_footer app...

    see the sandwich.conf .json file for inputs 
"""
import sys
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
    # import pdb; pdb.set_trace()
    response = urllib2.urlopen(url.replace(" ", "%20"))
    html = response.read()
    if html:
        ret_val = html
    return ret_val


def get_file_data(file_path, start, end, def_val=""):
    """ utility class to grab data from a file
        optional start and end points can be defined
    """
    ret_val = def_val
    print "opening file {0} (start={1}, end={2})".format(file_path, start, end)

    # step 1: grab file line by line, and bound the output based on optional start or end points in the file
    lines = []
    with open(file_path) as f:
        for i, l in enumerate(f):
            if start and i+1 < start:
                continue
            if end and i+1 > end:
                break
            lines.append(l)

    # step 2: list to string
    if len(lines) > 0:
        ret_val = ''.join(map(str, lines))
    return ret_val


def get_data(cfg, def_val=""):
    ret_val = data = def_val
    if cfg.get('url'):
        data = get_url_data(cfg.get('url'), def_val)
    elif cfg.get('file'):
        data = get_file_data(cfg.get('file'), cfg.get('start'), cfg.get('end'), def_val)
    elif cfg.get('text'):
        data = cfg.get('text')
    if data:
        ret_val = data
    return ret_val


def sandwich(config):
    ''' assumes a dict with output string (file) and input list (content)
        @see sandwich.conf for an example
    '''

    # step 1: cache the data
    data = []
    for cfg in config.get('inputs'):
        data.append(get_data(cfg))

    # step 2: output that data
    with open(config.get('output'), 'w') as f:
        for d in data:
            f.write(d)


def sandwich_via_file(config_path='sandwich.conf'):
    config = get_json(config_path)
    sandwich(config)


def main():
    if len(sys.argv) >= 2:
        sandwich_via_file(sys.argv[1])
    else:
        sandwich_via_file()


if __name__ == '__main__':
    main()
