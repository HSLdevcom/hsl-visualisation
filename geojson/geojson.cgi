#!/usr/bin/env python
#
# A simple CGI script to serve the JSON files as JSONP
# Used to work around the same-origin policy of browser javascript

import cgitb
cgitb.enable()

import cgi

fs = cgi.FieldStorage()
callback = fs.getfirst("callback")
line = fs.getfirst("line")

print "Content-type: text/plain"
print

if callback:
    print callback + "("

if line and not "/" in line:
    body = open("gtfs2geojson/%s.json" % line).read()
    print body

if callback:
    print ");"
