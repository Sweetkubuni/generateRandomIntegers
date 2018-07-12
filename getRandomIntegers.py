import json
import urllib2

def getRandomizeArray(config, apiKey):
	json_params = json.dumps({"jsonrpc": "2.0","method": "generateIntegers","params": {"apiKey": apiKey, "n": config[0], "min": config[1], "max": config[2], "replacement": 'true' }, "id": 1})
	clen = len(json_params)
	req = urllib2.Request('https://api.random.org/json-rpc/1/invoke', json_params, {'Content-Type': 'application/json', 'Content-Length': clen})
	f = urllib2.urlopen(req)
	response = f.read()
	f.close()
	return response

def parseRandomJson( data ):
	resp = json.loads(data)
	return resp['result']['random']['data']

if __name__ == "__main__":
    print parseRandomJson(getRandomizeArray([10000, 1, 50], ""))
