## -*- coding: utf-8 -*-
<%namespace name="util" file="/shared/utils/misc_utils.mako"/>
##
## BELOW ARE THE ABSTRACT METHODS (to be overridden by sub-classed templates) that populate this base page
##
<%def name="title()">${util.page_title('Transit Information')}</%def>

<%def name="nav_bar()"></%def>

<%def name="page_header()">
<%
    header_text = util.page_header()
    sub_header_text = util.page_sub_header()
    second_header_text = util.page_second_header()
%>
%if header_text:
<!-- Header start -->
<div class="standardheader">
    %if breadcrumb_text and TODO:
    <p class="breadcrumb"><a href="${util.url_domain()}/index.htm">Home</a> : ${breadcrumb_text}</p>
    %endif
    <h1>
        ${header_text|n}
    </h1>
    %if sub_header_text:
    <p class="h1sub">${sub_header_text|n}</p>
    %endif
    %if second_header_text:
    <div class="first">
        <p class="h1sub">${second_header_text|n}</p>
    </div>
    %endif
</div>
<!-- Header end -->
%endif
</%def>


<%def name="emergency_content()">
<%
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


<%def name="app_css()"><!--ABSTRACT app_css()--></%def>
<%def name="app_js()"><!--ABSTRACT app_js()--></%def>
<%def name="js_onload()">/** ABSTRACT js_onload() **/</%def>
<%def name="js_ui_include()"></%def>
<%def name="meta_data()">
    <meta name="Keywords"    content="Transit, Schedule, Information"/>
    <meta name="Description" content="Transit Information System"/>
</%def>
${next.body()}
