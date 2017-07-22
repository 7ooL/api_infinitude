# pyInfinitude
python API to interact with Infinitude
https://github.com/nebulous/infinitude
Infinitude is an alternative web service for Carrier Infinity Touch and compatible thermostats.

# Basic Overview
This class will have a getter and setter function for each value in the infinitude system configuation file.

Pulls json file from `http:{IP}:{PORT}/systems.json`    
and     
Publishes to `http:{IP}:{PORT}/systems/infinitude`    

# Purpose
I'm writing my own home automation program and tieing in the HVAC system is just one part. I wasn't able to do all that i wanted using the current Infinitude API. 
