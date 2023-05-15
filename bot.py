import os
import telebot
import requests


api_key = os.environ['TELEGRAM_TOKEN']
chat_id = os.environ['TELEGRAM_CHAT_ID']
auth_token = os.environ['WETRACK_AUTH_TOKEN']
bot = telebot.TeleBot(api_key)


def test_request():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(auth_token)
    }
    response = requests.get('https://wetrack.advantest.com/rest/api/2/search?jql=assignee%20%3D%20currentUser()%20AND%20resolution%20%3D%20Unresolved%20order%20by%20updated%20DESC',
                            headers=headers)
    response_dict = response.json()
    message = "*****Your Open Issues*****\n\n"
    for issue in response_dict['issues']:
        issue_key = issue['key']
        summary = issue['fields']['summary']
        url = "https://wetrack.advantest.com/browse/{}".format(issue_key)
        message += f"{issue_key : <10} {summary : ^10} {url : >10}\n\n"
    return message

bot.send_message(chat_id, test_request())