
import pyInfinitude

ip = '192.168.1.248'
port = '3000'
file = 'infinitude.json'

hvac = pyInfinitude.infinitude(ip,port,file)

# get the current system configuations
hvac.pullConfig()

# get the back light setting
hvac.get_blight()

# test for integer validating
hvac.set_blight(60)
hvac.set_blight(-1)
hvac.set_blight(1.1)
hvac.set_blight("fgfjg")

# test for on off validating
hvac.set_cfghumid("off")
hvac.set_cfghumid("fhfjg")
hvac.set_cfghumid(13)
hvac.set_cfghumid("on")

# set zone(0)'s sleep(2) heat temp to 68
hvac.set_zone_activity_htsp(0,2,68)

# set zone(0)'s sleep(2) cool temp to 73
hvac.set_zone_activity_clsp(0,2,73)

# get saturdays wake profile time for zone 1
hvac.get_zone_program_day_period_time(0, 6, 0)

# test for time validating
hvac.set_zone_program_day_period_time(0, 6, 0, "25:00")
hvac.set_zone_program_day_period_time(0, 6, 0, "25:0")
hvac.set_zone_program_day_period_time(0, 6, 0, "14:00:45")
hvac.set_zone_program_day_period_time(8, 6, 0, "14:00")
hvac.set_zone_program_day_period_time(0, 7, 0, "14:00")
hvac.set_zone_program_day_period_time(0, 6, 5, "14:00")
hvac.set_zone_program_day_period_time(0, 6, 0, "14:00")

# save the changes made by setters, by pushing new configuation file
#hvac.pushConfig()


