<%inherit file="/desktop/header_base.html"/>
<%def name="title()">Open Trip Tools</%def>
<%def name="js_ui_include()">Open Trip Tools</%def>

<%namespace name="util"  file="/shared/utils/misc_utils.mako"/>
<%
    extra_params = util.get_extra_params()
    rel_path='./'
    if util.has_url_param('mobile'):
        rel_path = './m/'
    pages = [
        {'label': 'Parts'},
        {'u':'header.html', 'p':'title=Blah%20;Blah%20;Blah&header=Bo%20;Bo%20;Bo', 'n':'header with title and header'},
        {'u':'header.html', 'p':'title=Title And Header Same&header=True',          'n':'header with title == header (true param)'},
        {'u':'header.html', 'p':'title=No Header',                                  'n':'header with title but no header'},
        {'u':'header.html', 'p':'header=No Title',                                  'n':'header with no title, just header (title == header)'},
        {'u':'header.html', 'p':'header=WARNING&emergency_content=YO YO YO',        'n':'Show a warning atop the page'},
        {'label': 'Footers'},
        {'u':'footer.html', 'p':'',                                                 'n':'No params'},
        {'label': 'Examples'},
        {'u':'example.html', 'p':'', 'n':'example app #1 using header & footer'},
    ] 
%>
    <button onclick="location.href='.'">ENGLISH</button> <button onclick="location.href='.?_LOCALE_=es'">SPANISH</button> <button onclick="location.href='.?mobile=1${extra_params}'">MOBILE</button>
    <br/>
    <h1>
    %if 'm' in rel_path:
        MOBILE |
    %else:
        DESKTOP |
    %endif
    %if len(extra_params) > 1:
        SPANISH
    %else:
        ENGLISH
    %endif
    </h1>
    <h2>Welcome to the Header Footer testing area!</h2>
    <p>Use the links below to test out the Trip Planner and its related pages.</p>
    %for p in pages:
        %if 'label' in p:
            <h2>${p['label']}</h2>
        %else:
            <a target="_blank" href="${p['path'] if 'path' in p else rel_path}${p['u']}?${p['p']}${extra_params}">${p['u']}</a>  ${p['n'] if 'n' in p else ''}<br/>
        %endif
    %endfor
<%include file="/desktop/footer.html" />