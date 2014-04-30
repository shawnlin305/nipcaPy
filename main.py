# Public Python Library
import pycurl
import cStringIO
import sys
sys.path.append('testScript')

# Local Python Library
from camInfo import *

# Global value
httpRetCode = ''
httpRetHeader = cStringIO.StringIO()
httpRetBody = cStringIO.StringIO()

def debug(debug_type, debug_msg):
	""" 
	Support debug_type as : 
	CURLINFO_TEXT(0)
	CURLINFO_HEADER_IN(1)
	CURLINFO_HEADER_OUT(2)
	CURLINFO_DATA_IN(3) 
	CURLINFO_DATA_OUT(4)
	""" 
	if (debug_type == 2) and (len(debug_msg) < 300):
		for msg in debug_msg.split('\n'):
			print ">>> %s" % msg.strip()

def cleanHttpResponse():
	""" (None) -> (None)
	""" 
	httpRetCode = ''
	httpRetHeader.truncate(0)
	httpRetBody.truncate(0)

def sendRequest():
	""" (None) -> (None)
	""" 
	# Clean HTTP response to avoid confusing 
	cleanHttpResponse()

	# Send CGI request.
	testCgi = pycurl.Curl()
	testCgi.setopt(pycurl.USERPWD, username + ":" +  passwd)
	testCgi.setopt(pycurl.URL, 'http://' + camIP + ':' + str(camPort) + cgiPath)
	if postParameter:
		testCgi.setopt(pycurl.POSTFIELDS, postParameter)
	testCgi.setopt(pycurl.VERBOSE, True)
	testCgi.setopt(pycurl.DEBUGFUNCTION, debug)
	testCgi.setopt(pycurl.HEADERFUNCTION, httpRetHeader.write)
	testCgi.setopt(pycurl.WRITEFUNCTION, httpRetBody.write)
	if httpAuth is 'DIGEST':
		testCgi.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_DIGETS)
	testCgi.perform()

	# Get Return information
	global httpRetCode 
	httpRetCode = testCgi.getinfo(pycurl.RESPONSE_CODE)
	testCgi.close()


"""
Run testing
"""
from get_info_cgi import *
sendRequest()
if analyseReturnContent(httpRetCode, httpRetHeader.getvalue(), httpRetBody.getvalue()) == True:
	print ('\033[1;31;32m' + 'HTTP GET info.cgi Pass!' + '\033[0m')
else:
	print ('\033[1;31;31m' + 'HTTP GET info.cgi Failure!' + '\033[0m')

from get_mic_cgi import *
sendRequest()
if analyseReturnContent(httpRetCode, httpRetHeader.getvalue(), httpRetBody.getvalue()) == True:
	print ('\033[1;31;32m' + 'HTTP GET info.cgi Pass!' + '\033[0m')
else:
	print ('\033[1;31;31m' + 'HTTP GET info.cgi Failure!' + '\033[0m')

