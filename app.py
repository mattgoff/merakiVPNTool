import requests
import os

def doHtpCall(url):
    payload={}

    merakiKey = os.getenv('MERAKI_KEY')

    headers = {
    'Accept': 'application/json',
    'X-Cisco-Meraki-API-Key': merakiKey
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    jsonData = response.json()
    return jsonData

def getSiteNumber(sitename, allsitesjson):
    for site in allsitesjson:
        if (sitename in site['name']):
            # print(site['name'] + " " + site['id'])
            return site['id']
    return "Not Found"

def getVPNSettings(siteNumber):
    pass

siteName = input("Enter the site name: ")
siteUpper = siteName.upper()

allSitesJson = doHtpCall("https://api.meraki.com/api/v1/organizations/706810/networks")
siteNumberThatWeWant = getSiteNumber(siteUpper, allSitesJson)

# print("Found: {} with an ID of: {}".format(siteUpper, siteNumberThatWeWant))
# print("Found: " + siteUpper + " with an ID of: " + siteNumberThatWeWant)
# print(f'Found: {siteUpper} with an ID of: {siteNumberThatWeWant}')

if siteNumberThatWeWant != "Not Found":
    siteToSiteVPNInfo = doHtpCall(f"https://api.meraki.com/api/v1/networks/{siteNumberThatWeWant}/appliance/vpn/siteToSiteVpn")
    for asdf in siteToSiteVPNInfo['subnets']:
        print(asdf['localSubnet'])
else:
    print(f"Name Not Found: {siteName}")

