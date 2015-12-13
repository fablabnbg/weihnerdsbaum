#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# WiFi mac address sniffer (passive)
#
# (C) 2015 juewei@fabfolk.com (based on code from Adam Ziaja)

from scapy.all import *

def generate_manufacturer_index(file):
  """ generates a hash table from a file.
      You can download the needed file from like this:
      curl -s "https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf;hb=HEAD" > manuf.txt
  """
  vendor = {}
  for line in open(file).read().splitlines():
    if line.startswith('#') or len(line) < 7: continue
    (mac,remainder) = line.split('\t',1)
    if remainder is None or not "# " in remainder: continue
    (short_name,long_name) = remainder.split('# ',1)
    # some of the addresses have full 56-bit size and netmasks, some others are short.
    # we store the short formats.
    if mac.endswith('/16'): mac = mac[:5]
    if mac.endswith('/24'): mac = mac[:8]
    if mac.endswith('/25'): mac = mac[:8]
    if mac.endswith('/28'): mac = mac[:10]
    if mac.endswith('/32'): mac = mac[:11]
    if mac.endswith('/36'): mac = mac[:13]
    if mac.endswith('/40'): mac = mac[:14]
    if mac.endswith('/44'): mac = mac[:16]
    if mac.endswith('/45'): mac = mac[:16]
    if mac.endswith('/48'): mac = mac[:17]
    if mac.find('/') >= 0: print "unhandled netmask seen", mac
    # some addresses are written with '-', some with ':'. We store the ':' format.
    mac = mac.replace('-', ':')
    # we assert upper case, just to be safe. They all appear to use upper case.
    vendor[mac.upper()] = long_name
  return vendor

def lookup_manufacturer(manuf_table, mac):
  if mac is None: return None
  mac = mac.upper()
  if mac in manuf_table: return manuf_table[mac]
  if mac[:17] in manuf_table: return manuf_table[mac[:17]]
  if mac[:16] in manuf_table: return manuf_table[mac[:16]]
  if mac[:14] in manuf_table: return manuf_table[mac[:14]]
  if mac[:11] in manuf_table: return manuf_table[mac[:11]]
  if mac[:13] in manuf_table: return manuf_table[mac[:13]]
  if mac[:10] in manuf_table: return manuf_table[mac[:10]]
  if mac[:8]  in manuf_table: return manuf_table[mac[:8]]
  if mac[:5]  in manuf_table: return manuf_table[mac[:5]]
  return None

mac_seen = set()	# report every mac only once.
vendor = generate_manufacturer_index('manuf.txt')

def record_mac(pkt, addr):
  mac_seen.add(addr)
  if addr is None: return
  addr = addr.upper()
  f = open("seen.txt", "a")
  print >>f, addr, pkt.summary()
  f.close()
  if addr == '00:16:DC:67:7F:84': 
  	print "ASUS A10 seen =============================="
	sys.exit()
  if addr == '5C:51:4F:4C:13:50': print "t440s seen =============================="
  print "\n", len(mac_seen), addr, lookup_manufacturer(vendor, addr), "\n\t"+pkt.summary()


def Handler(pkt):
    # if pkt.haslayer(Dot11): # 802.11
    if pkt.addr1 not in mac_seen: record_mac(pkt, pkt.addr1)
    if pkt.addr2 not in mac_seen: record_mac(pkt, pkt.addr2)
    if pkt.addr3 not in mac_seen: record_mac(pkt, pkt.addr3)
    if pkt.addr4 not in mac_seen: record_mac(pkt, pkt.addr4)

sniff(iface="mon0", count=0, prn=Handler, store=0) # sudo rfkill unblock wifi && sudo airmon-ng start wlan0
