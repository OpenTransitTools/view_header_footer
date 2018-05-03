## -*- coding: utf-8 -*-
<%namespace name="util" file="/shared/utils/hf_utils.mako"/>
##
## BELOW ARE THE ABSTRACT METHODS (to be overridden by sub-classed templates) that populate this base page
##
<%def name="title()">${util.page_title('Transit Information')}</%def>

<%def name="meta_data()">
    <meta name="robots"      content="noindex"/>
    <meta name="Keywords"    content="Transit, Schedule, Information, Trip Planning"/>
    <meta name="Description" content="Transit Information System"/>
</%def>

<%def name="favicon()">
    <link rel="shortcut icon" href="${util.url_domain()}/favicon.ico" type="image/x-icon">
    <link rel="icon" href="${util.url_domain()}/favicon.ico" type="image/x-icon">
</%def>

<%def name="nav_bar()"></%def>

<%def name="page_header()"><%
    header_text = util.page_header()
    sub_header_text = util.page_sub_header()
    second_header_text = util.page_second_header()
    icon_cls = util.page_icon_cls()
    icon_url = util.page_icon_url()
%>
%if header_text:
<!-- Header start -->
<div class="standardheader">
    %if breadcrumb_text and TODO:
    <p class="breadcrumb"><a href="${util.url_domain()}/index.htm">Home</a> : ${breadcrumb_text}</p>
    %endif
    %if icon_cls:
    <h1>
        %if icon_url:
        <a class="${icon_cls}" href="${icon_url}"></a>
        %else:
        <i class="${icon_cls}"></i>
        %endif
        ${header_text|n}
    </h1>
    %else:
    <h1>${header_text|n}</h1>
    %endif
    %if sub_header_text:
    <p class="h1sub">${sub_header_text|n}</p>
    %endif
    %if second_header_text:
    <div class="first">
        <p>${second_header_text|n}</p>
    </div>
    %endif
</div>
<!-- Header end -->
%endif
</%def>


<%def name="emergency_content()"><%
    em_content = util.emergency_content()
    em_type = util.emergency_type()
%>
%if em_content:
<div id="emergencyContainer">
  <div id="global-alert" class="show">
    <div id="NoticeBox">
      <div id="emergency">
          <p class="header">${em_content} <span class="update"> TIME TODO </span></p>
          <p>${em_content}</p>
      </div>
    </div>
  </div>
</div>
%endif
</%def>

<%def name="js_onload()"><%
    onload_function = util.page_onload()
    ret_val = "/** ABSTRACT **/"
    if onload_function:
        ret_val = "javascript:{}()".format(onload_function)
    return ret_val
%></%def>

<%def name="hf_include()"><!--ABSTRACT hf_include()--></%def>
<%def name="app_include()"><!--ABSTRACT app_include()--></%def>
${next.body()}
