
import requests
import time
import json


hook = ''



def check():
    url = "https://www.cvs.com/Services/ICEAGPV1/immunization/1.0.0/getIMZStores"
    zip_code = ""
    payload =  "{\"requestMetaData\":{\"appName\":\"CVS_WEB\",\"lineOfBusiness\":\"RETAIL\",\"channelName\":\"WEB\",\"deviceType\":\"DESKTOP\",\"deviceToken\":\"7777\",\"apiKey\":\"a2ff75c6-2da7-4299-929d-d670d827ab4a\",\"source\":\"ICE_WEB\",\"securityType\":\"apiKey\",\"responseFormat\":\"JSON\",\"type\":\"cn-dep\"},\"requestPayloadData\":{\"selectedImmunization\":[\"CVD\"],\"distanceInMiles\":35,\"imzData\":[{\"imzType\":\"CVD\",\"ndc\":[\"59267100002\",\"59267100003\",\"59676058015\",\"80777027399\"],\"allocationType\":\"1\"}],\"searchCriteria\":{\"addressLine\":\""+zip_code+"\"}}}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'Origin': 'https://www.cvs.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.cvs.com/vaccine/intake/store/cvd-store-select/first-dose-select',
        'TE': 'Trailers'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    jsons = json.loads(response.text)
    return jsons['responseMetaData']['statusCode']


res = check()
print(res)
params = {
    'username': "vaci",
    'content': "Vaccine in Stock \n https://www.cvs.com/immunizations/covid-19-vaccine"
}
while True:
    res = check()
    if res == "1010":
        time.sleep(60)
    else:
        requests.post(hook, params)
        time.sleep(60)






