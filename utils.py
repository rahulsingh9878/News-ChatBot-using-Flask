from wit import Wit
from gnewsclient import gnewsclient

# Enter your Wit.ai Access Token
access_token = " ************************ "
client = Wit(access_token = access_token)

def wit_response(message_text):
	resp = client.message(message_text)
	categories = {'newstype':None, 'loction':None}

	entities = list(resp['entities'])
	for entity in entities:
		categories[entity] = resp['entities'][entity][0]['value']

	return categories

def get_news_elements(categories):
	news_client = gnewsclient()
	news_client.query = ''
	if categories['newstype'] != None:
		news_client.query += categories['newstype'] + ' '

	if categories['location'] != None:
		news_client.query += categories['location']

	news_items = news_client.get_news()

	elements = []

	for item in news_items:
		element = {
					'title': item['title'],
					'buttons': [{
								'type': 'web_url',
								'title': "Read More",
								'url': item['link']
					}],
					'image_url': item['img']
		}
		elements.append(element)


	return elements
