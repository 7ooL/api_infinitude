import ConfigParser
import pyInfinitude

private = ConfigParser.RawConfigParser()
private.read('/home/host/home_auto_scripts/private.ini')

ip = private.get('hvac', 'ip')
port = private.get('hvac', 'port')
file = 'infinitude.json'

hvac = pyInfinitude.infinitude(ip,port,file)

hvac.pullConfig()
#hvac.get_blight()
#hvac.set_blight(61)
#hvac.get_blight()
hvac.get_ue_demandClAbs()
hvac.set_ue_demandClAbs(82)
hvac.get_ue_demandClAbs()

hvac.pushConfig()


