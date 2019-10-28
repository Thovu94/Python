import pycurl
import xml.etree.ElementTree as bus
import webbrowser
from StringIO import StringIO

def getOCData(stopNo, routeNo):
	c = pycurl.Curl()
	c.setopt(pycurl.POST, True )
	c.setopt(pycurl.POSTFIELDS,'appID=3875e418&apiKey=ea5f5d83fd97bc2d2b311c745cf3585b&stopNo='+stopNo+'&routeNo='+routeNo+'&format=xml')
	c.setopt(pycurl.URL, 'https://api.octranspo1.com/v1.2/GetNextTripsForStop')
	c.setopt(pycurl.SSL_VERIFYHOST,0)
	c.setopt(pycurl.SSL_VERIFYPEER,0)
	buffer = StringIO()
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	return buffer


def doIt():
	stopNo = str(input("Enter the stop number: "))
	routeNo = str(input("Enter the route number: "))
	lst = []
	doc = bus.fromstring(getOCData(stopNo, routeNo).getvalue().decode('utf-8'))     # Your shortened XML document
   
	for b in doc.findall('.//{http://tempuri.org/}Trip'):
		lat = b.findtext('{http://tempuri.org/}Latitude')
		lon = b.findtext('{http://tempuri.org/}Longitude')
		start = b.findtext('{http://tempuri.org/}TripStartTime')
		print tuple((lat,lon,start))
		lst .append(tuple((lat,lon,start)))
	for l in lst:
		print l[0],l[1],l[2]
		url="https://www.google.ca/maps/place//@"+l[0]+","+l[1]+",16z/data=!3m1!4b1!4m2!3m1!1s0x0:0x0"
		webbrowser.open(url,new=0,autoraise=True)


if __name__ == '__main__':
    doIt()
