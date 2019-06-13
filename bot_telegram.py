import requests
import telegram
import datetime


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=60):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def force_reply(self, force_reply=True):
        params={'force_reply':force_reply}
        method='ForceReply'
        resp=requests.post(self.api_url+method, params)
        # print(resp)
        return resp

    def send_message(self, chat_id, text, bool=False):
        print(self.force_reply(bool))
        params = {'chat_id': chat_id, 'text': text, 'reply_markup':self.force_reply(bool)}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_message(self, data):
        message_text = data['message']['text']
        return message_text

    def send_chat_action(self, chat_id, action):
        params={'chat_id':chat_id, 'action':action}
        method='sendChatAction'
        resp=requests.post(self.api_url+method, params)
        return resp

    # def remove_keyboard_markup(self)
    #     params={''}
    

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update
