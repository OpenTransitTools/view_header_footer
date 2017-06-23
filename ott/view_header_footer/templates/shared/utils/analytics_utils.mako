## -*- coding: utf-8 -*-
##
## routines for making ga skinny
##
<%def name="ga_init()"><%
    # TODO: grab ga number from config ... if no number, no GA
    # TODO: update GA init code below...
    account='UA-688646-3'
%>
<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', '${account}']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>
</%def>

#
# event call to GA
# _gaq.push(['_trackEvent', 'Your App Name Here', 'Event Name (submit)', 'Longer Event Description Text']);
#
<%def name="event(app, evt, desc)">onClick="_gaq.push(['_trackEvent', '${app}', '${evt}', '${desc}']);"</%def>
submit=event('OttHeaderFooter', 'Menu-Click', ' clicked the menu bar')

<%def name="empty_method()"></%def>