## -*- coding: utf-8 -*-
<%
    from ott.view_header_footer.utils import client_utils
    from ott.utils import html_utils

    # simple translate method
    txt = "TODO HEADER"
    if html_utils.get_lang(request) == "es":
        txt = "TODO HEADER - Número uno buenos días"
    txt = client_utils.clean_str(txt)

    # TODO dynamic div name via
    div_id = "main"

    # server port - should be in .ini as ott.svr_port -- important for proxied app server behind port 80
    port = html_utils.get_svr_port(request)
    header = client_utils.cached_wget_header(port=port, title=txt)
    footer = client_utils.cached_wget_footer(port=port)
%>${header|n}
    <div id="${div_id}"></div>
${footer|n}
