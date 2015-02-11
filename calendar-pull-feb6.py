from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
from collections import OrderedDict

import httplib2
import collections


# From Configure your App
import gflags
import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run
import json

FLAGS = gflags.FLAGS

# Set up a Flow object to be used if we need to authenticate. This
# sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
# the information it needs to authenticate. Note that it is called
# the Web Server Flow, but it can also handle the flow for native
# applications
# The client_id and client_secret can be found in Google Developers Console
FLOW = OAuth2WebServerFlow(
    client_id='317796910577.apps.googleusercontent.com',
    client_secret='IvKDHSorjkShs8YHxZtya5-U',
    scope='https://www.googleapis.com/auth/calendar.readonly',
    user_agent='YOUR_APPLICATION_NAME/YOUR_APPLICATION_VERSION')

# To disable the local server feature, uncomment the following line:
# FLAGS.auth_local_webserver = False

# If the Credentials don't exist or are invalid, run through the native client
# flow. The Storage object will ensure that if successful the good
# Credentials will get written back to a file.
storage = Storage('calendar.dat')
credentials = storage.get()
if credentials is None or credentials.invalid == True:
  credentials = run(FLOW, storage)

# Create an httplib2.Http object to handle our HTTP requests and authorize it
# with our good Credentials.
http = httplib2.Http()
http = credentials.authorize(http)

# Build a service object for interacting with the API. Visit
# the Google Developers Console
# to get a developerKey for your own application.
service = build(serviceName='calendar', version='v3', http=http,
       developerKey='AIzaSyDdUN2cGXtCmCICZbKvyrrea9Gb6uT-FlM')
#print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
calendar = service.calendars().get(calendarId='erin.mcgill@controlgroup.com').execute()
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
dict_cal_entries = service.calendarList().list().execute()
print "This is the type that service.calendarlist (meaning this is dict_cal_entries) returns"
print type(dict_cal_entries)
print ""
print "*****************************************"
print ""
whatever = dict_cal_entries['items'][10]['summary']
whatever2 = dict_cal_entries['items'][10]['id']
# can join everything on the list: l = join.str(list, ';')
my_items =  whatever + ',' + whatever2
print my_items
print ""
print ""
print "This is a dict_cal_entries['items'][0]['summary']"
print dict_cal_entries['items'][0]['summary']
print ""
print ""
print "Maybe this is the type of dictcalentries[items]"
print type(dict_cal_entries['items'])
list_cal_entries = dict_cal_entries['items']
print ""
print "This is the list_cal_entries[0]"
print list_cal_entries[0]
print ""
print "Trying to find the number of entries in the list of items - should be number of dictionaries in the list"
print len(list_cal_entries)

print "We'll see if the for loop to give us the entry and the entry's summary works"
position = 0
for entry in list_cal_entries:
  print str(position) + ' ' + list_cal_entries[position]['summary']
  position = position + 1
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
##print "This is what calendarList.get returns"
##get_cal_list = service.calendarList().get(calendarId='erin.mcgill@controlgroup.com').execute()
##print get_cal_list
## Get events for the last week
#   For each of these events, print out the following:
#     - description
#     - start
#     - organizer
#     - 
events = service.events().list(calendarId='erin.mcgill@controlgroup.com').execute()
#events = service.events().list(calendarId='erin.mcgill@gmail.com').execute()
print "This is the type that service.events.list returns"
print type(events)
things = events['items']
#print "These are the things!"
#print things
print things[0]['creator']
print things[0]['description']
print things[0]['start']
print "There are this many things: " + str(len(things))
position_in_events = 0
for entry in things:
#  if "2014" in str(things[position]['start']):
    print str(position) 
#    print "The creator: " + str(things[position]['creator']['displayName'])
#    print "The description: " + str(things[position]['description'])
    print "The start time: " + str(things[position]['start'])
#print things[0]['creator']
#print things[0]['description']
#print things[0]['start']
string_of_items = str(things)
number = len(string_of_items)
