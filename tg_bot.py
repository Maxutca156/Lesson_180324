import pprint
import requests

token = '6623809896:AAEzuCEjCUQfcLlUjnIe_XGvDV-03NkdHoQ'
main_url = f'https://api.telegram.org/bot{token}'
#url = f'{main_url}/getMe'

# = requests.get(url)
#print(result.json())

url = f'{main_url}/getUpdates'
result = requests.get(url)
pprint.pprint(result.json())

messages = result.json()['result']
for message in messages:
    chat_id = message['message']['chat']['id']
    url = f'{main_url}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': 'Привет дорогой пользователь!'
    }
    result = requests.post(url, params = params)
