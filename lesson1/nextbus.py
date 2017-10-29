#! /usr/bin/env python3

import urllib.request
from xml.etree.ElementTree import XML
import sys

if len(sys.argv) != 3:
    raise SystemExit("Usage : nextbus.py [route ID] [stop ID]")

stop = sys.argv[2]
route = sys.argv[1]
url = "http://www.ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={}&route={}".format(stop, route)

u = urllib.request.urlopen(url)
data = u.read()
doc = XML(data)

for pt in doc.findall(".//pt"):
    print(pt.text)



