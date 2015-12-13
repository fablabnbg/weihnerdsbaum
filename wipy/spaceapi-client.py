#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import socket
import json
import time

version = '0.1'

class FabLabNbgAPI():
  """
  access the spaceapi data of FabLab Nuernberg
  """
  def __init__(self,ua='spaceapi/'+version):
    self.url_host = 'api.fablab-nuernberg.de'
    self.url_port = 80
    self.url_path = '/spaceapi.php'
    self.user_agent = ua

    # do not use HTTP/1.1 -> this gives us Transfer-Encoding: chunked and a long timeout with a simple recv() loop.
    self.request = "GET "+self.url_path+" HTTP/1.0\r\nUser-Agent: "+self.user_agent+"\r\nHost: "+self.url_host+"\r\nAccept: */*\r\n\r\n"
    self.url_addr = '188.40.30.16'	# skip DNS.

  def poll(self):
    s = socket.socket()
    s.connect(socket.getaddrinfo(self.url_addr, self.url_port)[0][4])
    s.send(self.request)
    f = s.makefile()
    txt = f.read()
    f.close()
    s.close()
    (header, body) = txt.split("\r\n\r\n", 1)
    return json.loads(body)


if __name__ == '__main__':
  api = FabLabNbgAPI()
  space = api.poll()

  if space['state']['open']:
    print "Geöffnet",
  else:
    print "Gechlossen",
  print "seit", time.ctime(int(space['state']['lastchange']))


