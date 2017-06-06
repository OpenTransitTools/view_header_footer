<%namespace name="util"  file="/shared/utils/misc_utils.mako"/>
<%
    extra_params = util.get_extra_params()
    rel_path='./'
    if util.has_url_param('mobile'):
        rel_path = './m/'
    pages = [
        {'label': 'Trip Planner Pages'},
        {'u':'pform_standalone.html', 'p':'from=2&to=834', 'n':'basic embedded trip planner form (outside the home page, as opposed to the server-side include above)'},
        {'u':'', 'p':'', 'n':''},
        {'label': 'BLAH'},
        {'u':'stop_schedule.html', 'p':'stop_id=11507&more', 'n':'more button'},
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
    <h2>Welcome to the Trip Tools testing area!</h2>
    <p>Use the links below to test out the Trip Planner and its related pages.</p>
    <p>We'll probably want to cull this list a bit for the official testing. Reorganize, too. But we need to keep this page as-is... maybe make it test.html or something like that.</p>

    %for p in pages:
        %if 'label' in p:
            <h2>${p['label']}</h2>
        %else:
            <a target="_blank" href="${p['path'] if 'path' in p else rel_path}${p['u']}?${p['p']}${extra_params}">${p['u']}</a>  ${p['n'] if 'n' in p else ''}<br/>
        %endif
    %endfor
