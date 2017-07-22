import requests
import json
import logging
from logging.config import BaseConfigurator

logging.config.fileConfig('../logging.ini')

class infinitude:

  def __init__(self, hvacIP, hvacPort, jsonFile):
    self.ip  =  hvacIP
    self.port  = hvacPort
    self.file  = jsonFile

  def pullConfig(self):
    api_url='http://'+str(self.ip)+':'+str(self.port)+'/systems.json'
    r = requests.get(api_url)
    logging.debug(r)
    with open(self.file, 'w') as f:
      f.write(r.text)
    f.close()

  def pushConfig(self):
    api_url='http://'+str(self.ip)+':'+str(self.port)+'/systems/infinitude'
    c = self.loadJson()
    r = requests.post(api_url, data=c)
    logging.debug(r)

  def loadJson(self):
    f = open(self.file, 'r')
    j = f.read() 
    f.close()
    return j

  def writeJson(self, c):
    f = open(self.file, 'w')
    j = f.write(json.dumps(c)) 
    f.close()

  def get_blight(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['blight'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_blight(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['blight'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_cfgauto(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgauto'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgauto(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgauto'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_cfgchgovr(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgchgovr'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgchgovr(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgchgovr'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_cfgcph(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgcph'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgcph(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgcph'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_cfgdead(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgdead'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgdead(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgdead'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_cfgem(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgem'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgem(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgem'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_cfgfan(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgfan'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgfan(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgfan'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_cfghumid(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfghumid'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfghumid(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfghumid'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_cfgpgm(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgpgm'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgpgm(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgpgm'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_cfgrecovery(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgrecovery'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgrecovery(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgrecovery'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_cfgtype(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgtype'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgtype(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgtype'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_cfguv(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfguv'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfguv(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfguv'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_cfgvent(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgvent'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgvent(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgvent'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_cfgzoning(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgzoning'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgzoning(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgzoning'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_ducthour(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['ducthour'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ducthour(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['ducthour'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_erate(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['erate'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_erate(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['erate'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_filterinterval(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['filterinterval'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_filterinterval(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['filterinterval'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_filtertype(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['filtertype'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_filtertype(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['filtertype'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_filtrrmd(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['filtrrmd'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_filtrrmd(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['filtrrmd'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_fueltype(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['fueltype'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_fueltype(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['fueltype'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_gasunit(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['gasunit'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_gasunit(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['gasunit'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_grate(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['grate'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_grate(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['grate'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_heatsource(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['heatsource'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_heatsource(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['heatsource'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_humidityfan(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityfan'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_humidityfan(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityfan'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_huminterval(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['huminterval'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_huminterval(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['huminterval'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_humoff(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humoff'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_humoff(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humoff'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_humrmd(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humrmd'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_humrmd(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humrmd'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_mode(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['mode'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_mode(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['mode'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_optmpoff(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['optmpoff'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_optmpoff(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['optmpoff'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_screensaver(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['screensaver'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_screensaver(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['screensaver'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_sound(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['sound'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_sound(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['sound'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_statpressmon(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['statpressmon'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_statpressmon(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['statpressmon'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_uvinterval(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['uvinterval'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_uvinterval(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['uvinterval'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_uvrmd(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['uvrmd'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_uvrmd(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['uvrmd'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_vacat(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['vacat'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_vacat(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['vacat'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_vacend(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['vacend'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_vacend(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['vacend'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_vacfan(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['vacfan'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_vacfan(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['vacfan'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_vacmaxt(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['vacmaxt'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_vacmaxt(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['vacmaxt'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_vacmint(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['vacmint'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_vacmint(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['vacmint'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_vacstart(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['vacstart'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_vacstart(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['vacstart'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_ventinterval(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['ventinterval'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ventinterval(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['ventinterval'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_ventrmd(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['ventrmd'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ventrmd(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['ventrmd'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_ha_humid(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['humid'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_humid(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityAway'][0]['humid'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_ha_humidifier(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['humidifier'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_humidifier(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityAway'][0]['humidifier'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_ha_rclg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['rclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_rclg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityAway'][0]['rclg'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_ha_rhtg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['rhtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def get_ha_rclgovercool(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['rclgovercool'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_rclgovercool(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityAway'][0]['rclgovercool'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_ha_ventclg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['ventclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_ventclg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityAway'][0]['ventclg'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_ha_venthtg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['venthtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_venthtg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityAway'][0]['venthtg'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_ha_ventspdclg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['ventspdclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_ventspdclg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityAway'][0]['ventspdclg'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_ha_ventspdhtg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['ventspdhtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_ventspdhtg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityAway'][0]['ventspdhtg'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hh_humid(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['humid'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_humid(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['humid'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hh_humidifier(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['humidifier'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_humidifier(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['humidifier'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hh_rclg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['rclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_rclg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['rclg'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hh_rhtg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['rhtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_rhtg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['rhtg'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hh_rclgovercool(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['rclgovercool'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_rclgovercool(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['rclgovercool'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hh_ventclg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['ventclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_ventclg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['ventclg'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hh_venthtg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['venthtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_venthtg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['venthtg'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hh_ventspdclg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['ventspdclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_ventspdclg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['ventspdclg'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hh_ventspdhtg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['ventspdhtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_ventspdhtg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['ventspdhtg'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hv_humid(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['humid'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_humid(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['humid'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hv_humidifier(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['humidifier'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_humidifier(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['humidifier'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hv_rclg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['rclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_rclg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['rclg'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hv_rhtg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['rhtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_rhtg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['rhtg'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hv_rclgovercool(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['rclgovercool'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_rclgovercool(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['rclgovercool'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hv_ventclg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['ventclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_ventclg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['ventclg'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hv_venthtg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['venthtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv
	
  def set_hv_venthtg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['venthtg'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hv_ventspdclg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['ventspdclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_ventspdclg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['ventspdclg'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

  def get_hv_ventspdhtg(self):
    c = self.loadJson()
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['ventspdhtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_ventspdhtg(self, value):
    c = self.loadJson()
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['ventspdhtg'] = [value]
    self.writeJson(jo)
    logging.debug(str(value))

