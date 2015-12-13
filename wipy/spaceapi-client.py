#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import FabLabNbgAPI
import time

api = FabLabNbgAPI.SpaceAPI()
(state,since) = api.poll([ 'state/open', 'state/lastchange' ])

if state:
    print "Geöffnet",
else:
    print "Gechlossen",
print "seit", time.ctime(int(since))


