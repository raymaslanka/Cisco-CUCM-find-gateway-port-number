# Cisco-CUCM-find-gateway-port-number
Cisco Analog Gateway Port Number Finder

This is a small sample of how to retrieve a CUCM analog gateway description and voice-port number given the MAC address of the analog phone.

Handy for crossconencting in the field, this eliminates the need to manually find the gateway after modifying the MAC address and then convert the MAC to a physical port. 

There is little error handling and no input verification here. This is just a sample of the associated AXL API usage.

Much of this is boiler plate courtesy of https://paultursan.com/2016/04/getting-started-with-python-cucm-axl-api-programming/

Tested in Python 3.6.2 against CUCM 12.5.
