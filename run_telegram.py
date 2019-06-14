from insent_ai.bot_telegram import BotHandler
import datetime, json, time
import telegram

token = "833734852:AAHUHDH5KVvNovdxEYxoEBJ2JLkmbHKxswg"

greet_bot = BotHandler(token)
now = datetime.datetime.now()

def read_intents(intents_filename):
	with open(intents_filename, encoding='utf-8') as intents_file:
		intents=json.loads(intents_file.read())
	return intents

# def check_input_validty(input_type):
#   if input_type=="email":


def input_ouptput(intents, key="convo_end"):

	bot_reply=intents[key]['bot']
	option_answer=intents[key]['answers']

	new_offset = None

	latest_update=greet_bot.get_updates(new_offset)

	last_update = greet_bot.get_last_update()
	last_update_id = last_update['update_id']
	last_chat_text = last_update['message']['text']
	last_chat_id = last_update['message']['chat']['id']
	last_chat_name = last_update['message']['chat']['first_name']

	for i in range(len(bot_reply)):
		if (bot_reply[i].startswith("-Input-")):
			input_type=bot_reply[i].split("-")[-1]
			if input_type=="email":
				greet_bot.send_message(last_chat_id, 'Email_Id: ', 'True')

			elif input_type=="company":
				greet_bot.send_message(last_chat_id, 'Company Name: ', 'True')
				
			else:
				greet_bot.send_message(last_chat_id, 'Enter your reply here: ')

		else:
			greet_bot.send_message(last_chat_id, '{}'.format(bot_reply[i]))


		greet_bot.send_chat_action(last_chat_id, 'typing')
	
	custom_keyboard=[]
	for i in range(len(option_answer)):
		try:
			greet_bot.send_message(last_chat_id, str(i+1)+" "+option_answer[i]['answer'])
			custom_keyboard = custom_keyboard.append([option_answer[i]])
			answer_flag=1
		except:
			answer_flag=0
			pass


	nextKey=None

	if answer_flag==1:
		reply_markup=greet_bot.custom_keyboard(last_chat_id, custom_keyboard, 'testing')

		greet_bot.send_message(chat_id=chat_id, 
                 text=text, 
                 reply_markup=reply_markup)

		greet_bot.send_message(last_chat_id, "Type your option number")
		# option_input=greet_bot.get_message(last_update)
		# option_input=greet_bot.send_message(last_chat_id, "")

		print(option_input)
		option_number=int(option_input)-1
		nextKey=(option_answer[option_number]['nextId'])
	
	else:
		nextKey=(option_answer[0]['nextId'])
	input_ouptput(intents, nextKey)


def main():
	
	intents_filename="insent_ai/intents.json"
	default_key="welcome"
	
	new_offset=None
	while True:
		greet_bot.get_updates(new_offset)
		last_update = greet_bot.get_last_update()
		

		last_update_id = last_update['update_id']
		last_chat_text = last_update['message']['text']
		last_chat_id = last_update['message']['chat']['id']
		last_chat_name = last_update['message']['chat']['first_name']

		intents=read_intents(intents_filename)
		input_ouptput(intents, default_key)

		new_offset = last_update_id + 1

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
