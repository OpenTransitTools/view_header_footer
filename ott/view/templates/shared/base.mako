## -*- coding: utf-8 -*-
<%namespace name="util" file="/shared/utils/misc_utils.mako"/>
##
## BELOW ARE THE ABSTRACT METHODS (to be overridden by sub-classed templates) that populate this base page
##
<%def name="title()">${util.page_title('Transit Information')}</%def>
<%def name="page_header()">${util.page_header()}</%def>
<%def name="emergency_content()"><!-- ABSTRACT emergency_content() --></%def>
<%def name="app_css()"><!--ABSTRACT app_css()--></%def>
<%def name="app_js()"><!--ABSTRACT app_js()--></%def>
<%def name="js_onload()">/** ABSTRACT js_onload() **/</%def>
<%def name="js_ui_include()">
    <!-- jquery and menu are needed to make the trimet header drop down work ... usually included at bottom on page -->
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js" type="text/javascript"></script>
    <script src="${util.url_domain()}/global/js/menu.min.js" type="text/javascript"></script>
</%def>
<%def name="meta_data()">
    <meta name="Keywords"    content="Transit, Schedule, Information"/>
    <meta name="Description" content="Transit Information System"/>
</%def>
${next.body()}
