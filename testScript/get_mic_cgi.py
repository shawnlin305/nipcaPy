cgiPath = '/config/mic.cgi'
httpAuth = 'BASIC' # or 'DIGEST'
postParameter = ''
retFormat = 'INI' # or 'XML'

from parseIni import parsingINI
from model import *
from commonCheck import *

def isRetCodeOK(httpRetCode):
	""" (str) -> bool
	Check HTTP Return Code is 2xx.
	Is return code is 2xx(success) return True, else return False
	"""
	print 'Return Code :', httpRetCode
	if (int(httpRetCode) // 100) == 2:
		return True
	else:
		return False

def isBodyOK(httpRetBody):
	""" None -> bool
	Check http response body according return format.
	"""
	return True

def analyseReturnContent(httpRetCode, httpRetHeader, httpRetBody):
	# (None) -> bool
	#If analyse Okay return True, else return False
	#
	print '==== Check response from mic.cgi ================================='
	# Dump result
	#print httpRetHeader
	#print httpRetBody

	# Check Return HTTP Code
	if isRetCodeOK(httpRetCode) == False:
		print 'HTTP Response Code Error : ', httpRetCode
		return False
	
	# Check Return Body
	if isBodyOK(httpRetBody) == False:
		print 'Check Return Body Failed : '
		return False

	return True
