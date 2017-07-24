import requests
import json
import time
import logging

class infinitude:

  def __init__(self, hvacIP, hvacPort, jsonFile, statusFile):
    self.ip  =  hvacIP
    self.port  = hvacPort
    self.file  = jsonFile
    self.status = statusFile

  def __is_on_or_off(self, i):
    if i == 'on' or i == 'off':
      return True
    logging.error(str(i)+' must be "on" or "off"')
    return False

  def __is_int(self, i):
    if isinstance(i, int):
      return True
    logging.error(str(i)+' must an integer')
    return False

  def __is_float(self, i):
    if isinstance(i, float):
      return True
    logging.error(str(i)+' must an float')
    return False

  def __is_in_range(self, i, l, u):
    if l <= i <= u:
      return True
    logging.error(str(i)+' must be between '+str(l)+' and '+str(u))
    return False

  def __is_string(self, i):
    if isinstance(i, string):
      return True
    logging.error(str(i)+' must a string')
    return False

  def __is_valid_time(self, i):
    try:
        time.strptime(i, '%H:%M')
        return True
    except ValueError:
        logging.error(str(i)+' time is wrong format')
        return False

  def __is_valid_activity(self, i):
    if i == 'home' or i == 'away' or i == 'wake' or i == 'sleep' or i == 'manual':
      return True
    logging.error(str(i)+' must be wake, home, sleep, away, or manual')
    return False

  def pullStatus(self):
    api_url='http://'+str(self.ip)+':'+str(self.port)+'/status.json'
    r = requests.get(api_url)
    if r.status_code == requests.codes.ok :
      with open(self.status, 'w') as f:
        f.write(r.text)
      f.close()
      return True
    else:
      logging.error(r)
      return False

  def pullConfig(self):
    api_url='http://'+str(self.ip)+':'+str(self.port)+'/systems.json'
    r = requests.get(api_url)
    if r.status_code == requests.codes.ok :
      with open(self.file, 'w') as f:
        f.write(r.text)
      f.close()
      return True
    else:
      logging.error(r)
      return False

  def pushConfig(self):
    api_url='http://'+str(self.ip)+':'+str(self.port)+'/systems/infinitude'
    c = self.loadJson(self.file)
    r = requests.post(api_url, data=c)
    if r.status_code == requests.codes.ok :
      return True
    else:
     logging.error(r)
     return False

  def loadJson(self, file):
    f = open(file, 'r')
    j = f.read() 
    f.close()
    return j

  def writeJson(self, c):
    f = open(self.file, 'w')
    j = f.write(json.dumps(c)) 
    f.close()

  def get_blight(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['blight'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_blight(self, value):
    if self.__is_int(value) and self.__is_in_range(value,0,100):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['blight'] = [json.dumps(value)]
      self.writeJson(jo)
      logging.info(str(value))

  def get_cfgauto(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgauto'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgauto(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['cfgauto'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_cfgchgovr(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgchgovr'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgchgovr(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgchgovr'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_cfgcph(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgcph'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgcph(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgcph'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_cfgdead(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgdead'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgdead(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgdead'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_cfgem(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgem'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgem(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgem'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_cfgfan(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgfan'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgfan(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['cfgfan'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_cfghumid(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfghumid'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfghumid(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['cfghumid'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_cfgpgm(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgpgm'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgpgm(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['cfgpgm'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_cfgrecovery(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgrecovery'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgrecovery(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['cfgrecovery'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_cfgtype(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgtype'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgtype(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['cfgtype'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_cfguv(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfguv'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfguv(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['cfguv'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_cfgvent(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgvent'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgvent(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['cfgvent'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_cfgzoning(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['cfgzoning'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_cfgzoning(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['cfgzoning'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_ducthour(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['ducthour'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ducthour(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['ducthour'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_erate(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['erate'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_erate(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['erate'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_filterinterval(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['filterinterval'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_filterinterval(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['filterinterval'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_filtertype(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['filtertype'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_filtertype(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['filtertype'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_filtrrmd(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['filtrrmd'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_filtrrmd(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['filtrrmd'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_fueltype(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['fueltype'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_fueltype(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['fueltype'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_gasunit(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['gasunit'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_gasunit(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['gasunit'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_grate(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['grate'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_grate(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['grate'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_heatsource(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['heatsource'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_heatsource(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['heatsource'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_humidityfan(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityfan'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_humidityfan(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humidityfan'] = [json.dumps(value)]
      self.writeJson(jo)
      logging.info(str(value))

  def get_huminterval(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['huminterval'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_huminterval(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['huminterval'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_humoff(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humoff'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_humoff(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humoff'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_humrmd(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humrmd'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_humrmd(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humrmd'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_mode(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['mode'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_mode(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['mode'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_optmpoff(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['optmpoff'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_optmpoff(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['optmpoff'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_screensaver(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['screensaver'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_screensaver(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['screensaver'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_sound(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['sound'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_sound(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['sound'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_statpressmon(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['statpressmon'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_statpressmon(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['statpressmon'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_uvinterval(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['uvinterval'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_uvinterval(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['uvinterval'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_uvrmd(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['uvrmd'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_uvrmd(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['uvrmd'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_vacat(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['vacat'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_vacat(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['vacat'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_vacend(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['vacend'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_vacend(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['vacend'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_vacfan(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['vacfan'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_vacfan(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['vacfan'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_vacmaxt(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['vacmaxt'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_vacmaxt(self, value):
    if self.__is_float(value) and self.__is_in_range(value,0,100):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['vacmaxt'] = [json.dumps(value)]
      self.writeJson(jo)
      logging.info(str(value))

  def get_vacmint(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['vacmint'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_vacmint(self, value):
    if self.__is_float(value) and self.__is_in_range(value,0,100):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['vacmint'] = [json.dumps(value)]
      self.writeJson(jo)
      logging.info(str(value))

  def get_vacstart(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['vacstart'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_vacstart(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['vacstart'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ventinterval(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['ventinterval'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ventinterval(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['ventinterval'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ventrmd(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['ventrmd'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ventrmd(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['ventrmd'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_ha_humid(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['humid'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_humid(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityAway'][0]['humid'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ha_humidifier(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['humidifier'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_humidifier(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humidityAway'][0]['humidifier'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_ha_rclg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['rclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_rclg(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityAway'][0]['rclg'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ha_rhtg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['rhtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def get_ha_rclgovercool(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['rclgovercool'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_rclgovercool(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humidityAway'][0]['rclgovercool'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_ha_ventclg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['ventclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_ventclg(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humidityAway'][0]['ventclg'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_ha_venthtg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['venthtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_venthtg(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humidityAway'][0]['venthtg'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_ha_ventspdclg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['ventspdclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_ventspdclg(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityAway'][0]['ventspdclg'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ha_ventspdhtg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityAway'][0]['ventspdhtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ha_ventspdhtg(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityAway'][0]['ventspdhtg'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_hh_humid(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['humid'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_humid(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['humid'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_hh_humidifier(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['humidifier'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_humidifier(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humidityHome'][0]['humidifier'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_hh_rclg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['rclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_rclg(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['rclg'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_hh_rhtg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['rhtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_rhtg(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['rhtg'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_hh_rclgovercool(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['rclgovercool'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_rclgovercool(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humidityHome'][0]['rclgovercool'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_hh_ventclg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['ventclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_ventclg(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humidityHome'][0]['ventclg'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_hh_venthtg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['venthtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_venthtg(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humidityHome'][0]['venthtg'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_hh_ventspdclg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['ventspdclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_ventspdclg(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['ventspdclg'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_hh_ventspdhtg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityHome'][0]['ventspdhtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hh_ventspdhtg(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityHome'][0]['ventspdhtg'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_hv_humid(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['humid'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_humid(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['humid'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_hv_humidifier(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['humidifier'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_humidifier(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humidityVacation'][0]['humidifier'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_hv_rclg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['rclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_rclg(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['rclg'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_hv_rhtg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['rhtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_rhtg(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['rhtg'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_hv_rclgovercool(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['rclgovercool'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_rclgovercool(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humidityVacation'][0]['rclgovercool'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_hv_ventclg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['ventclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_ventclg(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humidityVacation'][0]['ventclg'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_hv_venthtg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['venthtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_venthtg(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['humidityVacation'][0]['venthtg'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_hv_ventspdclg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['ventspdclg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_ventspdclg(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['ventspdclg'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_hv_ventspdhtg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['humidityVacation'][0]['ventspdhtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_hv_ventspdhtg(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['humidityVacation'][0]['ventspdhtg'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ue_demandClAbs(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['utilityEvent'][0]['demandClAbs'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ue_demandClAbs(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['utilityEvent'][0]['demandClAbs'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ue_demandHtAbs(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['utilityEvent'][0]['demandHtAbs'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ue_demandHtAbs(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['utilityEvent'][0]['demandHtAbs'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ue_demandOffset(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['utilityEvent'][0]['demandOffset'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ue_demandOffset(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['utilityEvent'][0]['demandOffset'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ue_maxLimit(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['utilityEvent'][0]['maxLimit'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ue_maxLimit(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['utilityEvent'][0]['maxLimit'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ue_minLimit(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['utilityEvent'][0]['minLimit'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ue_minLimit(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['utilityEvent'][0]['minLimit'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ue_priceClAbs(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['utilityEvent'][0]['priceClAbs'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ue_priceClAbs(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['utilityEvent'][0]['priceClAbs'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ue_priceHtAbs(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['utilityEvent'][0]['priceHtAbs'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ue_priceHtAbs(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['utilityEvent'][0]['priceHtAbs'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ue_priceLimit(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['utilityEvent'][0]['priceLimit'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ue_priceLimit(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['utilityEvent'][0]['priceLimit'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ue_priceOffset(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['utilityEvent'][0]['priceOffset'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ue_priceOffset(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['utilityEvent'][0]['priceOffset'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ue_demandResp(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['utilityEvent'][0]['demandResp'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ue_demandResp(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['utilityEvent'][0]['demandResp'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ue_enabled(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['utilityEvent'][0]['enabled'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ue_enabled(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['utilityEvent'][0]['enabled'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_ue_priceResp(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['utilityEvent'][0]['priceResp'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ue_priceResp(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['utilityEvent'][0]['priceResp'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_ue_restoreDefaults(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['utilityEvent'][0]['restoreDefaults'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_ue_restoreDefaults(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['utilityEvent'][0]['restoreDefaults'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_wh_hold(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['wholeHouse'][0]['hold'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_wh_hold(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['wholeHouse'][0]['hold'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_wh_holdActivity(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['wholeHouse'][0]['holdActivity'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_wh_holdActivity(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['wholeHouse'][0]['holdActivity'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  def get_wh_otmr(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['wholeHouse'][0]['otmr'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_wh_otmr(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['wholeHouse'][0]['otmr'] = [value]
    self.writeJson(jo)
    logging.info(str(value))

  # id: 0 = home, 1 = away, 2 = sleep, 3 = wake, 4 = manual
  def get_wh_activities(self,id):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['wholeHouse'][0]['activities'][0]['activity'][id]['blight'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  # id: 0 = home, 1 = away, 2 = sleep, 3 = wake, 4 = manual
  def set_wh_activities(self, id, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['wholeHouse'][0]['activities'][0]['activity'][id]['blight'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_wp_rhtg(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['windowprotect'][0]['rhtg'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_wp_rhtg(self, value):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jo['system'][0]['config'][0]['windowprotect'][0]['rhtg'] = [json.dumps(value)]
    self.writeJson(jo)
    logging.info(str(value))

  def get_wp_enabled(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['windowprotect'][0]['enabled'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_wp_enabled(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['windowprotect'][0]['enabled'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  def get_wp_ventprotect(self):
    c = self.loadJson(self.file)
    jo = json.loads(c)
    jd = json.dumps(jo['system'][0]['config'][0]['windowprotect'][0]['ventprotect'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def set_wp_ventprotect(self, value):
    if self.__is_on_or_off(value):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['windowprotect'][0]['ventprotect'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  # zone 0-7
  def get_zone_hold(self,zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['hold'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def set_zone_hold(self, zone, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_on_or_off(value):
        c = self.loadJson(self.file)
        jo = json.loads(c)
        jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['hold'] = [value]
        self.writeJson(jo)
        logging.info(str(value))

  # zone 0-7
  def get_zone_tempoffset(self,zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['tempoffset'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def set_zone_tempoffset(self, zone, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['tempoffset'] = [json.dumps(value)]
      self.writeJson(jo)
      logging.info(str(value))

  # zone 0-7
  def get_zone_holdActivity(self,zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['holdActivity'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def set_zone_holdActivity(self, zone, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['holdActivity'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  # zone 0-7
  def get_zone_name(self,zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['name'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def set_zone_name(self, zone, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['name'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  # zone 0-7
  def get_zone_setback(self,zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['setback'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def set_zone_setback(self, zone, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_on_or_off(value):
        c = self.loadJson(self.file)
        jo = json.loads(c)
        jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['setback'] = [value]
        self.writeJson(jo)
        logging.info(str(value))

  # zone 0-7
  def get_zone_airflowlimit(self,zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['airflowlimit'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def set_zone_airflowlimit(self, zone, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['airflowlimit'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  # zone 0-7
  def get_zone_otmr(self,zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['otmr'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def set_zone_otmr(self, zone, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['otmr'] = [value]
      self.writeJson(jo)
      logging.info(str(value))

  # zone 0-7
  def get_zone_enabled(self,zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['enabled'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def set_zone_enabled(self, zone, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_on_or_off(value):
        c = self.loadJson(self.file)
        jo = json.loads(c)
        jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['enabled'] = [value]
        self.writeJson(jo)
        logging.info(str(value))

  # zone 0-7
  def get_zone_cfmlimit(self, zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['cfmlimit'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def set_zone_cfmlimit(self, zone, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.file)
      jo = json.loads(c)
      jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['cfmlimit'] = [json.dumps(value)]
      self.writeJson(jo)
      logging.info(str(value))

  # zone 0-7, id: 0 = home, 1 = away, 2 = sleep, 3 = wake, 4 = manual
  def get_zone_activity_name(self, zone, id):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_int(id) and self.__is_in_range(id,0,4):
        c = self.loadJson(self.file)
        jo = json.loads(c)
        jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['activities'][0]['activity'][id]['id'])
        fv = jd.replace('["',"").replace('"]','')
        fv = jd.replace('"','').replace('"','')
        logging.debug(str(fv))
        return fv

  # zone 0-7, id: 0 = home, 1 = away, 2 = sleep, 3 = wake, 4 = manual
  def get_zone_activity_htsp(self, zone, id):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_int(id) and self.__is_in_range(id,0,4):
        c = self.loadJson(self.file)
        jo = json.loads(c)
        jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['activities'][0]['activity'][id]['htsp'])
        fv = jd.replace('["',"").replace('"]','')
        logging.debug(str(fv))
        return fv

  # zone 0-7, id: 0 = home, 1 = away, 2 = sleep, 3 = wake, 4 = manual
  def set_zone_activity_htsp(self, zone, id, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_int(id) and self.__is_in_range(id,0,4):
        if self.__is_float(value) and self.__is_in_range(value,0,100):
          c = self.loadJson(self.file)
          jo = json.loads(c)
          jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['activities'][0]['activity'][id]['htsp'] = [json.dumps(value)]
          self.writeJson(jo)
          logging.info("zone:"+str(zone)+" id:"+str(id)+" value:"+str(value))

  # zone 0-7, id: 0 = home, 1 = away, 2 = sleep, 3 = wake, 4 = manual
  def get_zone_activity_clsp(self, zone, id):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_int(id) and self.__is_in_range(id,0,4):
        c = self.loadJson(self.file)
        jo = json.loads(c)
        jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['activities'][0]['activity'][id]['clsp'])
        fv = jd.replace('["',"").replace('"]','')
        logging.debug(str(fv))
        return fv

  # zone 0-7, id: 0 = home, 1 = away, 2 = sleep, 3 = wake, 4 = manual
  def set_zone_activity_clsp(self, zone, id, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_int(id) and self.__is_in_range(id,0,4):
        if self.__is_float(value) and self.__is_in_range(value,0,100):
          c = self.loadJson(self.file)
          jo = json.loads(c)
          jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['activities'][0]['activity'][id]['clsp'] = [json.dumps(value)]
          self.writeJson(jo)
          logging.info("zone:"+str(zone)+" id:"+str(id)+" value:"+str(value))

  # zone 0-7, id: 0 = home, 1 = away, 2 = sleep, 3 = wake, 4 = manual
  def get_zone_activity_fan(self, zone, id):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_int(id) and self.__is_in_range(id,0,4):
        c = self.loadJson(self.file)
        jo = json.loads(c)
        jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['activities'][0]['activity'][id]['fan'])
        fv = jd.replace('["',"").replace('"]','')
        logging.debug(str(fv))
        return fv

  # zone 0-7, id: 0 = home, 1 = away, 2 = sleep, 3 = wake, 4 = manual
  def set_zone_activity_fan(self, zone, id, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_int(id) and self.__is_in_range(id,0,4):
        if self.__is_on_or_off(value):
          c = self.loadJson(self.file)
          jo = json.loads(c)
          jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['activities'][0]['activity'][id]['fan'] = [value]
          self.writeJson(jo)
          logging.info("zone:"+str(zone)+" id:"+str(id)+" value:"+str(value))

  # zone 0-7, day: 0-6 is Sunday-Saturday, period: 0-4
  def get_zone_program_day_period_enabled(self, zone, day, period):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_int(day) and self.__is_in_range(day,0,6):
        if self.__is_int(period) and self.__is_in_range(period,0,4):
          c = self.loadJson(self.file)
          jo = json.loads(c)
          jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['program'][0]['day'][day]['period'][period]['enabled'])
          fv = jd.replace('["',"").replace('"]','')
          logging.debug(str(fv))
          return fv

  # zone 0-7, day: 0-6 is Sunday-Saturday, period: 0-4
  def set_zone_program_day_period_enabled(self, zone, day, period, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_int(day) and self.__is_in_range(day,0,6):
        if self.__is_int(period) and self.__is_in_range(period,0,4):
          if self.__is_on_or_off(value):
            c = self.loadJson(self.file)
            jo = json.loads(c)
            jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['program'][0]['day'][day]['period'][period]['enabled'] = [value]
            self.writeJson(jo)
            logging.info(str(value))

  # zone 0-7, day: 0-6 is Sunday-Saturday, period: 0-4
  def get_zone_program_day_period_time(self, zone, day, period):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_int(day) and self.__is_in_range(day,0,6):
        if self.__is_int(period) and self.__is_in_range(period,0,4):
          c = self.loadJson(self.file)
          jo = json.loads(c)
          jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['program'][0]['day'][day]['period'][period]['time'])
          fv = jd.replace('["',"").replace('"]','')
          logging.debug(str(fv))
          return fv

  # zone 0-7, day: 0-6 is Sunday-Saturday, period: 0-4
  def set_zone_program_day_period_time(self, zone, day, period, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_int(day) and self.__is_in_range(day,0,6):
        if self.__is_int(period) and self.__is_in_range(period,0,4):
          if self.__is_valid_time(value):
            c = self.loadJson(self.file)
            jo = json.loads(c)
            jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['program'][0]['day'][day]['period'][period]['time'] = [value]
            self.writeJson(jo)
            logging.info(str(value))

  # zone 0-7, day: 0-6 is Sunday-Saturday, period: 0-4
  def get_zone_program_day_period_activity(self, zone, day, period):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_int(day) and self.__is_in_range(day,0,6):
        if self.__is_int(period) and self.__is_in_range(period,0,4):
          c = self.loadJson(self.file)
          jo = json.loads(c)
          jd = json.dumps(jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['program'][0]['day'][day]['period'][period]['activity'])
          fv = jd.replace('["',"").replace('"]','')
          logging.debug(str(fv))
          return fv

  # zone 0-7, day: 0-6 is Sunday-Saturday, period: 0-4
  def set_zone_program_day_period_activity(self, zone, day, period, value):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      if self.__is_int(day) and self.__is_in_range(day,0,6):
        if self.__is_int(period) and self.__is_in_range(period,0,4):
          if self.__is_valid_activity(value):
            c = self.loadJson(self.file)
            jo = json.loads(c)
            jo['system'][0]['config'][0]['zones'][0]['zone'][zone]['program'][0]['day'][day]['period'][period]['activity'] = [value]
            self.writeJson(jo)
            logging.info(str(value))

  def set_current_profile(self, until, profile):
    if self.__is_valid_activity(profile):
      if self.__is_valid_time(until):
        api_url='http://'+str(hvacIP)+':'+str(hvacPort)+'/api/1/hold?activity='+profile+'&until="'+until+'"'
        r = requests.get(api_url)
        if r.status_code == requests.codes.ok :
          logging.debug('setting '+profile+' until '+until)
          return True
        else:
          logging.error(r)
          return False

  def get_current_oat(self):
    c = self.loadJson(self.status)
    jo = json.loads(c)
    jd = json.dumps(jo['status'][0]['oat'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def get_current_filtrlvl(self):
    c = self.loadJson(self.status)
    jo = json.loads(c)
    jd = json.dumps(jo['status'][0]['filtrlvl'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def get_current_vacatrunning(self):
    c = self.loadJson(self.status)
    jo = json.loads(c)
    jd = json.dumps(jo['status'][0]['vacatrunning'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def get_current_mode(self):
    c = self.loadJson(self.status)
    jo = json.loads(c)
    jd = json.dumps(jo['status'][0]['mode'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def get_current_cfgem(self):
    c = self.loadJson(self.status)
    jo = json.loads(c)
    jd = json.dumps(jo['status'][0]['cfgem'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def get_current_uvlvl(self):
    c = self.loadJson(self.status)
    jo = json.loads(c)
    jd = json.dumps(jo['status'][0]['uvlvl'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def get_current_ventlvl(self):
    c = self.loadJson(self.status)
    jo = json.loads(c)
    jd = json.dumps(jo['status'][0]['ventlvl'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def get_current_cfgtype(self):
    c = self.loadJson(self.status)
    jo = json.loads(c)
    jd = json.dumps(jo['status'][0]['cfgtype'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def get_current_humlvl(self):
    c = self.loadJson(self.status)
    jo = json.loads(c)
    jd = json.dumps(jo['status'][0]['humlvl'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  def get_current_humid(self):
    c = self.loadJson(self.status)
    jo = json.loads(c)
    jd = json.dumps(jo['status'][0]['humid'])
    fv = jd.replace('["',"").replace('"]','')
    logging.debug(str(fv))
    return fv

  # zone 0-7
  def get_current_zone_currentActivity(self, zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.status)
      jo = json.loads(c)
      jd = json.dumps(jo['status'][0]['zones'][0]['zone'][zone]['currentActivity'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def get_current_zone_enabled(self, zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.status)
      jo = json.loads(c)
      jd = json.dumps(jo['status'][0]['zones'][0]['zone'][zone]['enabled'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv 

  # zone 0-7
  def get_current_zone_htsp(self, zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.status)
      jo = json.loads(c)
      jd = json.dumps(jo['status'][0]['zones'][0]['zone'][zone]['htsp'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def get_current_zone_otmr(self, zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.status)
      jo = json.loads(c)
      jd = json.dumps(jo['status'][0]['zones'][0]['zone'][zone]['otmr'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def get_current_zone_name(self, zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.status)
      jo = json.loads(c)
      jd = json.dumps(jo['status'][0]['zones'][0]['zone'][zone]['name'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def get_current_zone_hold(self, zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.status)
      jo = json.loads(c)
      jd = json.dumps(jo['status'][0]['zones'][0]['zone'][zone]['hold'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def get_current_zone_fan(self, zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.status)
      jo = json.loads(c)
      jd = json.dumps(jo['status'][0]['zones'][0]['zone'][zone]['fan'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def get_current_zone_rt(self, zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.status)
      jo = json.loads(c)
      jd = json.dumps(jo['status'][0]['zones'][0]['zone'][zone]['rt'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def get_current_zone_rh(self, zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.status)
      jo = json.loads(c)
      jd = json.dumps(jo['status'][0]['zones'][0]['zone'][zone]['rh'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

  # zone 0-7
  def get_current_zone_clsp(self, zone):
    if self.__is_int(zone) and self.__is_in_range(zone,0,7):
      c = self.loadJson(self.status)
      jo = json.loads(c)
      jd = json.dumps(jo['status'][0]['zones'][0]['zone'][zone]['clsp'])
      fv = jd.replace('["',"").replace('"]','')
      logging.debug(str(fv))
      return fv

