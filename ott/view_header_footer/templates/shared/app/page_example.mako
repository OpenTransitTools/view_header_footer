## -*- coding: utf-8 -*-
<%
    from ott.view_header_footer.utils import client_utils
    header = client_utils.wget_header(port=request.server_port, header="Stop [MMM](/sandwich.html)", sub_header="Great Stop", icon_cls="fa-ss-outline h1icon", icon_url="/sandwich.html")
    footer = client_utils.wget_footer(port=request.server_port)

%>${header|n}

BLAH BLAH BLAH

${footer|n}