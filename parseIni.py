def parsingINI(iniString):

	iniSection = {}

	for line in iniString.split('\n'):
		line = line.lstrip()
		line = line.rstrip("\r\n")
		if '=' in line:
			key, value = line.split('=', 1)
			iniSection[key] = value.rstrip()
	"""
	for key in list(iniSection):
		print key + '=' + iniSection[key]
	"""
	return iniSection
