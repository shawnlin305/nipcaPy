import re
import socket

def checkString(key, expectStr, retStr):
	""" (string, string, string) -> bool
	"""
	if expectStr != retStr:
		print 'WARNING : ' + key + ' != ' + expectStr + ' ( Response ' + retStr + ' )'
		return False
	else:
		return True

def isNumber(s):
	""" (string) -> bool
	"""
	try:
		float(s)
		return True
	except:
		return False

def checkMacAddrFormat(macAddr):
	""" (string) -> bool
	"""
	if re.match("^([a-fA-F0-9]{2}:?){5}[a-fA-F0-9]{2}$", macAddr):
		return True
	else :
		print 'WARNING : MAC Address Format incorrect (' + macAddr + ')'  
		return False

def checkIPFormat(IpAddr):
	""" (string) -> bool
	"""
	try:
		socket.inet_aton(IpAddr)
		return True
	except:
		print 'WARNING : IP Address Format incorrect (' + IpAddr + ')'
		return False

