## -*- coding: utf-8 -*-
<%def name="page_title(def_val='')"><%
    ret_val = def_val
    t = get_first_param_safe_str('title')
    if t:
        ret_val = t
    else:
        h = get_first_param_safe_str('header', strip_url=True)
        if h:
            ret_val = h
    return ret_val
%></%def>


<%def name="alerts_banner()"><%
%></%def>


<%def name="page_header(def_val=None)"><% return get_first_param_safe_str('header', 200, def_val)%></%def>
<%def name="page_sub_header(def_val=None)"><% return get_first_param_safe_str('sub_header', 200, def_val)%></%def>
<%def name="page_second_header(def_val=None)"><% return get_first_param_safe_str('second_header', 200, def_val)%></%def>
<%def name="page_icon_cls(def_val=None)"><% return get_first_param_safe_str('icon_cls', 60, def_val)%></%def>
<%def name="page_icon_url(def_val=None)"><% return get_first_param_safe_str('icon_url', 200, def_val)%></%def>
<%def name="page_onload()"><% return get_first_param_safe_str('onload')%></%def>

<%def name="emergency_content(def_val=None)"><% return get_first_param_safe_str('emergency_content', 200, def_val)%></%def>
<%def name="emergency_type(def_val='caution')"><% return get_first_param_safe_str('emergency_type', 30, def_val)%></%def>

<%def name="alert_banner()">
<div id="global-alert" class="show" data-alert-updated="2018-02-20T7:58">
    <div id="WeatherEmergency">
        <div id="emergency">
            <p class="header">Winter Weather Continues <span class="update">Updated: 7:58 a.m., Tue. Feb. 20, 2018</span></p>
            <p>With changing weather conditions, some bus lines in higher elevations are canceled and buses on some other lines are using chains. Chained buses cannot run faster than 25 mph. Plus, the forecast has the possibility of more snow moving in during the afternoon commute. Plan extra time, keep an eye on the weather and check trimet.org/alerts before you go.  <a href="http://trimet.org/alerts/winterweather.htm">More</a></p>
        </div>
    </div>
</div>
</%def>


<%def name="get_ini_param(name, def_val=None)"><%
    ret_val = def_val
    try:
        ret_val = request.registry.settings[name]
        ret_val.strip()
    except Exception as e:
        #print e
        pass
    return ret_val
%></%def>

<%def name="url_domain()"><% return get_ini_param('ott.url_domain', '') %></%def>
<%def name="is_test()"><% return get_ini_param('ott.is_test') %></%def>


<%def name="get_first_param_safe_str(param_name, max_len=60, strip_url=False, def_val=None)"><%
    from ott.utils import html_utils
    return html_utils.get_first_param_safe_str(request, param_name, max_len, strip_url, def_val)
%></%def>


<%def name="get_first_param(param_name, def_val=None)"><%
    from ott.utils import html_utils
    return html_utils.get_first_param(request, param_name, def_val)
%></%def>


<%def name="has_url_param(param_name)"><%
    from ott.utils import html_utils
    ret_val = False
    loc = html_utils.get_first_param(request, param_name)
    if loc:
        ret_val = True
    return ret_val
%></%def>

<%def name="get_locale(def_val='en')"><%
    from ott.utils import html_utils
    ret_val = def_val
    try:
        loc = html_utils.get_first_param(request, '_LOCALE_')
        if loc:
            ret_val = loc
    except:
        ret_val = def_val
    return ret_val
%></%def>

<%def name="get_extra_params(def_val='')"><%
    ''' extra_params: this variable is built here, and should be appended to all <a href> urls.  The string is pre-pended with
        an ampersand, so if there are no parameters on a given url, maybe add something bogus to the url prior to ${extra_parmas}
    '''
    extra_params=def_val

    # step 1: append any locale url param to extra_params...
    loc = get_locale(None)
    if loc:
        extra_params = "{0}&_LOCALE_={1}".format(extra_params, loc)

    return extra_params
%></%def>

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
