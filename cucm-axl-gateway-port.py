from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.exceptions import Fault
from zeep.plugins import HistoryPlugin
from zeep.helpers import serialize_object
from requests import Session
from requests.auth import HTTPBasicAuth
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from lxml import etree
import getpass

disable_warnings(InsecureRequestWarning)

print()
username = input('CUCM username: ')
password = getpass.getpass('CUCM password: ')
user_input_MAC = input('Analog Port MAC: ')
print()

host = '<your CUCM pub FQDN>'

wsdl = 'file://C:/Users/<path to your>/AXL/12.5/axlsqltoolkit/schema/12.5/AXLAPI.wsdl'
location = 'https://{host}:8443/axl/'.format(host=host)
binding = "{http://www.cisco.com/AXLAPIService/}AXLAPIBinding"

session = Session()
session.verify = False
session.auth = HTTPBasicAuth(username, password)

transport = Transport(cache=SqliteCache(), session=session, timeout=20)
history = HistoryPlugin()
client = Client(wsdl=wsdl, transport=transport, plugins=[history])
service = client.create_service(binding, location)

def show_history():
    for item in [history.last_sent, history.last_received]:
        print(etree.tostring(item["envelope"], encoding="unicode", pretty_print=True))

gateway_device_name = 'SKIGW' + user_input_MAC[0:10]
gateway_slot = int(int(user_input_MAC[10])/2)
gateway_port = int(user_input_MAC[11:],16)
voice_port = str(gateway_slot) + '/0/' + str(gateway_port)

try:
    resp = service.listGateway(searchCriteria={'domainName': gateway_device_name},returnedTags={'description':''})
    #print(resp)
except Fault:
    show_history()

my_list = resp['return'].gateway
for gateway in my_list:
    print(gateway.description, voice_port)
    print()
