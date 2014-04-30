cgiPath = '/common/info.cgi'
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

	section = parsingINI(httpRetBody)
	
	# Start checking ...

	# Check Model
	if checkString('model', PJ_MODEL, section['model']) == False:
		return False
	
	# Check Product
	if HAS_WIRELESS == 'yes':
		if checkString('product', PJ_PRODUCT_W, section['product']) == False:
			return False
	else:
		if checkString('product', PJ_PRODUCT, section['product']) == False:
			return False

	# Check Brand
	if checkString('brand', PJ_OEM, section['brand']) == False:
		return False

	# Check Version
	if checkString('version', PJ_OEM_VERSION, section['version']) == False:
		print ' ... Minor issue, keep going ...'
		
	# Check Build
	""" Do Nothing, build doesn't matter """

	# Check NIPCA Version
	if checkString('nipca', PJ_NIPCA_VER, section['nipca']) == False:
		return False

	# Check MODEL NAME
	if checkString('name', PJ_MODEL, section['name']) == False:
		print ' ... Minor issue, keep going ...'
	
	# Check Location
	# Check MAC Address
	if checkMacAddrFormat(section['macaddr']) == False:
		return False

	# Check IP Address
	#if checkIPFormat(section['ipaddr']) == False:
	if checkIPFormat('192.168.0.255') == False:
		return False

	# Check NetMask
	if checkIPFormat(section['netmask']) == False:
		return False

	# Check Gateway
	if checkIPFormat(section['gateway']) == False:
		return False

	# Check Wireless
	if HAS_WIRELESS == 'yes':
		if checkString('wireless', 'yes', section['wireless']) == False:
			return False
	else:
		if checkString('wireless', 'no', section['wireless']) == False:
			return False

	# Check Input
	if isNumber(section['inputs']) == False:
		return False

	# Check Output
	if isNumber(section['outputs']) == False:
		return False

	# Check Speaker
	if checkString('speaker', HAS_SPEAKER, section['speaker']) == False:
		return False

	# Check Videoout
	if checkString('videoout', HAS_VIDEOOUT, section['videoout']) == False:
		return False

	# Check PIR
	if checkString('pir', HAS_PIR, section['pir']) == False:
		return False

	# Check ICR
	if checkString('icr', HAS_ICR, section['icr']) == False:
		return False

	# Check IR
	if checkString('ir', HAS_IR, section['ir']) == False:
		return False

	# Check MIC
	if checkString('mic', HAS_MIC, section['mic']) == False:
		return False

	return True

	
def analyseReturnContent(httpRetCode, httpRetHeader, httpRetBody):
	# (None) -> bool
	#If analyse Okay return True, else return False
	#
	print '==== Check response from info.cgi ================================='
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
