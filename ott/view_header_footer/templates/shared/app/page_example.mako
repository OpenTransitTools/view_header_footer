<%namespace name="util"  file="/shared/utils/hf_utils.mako"/>
<%
    from ott.view_header_footer.utils import client_utils
    port = util.get_ini_param('port', '14441')
    header = client_utils.wget_header(port=port, header="Stop XXX")
    footer = client_utils.wget_footer(port=port)
%>
${header|n}

BLAH BLAH BLAH

${footer|n}