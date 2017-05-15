#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""weathersrb.py Python script

All this stuff at the top of the script is just optional metadata;
the real code starts on the "import re" line
"""

__author__ = "Ljubomir Kurij (kurijlj@gmail.com)"
__version__ = "0.3"
__date__ = "Date: 2012/01/27 20:32"
__copyright__ = "Copyright (c) 2012 Ljubomir Kurij"
__license__ = "Python"




import re
#import cgi
from os import path as pth
from xml.etree import ElementTree as et

import webapp2
#from google.appengine.api import users
#from google.appengine.ext import webapp2
#from google.appengine.api import urlfetch
#from google.appengine.ext.webapp.util import run_wsgi_app
#from google.appengine.ext.webapp import template




stations = {
	u'Palić' : u'Palić',
	u'Sombor' : u'Sombor',
	u'Novi Sad' : u'Novi Sad',
	u'Zrenjanin' : u'Zrenjanin',
	u'Kikinda' : u'Kikinda',
	u'Banatski Karlovac' : u'B. Karlovac',
	u'Loznica' : u'Loznica',
	u'Sremska Mitrovica' : u'S. Mitrovica',
	u'Valjevo' : u'Valjevo',
	u'Beograd' : u'Beograd',
	u'Kragujevac' : u'Kragujevac',
	u'Smederevska Palanka' : u'S. Palanka',
	u'Veliko Gradište' : u'V. Gradište',
	u'Crni Vrh' : u'Crni Vrh',
	u'Negotin' : u'Negotin',
	u'Zlatibor' : u'Zlatibor',
	u'Sjenica' : u'Sjenica',
	u'Požega' : u'Požega',
	u'Kraljevo' : u'Kraljevo',
	u'Kopaonik' : u'Kopaonik',
	u'Kuršumlija' : u'Kuršumlija',
	u'Kruševac' : u'Kruševac',
	u'Ćuprija' : u'Ćuprija',
	u'Niš' : u'Niš',
	u'Leskovac' : u'Leskovac',
	u'Zaječar' : u'Zaječar',
	u'Dimitrovgrad' : u'Dimitrovgrad',
	u'Vranje' : u'Vranje',
	}




#class WelcomePage(webapp2.RequestHandler):
#
#	def __init__(self):
#
#		self.pagedata = {
#				'app_path': u'',
#				#'page_path': u''.join("%s" % (self.get_url())),
#				'page_title': u'Welcome to Weather Serbia Appliaction',
#				'page_description': u'Weather Serbia welcome page',
#				'page_keywords': u'weather, serbia',
#				'logo_img': 'images/logo_128.png',
#				'logo_title': u'Weather Serbia',
#				'logo_desc': u'Current weather conditions for Serbia.',
#				'wlcm_message': u'Welcome to Weather Serbia Application Welcome Page. To proceed please login.',
#				'wlcm_error': u'',
#				'login_url': u''.join("%s" % (users.create_login_url("/stations"))),
#				}
#
#
#	def get(self):
#
#		user = users.get_current_user()
#
#		if user:
#
#			self.redirect("/stations")
#
#
#		else:
#
#			self.pagedata['app_path'] = self.request.application_url
#
#			path = pth.join(pth.dirname(__file__), 'welcome.html')
#			self.response.out.write(template.render(path, self.pagedata))




class StationsPage(webapp2.RequestHandler):

	def __init__(self):

		self.pagedata = {
				'app_path': u'',
				#'page_path': u''.join("%s" % (self.get_url())),
				'page_title': u'Current Weather Conditions for Serbia',
				'page_description': u'Weather Serbia weather stations',
				'page_keywords': u'weather, serbia, stations',
				'logo_img': 'images/logo_128.png',
				'logo_title': u'Weather Serbia',
				'logo_desc': u'Current weather conditions for Serbia.',
				'stations' : sorted(stations.keys()),
				'logout_url': u''.join("%s" % (users.create_logout_url("/"))),
				}


	def get(self):

		self.pagedata['app_path'] = self.request.application_url


		path = pth.join(pth.dirname(__file__), 'stations.html')
		self.response.out.write(template.render(path, self.pagedata))




#class WeatherPage(webapp2.RequestHandler):
#
#	def __init__(self):
#
#		self.url = u'http://www.hidmet.gov.rs/eng/osmotreni/index.rss'
#
#		self.pagedata = {
#				'app_path' : u'',
#				#'page_path': u''.join("%s" % (self.get_url())),
#				'page_title' : u'Current Weather Conditions for Serbia',
#				'page_description': u'Current weather conditions for Serbia',
#				'page_keywords': u'weather, serbia, current, conditions',
#				'wthr_img' : u'images/logo_128.png',
#				'wthr_desc' : u'weather',
#				'station_title': u'Weather Serbia',
#				'time_date' : u'Current weather conditions for Serbia.',
#				'logo_img': 'images/logo_128.png',
#				'logo_title': u'Weather Serbia',
#				'logo_desc': u'Current weather conditions for Serbia.',
#				'message' : u'',
#				'temp' : u'',
#				'press' : u'',
#				'hum' : u'',
#				'wspd' : u'',
#				'wdir' : u'',
#				'snow' : u'',
#				'logout_url': u''.join("%s" % (users.create_logout_url("/"))),
#				}
#
#
#	def get(self):
#
#		self.pagedata['app_path'] = self.pagedata['app_path'].join(u'%s' % (self.request.application_url))
#
#		station = cgi.escape(self.request.get('station'))
#
#		if station and stations.has_key(station):
#
#			result = urlfetch.fetch(self.url)
#			#f = open(u'./index.rss.txt', 'r')
#
#			if result.status_code == 200:
#			#if f:
#
#				lmnt = et.fromstring(result.content)
#			#	lmnt = et.fromstring(f.read())
#
#				pubdate = lmnt.getiterator('pubDate')[0].text.split('+')[0][:-1]
#
#				for node in lmnt.getiterator('item'):
#
#					if (u'Station: ' + stations[station]) == node.find('title').text:
#
#						desc = node.find('description').text
#
#						self.pagedata['page_title'] = u''.join(u'Current Weather Conditions for %s' % (station))
#						self.pagedata['station_title'] = u''.join(u'%s' % (station))
#						self.pagedata['time_date'] = u''.join(u'Current weather conditions for %s' % (pubdate))
#						self.pagedata['wthr_img'] = u'images/' + re.search(u'Weather description ID: .*?;', desc).group(0).split(':')[1][1:-1] + '.png'
#						self.pagedata['wthr_desc'] = re.search(u'Weather description: .*?;', desc).group(0).split(':')[1][1:-2]
#						self.pagedata['temp'] = re.search(u'Temperature: .*?;', desc).group(0).split(':')[1][1:-1]
#						self.pagedata['press'] = u'Pressure: ' + re.search(u'Pressure: .*?;', desc).group(0).split(':')[1][1:-1]
#						self.pagedata['hum'] = u'Humidity: ' + re.search(u'Humidity: .*?;', desc).group(0).split(':')[1][1:-1]
#
#
#						# These are old wind generating lines.
#						#self.pagedata['wspd'] = u'Wind speed: ' + re.search(u'Wind speed: .*?;', desc).group(0).split(':')[1][1:-1]
#						#self.pagedata['wdir'] = u'Wind direction: ' + re.search(u'Wind direction: .*?;', desc).group(0).split(':')[1][1:-1]
#
#						# Check is there wind at all.
#						wind = re.search(u'Wind speed: .*?;', desc).group(0).split(':')[1][1:-1]
#						if re.match("tiho", wind):
#							self.pagedata['wspd'] = u'Wind speed: quiet'
#							self.pagedata['wdir'] = u''
#						else:
#							self.pagedata['wspd'] = u'Wind speed: ' + wind
#							self.pagedata['wdir'] = u'Wind direction: ' + re.search(u'Wind direction: .*?;', desc).group(0).split(':')[1][1:-1]
#
#
#						# This is old snow generating line.
#						#self.pagedata['snow'] = u'Snow thickness: ' + re.search(u'Snow: .*?;', desc).group(0).split(':')[1][1:-1]
#
#						# Check is there snow at all.
#						snow = re.search(u'Snow: .*?;', desc).group(0).split(':')[1][1:-1]
#						if re.match("[0-9]+", snow):
#							self.pagedata['snow'] = u'Snow thickness: ' + snow
#						else:
#							self.pagedata['snow'] = u''
#
#
#			else:
#
#				self.pagedata['message'] = u'Can not retrieve data!'
#
#
#		else:
#
#			self.pagedata['message'] = u'No station or unknown station selected!'
#
#
#		path = pth.join(pth.dirname(__file__), 'weather.html')
#		self.response.out.write(template.render(path, self.pagedata))




class DefaultPage(webapp2.RequestHandler):

	def get(self):

		self.redirect("/")




#application = webapp2.WSGIApplication([('/', WelcomePage), ('/stations', StationsPage), ('/weather', WeatherPage), ('/.*', DefaultPage)], debug=True)
app= webapp2.WSGIApplication([('/', StationsPage)], debug=True)




#def main():
#	run_wsgi_app(application)
#
#
#if __name__ == "__main__":
#	main()
