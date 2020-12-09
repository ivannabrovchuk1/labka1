import requests
import json
import logging
import time

logging.basicConfig(
	filename="server.log",
	filemode='a',
	level=logging.INFO,
	format='{levelname} {name} : {message}',
	style='{'
)
log=logging.getLogger(__name__)

def main(url):
	while True:
		try:
			r= requests.get(url)
			data=json.loads(r.content)
			logging.info("Server is avalible. Server time: %s", data['datetime'])
			logging.info("Requested page: %s", data['server_url'])
			logging.info("Server response contauns the following fields:")
			for key in data.keys():
				logging.info("Key: %s, Value: %s", key, data[key])
		except requests.exeptions.ConnectionError as e:
			logging.error("Unable to connect to the server" + str(e))
		time.sleep(60)
if __name__=='__main__':
	main("http://localhost:8000/health")
