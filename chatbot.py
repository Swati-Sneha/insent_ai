import time
import numpy as np
import sys, random
import json
import logging


def read_intents(intents_filename):
	with open(intents_filename, encoding='utf-8') as intents_file:
		intents=json.loads(intents_file.read())
	return intents

# def check_input_validty(input_type):
# 	if input_type=="email":


def input_ouptput(intents, key="convo_end"):

	bot_reply=intents[key]['bot']
	option_answer=intents[key]['answers']

	for i in range(len(bot_reply)):
		if (bot_reply[i].startswith("-Input-")):
			input_type=bot_reply[i].split("-")[-1]
			if input_type=="email":
				email_id=input("Email Id: ")
			elif input_type=="company":
				company=input("Company Name: ")
			else:
				reply=input("Reply: ")

		else:
			print("Insent Bot: ",bot_reply[i])

		[time.sleep(0),time.sleep(5)][i==len((bot_reply))-1]
	
	for i in range(len(option_answer)):
		try:
			print(str(i+1)+" "+option_answer[i]['answer'])
			answer_flag=1
		except:
			answer_flag=0
			pass

	nextKey=None

	if answer_flag==1:
		option_input=input("Type your option number ")
		option_number=int(option_input)-1
		nextKey=(option_answer[option_number]['nextId'])
	
	else:
		nextKey=(option_answer[0]['nextId'])
	input_ouptput(intents, nextKey)

def main():

	'''declaring constants'''
	intents_filename="intents.json"
	default_key="welcome"

	'''calling functions'''
	intents=read_intents(intents_filename)

	input_ouptput(intents, default_key)

	
if __name__ == '__main__': 
	main()	