from bluepy.btle import Scanner, DefaultDelegate

##Scan Area for all Devices
class ScanDelegate(DefaultDelegate):
    def __init__(self)
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, scanEntry, isNewDev, isNewData)
		if isNewData:
			print ('Discovered device", scanEntry.addr)
		elif isNewData:
			print ('Recieved new data from", scanEntry.addr)
       
 	scanner = Scanner.withDelegate(ScanDelegate())
	devices = scanner.scan(10.0)

	for dev in devices:
		print('Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
		for(adtype, desc, value) in dev.getScanData():
			print('%s = %s' % (desc, value))

##Scan only for known device
##class ScanDelegate(DefaultDelegate):
##    def __init__(self)
##        DefaultDelegate.__init__(self)
##              
##while True:
##	scanner = Scanner.withDelegate(ScanDelegate())
##	devices = scanner.scan(10.0)
##
##	for dev in devices:
##		if(dev.addr = ''):
##			print('Device %s, RSSI=%d dB" % (dev.addr, dev.rssi)
