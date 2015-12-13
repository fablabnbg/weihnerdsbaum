#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

from FabLabNbgAPI import FabLabNbgAPI
import time

api = FabLabNbgAPI()
(state,since) = api.poll([ 'state/open', 'state/lastchange' ])

if state:
    print "Geöffnet",
else:
    print "Gechlossen",
print "seit", time.ctime(int(since))


