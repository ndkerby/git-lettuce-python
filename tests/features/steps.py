from lettuce import *  
from selenium import webdriver
import urllib2 
import urllib
import pycurl
import StringIO
import json

def setup_email():
    URL = "http://sendgrid.com/api/mail.send.json"
    world.api_url = "http://sendgrid.com/api/mail.send.json"
    world.emailArgs={}

def set_credentials():
    world.emailArgs['api_user']="ndkerby"
    world.emailArgs['api_key']="Testing123"

def build_api_call():
    world.api_call=world.api_url + world.emailArgs

@step('Given I want to send an email')
def start_email(step):
    setup_email()

@step('I want to send an email to "(.*)", from "(.*)", with the subject "(.*)"')
def setup_required_fields(step, to_address, from_address, subject):
    world.emailArgs['to']= to_address
    world.emailArgs['from']= from_address
    world.emailArgs['subject']= subject

@step('Then I call the mail api')
def call_mail_api(step):
    set_credentials()
  # Initial Try: 
  #Received HTTPError: HTTP Error 400: Bad Request
    #json_data = json.dumps(world.emailArgs)
    #post_data = json_data.encode('utf-8')
    #req = urllib2.Request(world.api_url, post_data)
    #response = urllib2.urlopen(req)
    #world.the_page = response.read()
    
  # Second Try:   
  #Received HTTPError: HTTP Error 400: Bad Request
    #encode_data = urllib.urlencode(world.emailArgs)
    #request = urllib2.Request(world.api_url, encode_data)
    #response = urllib2.urlopen(request)
    #world.the_page = response.read() 

  # Third Try:      
  #Received error: (6, 'Could not resolve host: to=ndkerby%40gmail.com&api_key=Testing123&from=ndkerby%40gmail.com&api_user=ndkerby&subject=testing')
    email_request = pycurl.Curl()
    encode_data = urllib.urlencode(world.emailArgs)
    email_request.setopt(pycurl.URL,encode_data)
    world.email_request_page = StringIO.StringIO()
    email_request.setopt(pycurl.WRITEFUNCTION, world.email_request_page.write)    
    email_request.perform()
    email_request.close()

@step('I should recieve a success message')
def validate_success(step):
    assert world.email_request_page.getvalue()  == '{"message":"success"}'
