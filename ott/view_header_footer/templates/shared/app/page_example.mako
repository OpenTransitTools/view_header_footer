## -*- coding: utf-8 -*-
<%
    from ott.view_header_footer.utils import client_utils
    from ott.utils import html_utils
    txt = "YO Daba Daba"
    if html_utils.get_lang(request) == "es":
        txt = "Número uno buenos días"
    header = txt
    #header = client_utils.wget_header(port=request.server_port, title=txt, header="Stop [MMM](/sandwich.html)", sub_header=txt, icon_cls="fa-ss-outline h1icon", icon_url="/sandwich.html")
    footer = client_utils.wget_footer(port=request.server_port)
    header = client_utils.clean_str(header)
%>${header|n}

BLAH BLAH BLAH

${footer|n}
