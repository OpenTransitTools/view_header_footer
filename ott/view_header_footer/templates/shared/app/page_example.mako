## -*- coding: utf-8 -*-
<%
    from ott.view_header_footer.utils import client_utils
    from ott.utils import html_utils

    # simple translate method
    txt = "Number one Daba Daba"
    if html_utils.get_lang(request) == "es":
        txt = "Número uno buenos días"

    # server port - should be in .ini as ott.svr_port -- important for proxied app server behind port 80
    port = html_utils.get_server_port(request)

    surl = u"sandwich.html?{}".format(request.query_string).replace("&", "%26")
    header = client_utils.wget_header(port=port, title=txt, header="Stop [MMM](" + surl + ")", sub_header=txt, icon_cls="fa-ss-outline h1icon", icon_url=surl)
    footer = client_utils.wget_footer(port=port)
    header = client_utils.clean_str(header)
%>${header|n}

BLAH BLAH BLAH

${footer|n}
