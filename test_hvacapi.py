
import pyInfinitude

ip = '192.168.1.20'
port = '5000'
jsonFile = 'infinitude.json'
statusFile = 'status'

hvac = pyInfinitude.infinitude(ip,port,jsonFile,statusFile)

# get the current system configuations
hvac.pull_config()

# get mode
print (hvac.get_mode())
print (hvac.get_zone_program_day_period_activity(0, 0, 0))

for id in range(0,5):
  print (hvac.get_zone_activity_name(0, id))


#zone = 0
#for id in range(0,5):
#  profile = hvac.get_zone_activity_name(zone, id)
#  print ('id'+str(id)+', profile:'+profile)

#for day in range(0,6):
#  for period in range(0,5):
#    if hvac.get_zone_program_day_period_enabled(zone, day, period) == 'on':
#      print ('day'+str(day)+', period:'+str(period))



#print hvac.get_zone_activity_fan(0, 0)
#print hvac.get_zone_activity_clsp(0, 1)
# get the back light setting
#hvac.get_blight()

# test for integer validating
#hvac.set_blight(60)
#hvac.set_blight(-1)
#hvac.set_blight(1.1)
#hvac.set_blight("fgfjg")

# test for on off validating
#hvac.set_cfghumid("off")
#hvac.set_cfghumid("fhfjg")
#hvac.set_cfghumid(13)
#hvac.set_cfghumid("on")

# set zone(0)'s sleep(2) heat temp to 68
#hvac.set_zone_activity_htsp(0,2,68)

# set zone(0)'s sleep(2) cool temp to 73
#hvac.set_zone_activity_clsp(0,2,73)

# get saturdays wake profile time for zone 1
#hvac.get_zone_program_day_period_time(0, 6, 0)

# test for time validating
#hvac.set_zone_program_day_period_time(0, 6, 0, "25:00")
#hvac.set_zone_program_day_period_time(0, 6, 0, "25:0")
#hvac.set_zone_program_day_period_time(0, 6, 0, "14:00:45")
#hvac.set_zone_program_day_period_time(8, 6, 0, "14:00")
#hvac.set_zone_program_day_period_time(0, 7, 0, "14:00")
#hvac.set_zone_program_day_period_time(0, 6, 5, "14:00")
#hvac.set_zone_program_day_period_time(0, 6, 0, "14:00")

# save the changes made by setters, by pushing new configuation file
#hvac.push_config()


