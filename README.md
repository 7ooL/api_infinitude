# pyInfinitude
python API to interact with Infinitude
https://github.com/nebulous/infinitude
Infinitude is an alternative web service for Carrier Infinity Touch and compatible thermostats.

WARNING: I dont know the expected input to many of the backend settings so I'm not able to guard against them with sanity checks in the functions. That said always use caution when submitting values as it could do harm. 

# Basic Overview
This class will have a getter and setter function for each value in the infinitude system configuation file.

Pulls json file from `http:{IP}:{PORT}/systems.json`    
and     
Publishes to `http:{IP}:{PORT}/systems/infinitude`    

# Purpose
I'm writing my own home automation program and tieing in the HVAC system is just one piece. I wasn't able to do all that i wanted using the current Infinitude API.     

# Example
Setting away profile to hold for 15 minutes into the future    
```python
zone=0
dt = datetime.datetime.now()    
newHold = dt.replace(minute=0, second=0) + datetime.timedelta(minutes=(dt.minute//15+1)*15)    `
hvac.pullConfig()     
hvac.set_zone_holdActivity(zone,'away')    
hvac.set_zone_otmr(zone,newHold.strftime("%H:%M"))     
hvac.set_zone_hold(zone,'on')    
hvac.pushConfig()
    
