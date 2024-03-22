import urllib.request
import urllib.error
url = "http://esb.gvt.net.br:8888/ResourceManagement/WorkforceManagement/WorkforceManagementReporting/WorkOrderReporting?WSDL"
 
try:
   response = urllib.request.urlopen(url)
   print(response.read())
except urllib.error.URLError as e:
     print(f"Erro na requisção: {e}")