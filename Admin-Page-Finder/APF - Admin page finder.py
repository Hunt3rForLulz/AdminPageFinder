#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError
def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1
def findPage():
	f = open("web.txt","r");
	link = raw_input("Enter Site Name: ")
	print "\n\n Pages : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print ">>> ",req_link
def header():
	Space(9); print "-----------------------------"
	Space(9); print " +-+-+Admin Page Finder+-+-+ "
	Space(9); print "-----------------------------" 

header()
findPage()
