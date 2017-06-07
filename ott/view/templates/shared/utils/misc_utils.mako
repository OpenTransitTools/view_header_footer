## -*- coding: utf-8 -*-

<%def name="page_title(def_val='')">
    <%
    ret_val = def_val
    t = get_first_param_safe_str('title')
    if t:
        ret_val = t
    else:
        h = get_first_param_safe_str('header')
        if h:
            ret_val = h
    return ret_val
%></%def>


<%def name="page_header(def_val=None)">
    <%
    ret_val = def_val
    h = get_first_param_safe_str('header', 200)
    if h:
        ret_val = h
    return ret_val
%></%def>

<%def name="page_sub_header(def_val=None)">
    <%
    ret_val = def_val
    h = get_first_param_safe_str('sub_header', 200)
    if h:
        ret_val = h
    return ret_val
%></%def>

<%def name="get_ini_param(name, def_val=None)"><%
    ret_val = def_val
    try:
        ret_val = request.registry.settings[name]
        ret_val.strip()
    except Exception, e:
        #print e
        pass
    return ret_val
%></%def>

<%def name="url_domain()"><% return get_ini_param('ott.css_url', '') %></%def>
<%def name="is_test()"><% return get_ini_param('ott.is_test') %></%def>
<%def name="img_url()">${url_domain()}/images/triptools</%def>

<%def name="localize_str(s, def_val=None)"><%
    ret_val = def_val
    try:
        if s == "None":
            s = None
        elif s is not None:
            ret_val = _(s)
            if len(s) < 1:
                ret_val = def_val
    except:
        ret_val = def_val
    return ret_val
%></%def>

<%def name="unicode_to_str(s, def_val=None)"><%
    ret_val = def_val
    try:
        if s:
            ret_val = str(s)
    except:
        ret_val = def_val
    return ret_val
%></%def>

<%def name="get_url(url=None)"><%
    ret_val = url
    if url is None:
        host = get_ini_param('ott.host_url', request.host_url)
        ret_val = "{0}{1}".format(host, request.path_qs)
    ret_val = prep_url_params(ret_val, url_escape=True, spell_and=True)
    return ret_val
%></%def>


<%def name="get_first_param_safe_str(param_name, max_len=60, def_val=None)">
<%
    from ott.utils import html_utils
    return html_utils.get_first_param_safe_str(request, param_name, max_len, def_val)
%>
</%def>


<%def name="get_first_param(param_name, def_val=None)">
<%
    from ott.utils import html_utils
    return html_utils.get_first_param(request, param_name, def_val)
%>
</%def>



<%def name="has_url_param(param_name)">
<%
    from ott.utils import html_utils
    ret_val = False
    loc = html_utils.get_first_param(request, param_name)
    if loc:
        ret_val = True
    return ret_val
%>
</%def>

<%def name="get_locale(def_val='en')">
<%
    from ott.utils import html_utils
    ret_val = def_val
    try:
        loc = html_utils.get_first_param(request, '_LOCALE_')
        if loc:
            ret_val = loc
    except:
        ret_val = def_val
    return ret_val
%>
</%def>

<%def name="get_extra_params(def_val='')">
<%
    ''' extra_params: this variable is built here, and should be appended to all <a href> urls.  The string is pre-pended with
        an ampersand, so if there are no parameters on a given url, maybe add something bogus to the url prior to ${extra_parmas}
    '''
    extra_params=def_val

    # step 1: append any locale url param to extra_params... 
    loc = get_locale(None)
    if loc:
        extra_params = "{0}&_LOCALE_={1}".format(extra_params, loc)

    return extra_params
%>
</%def>

<%def name="pretty_date_from_ms(ms)"><%
    from ott.utils import date_utils
    pretty = date_utils.pretty_date_from_ms(ms)
%>${pretty}</%def>

<%def name="print_year()"><%
    from ott.utils import date_utils
    dt = date_utils.get_day_info()
%>${dt['year']}</%def>

<%def name="time_stamp()"><%
    from time import strftime as time
%><!-- built: ${'%m/%d/%Y at %H:%M' | time} --></%def>

<%def name="month_options(selected)">
    %for m in (_(u'January'), _(u'February'), _(u'March'), _(u'April'), _(u'May'), _(u'June'), _(u'July'), _(u'August'), _(u'September'), _(u'October'), _(u'November'), _(u'December')):
        <option value="${loop.index + 1}" ${'selected' if m == selected or str(loop.index+1) == str(selected) else ''} >${m}</option>
    %endfor
</%def>
<%def name="month_select(selected)"><select name="month" tabindex="7" id="month" class="regular">
    ${month_options(selected)}
    </select></%def>

<%def name="month_abbv_options(selected)">
    %for m in (_(u'Jan'), _(u'Feb'), _(u'Mar'), _(u'Apr'), _(u'May'), _(u'Jun'), _(u'Jul'), _(u'Aug'), _(u'Sep'), _(u'Oct'), _(u'Nov'), _(u'Dec')):
        <option value="${loop.index + 1}" ${'selected' if  m == selected or str(loop.index+1) == str(selected) else ''}>${m}</option>
    %endfor
</%def>
<%def name="month_abbv_select(selected)"><select name="month" tabindex="7" id="month" class="regular">
    ${month_abbv_options(selected)}
</select></%def>

<%def name="day_options(selected)">
    %for d in range(1, 32):
        <option value="${d}" ${'selected' if d == selected else ''}>${d}</option>
    %endfor
</%def>
<%def name="day_select(selected=1)"><select name="day" tabindex="8" id="day" class="regular">
    ${day_options(selected)}
    </select></%def>


<%def name="alerts(alert_list, img_url='/global/img/icon-alert.png')">
    %if alert_list and len(alert_list) > 0:
    <div id="alerts">
        %for a in alert_list:
        ${alert_content(a, img_url)}
        %endfor
    </div>
    %endif
</%def>

<%def name="alert_content(alert, img_url='/images/triptools/alert.png')">
    <p><img src="${url_domain()}${img_url}"/>
        %if header_text in alert and alert['header_text']:
        <b>${alert['header_text']}</b><br />
        %endif
        <b>${alert['route_short_names']}: </b> ${alert['description_text']} 
        %if alert['pretty_start_date']:
        <small>${_(u'As of')} ${alert['pretty_start_date']} <a href="${alert['url']}" target="#">${_(u'More')}</a></small>
        %endif
    </p>
</%def>

<%def name="compare_values(a, b)">
<%
    ret_val = False
    try:
        ret_val = float(a) == float(b)
    except:
        ret_val = a == b
    return ret_val
%>
</%def>

<%def name="or_bar(show_or=True)">
    %if show_or:
    <div class="or">
        <div class="or-bar"></div>
        <div class="or-text">${_(u'Or')}</div>
    </div>
    %endif
</%def>
