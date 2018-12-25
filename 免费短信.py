# -*- condig: utf-8 -*-
__author__ = 'bobby 作者'
__date__ = '2018/12/22 下午8:20'


import requests
import time
from bs4 import BeautifulSoup

from twilio.rest import Client


def text():

	message = []
	response = requests.get("https://www.tianqi.com/shantou/")
	html = response.text

	body = BeautifulSoup(html, 'lxml')
	# 日期
	date = time.strftime('%Y年%m月%d日', time.localtime(time.time()))
	message.append(date)

	name = body.select('.name h2')
	# 地区名
	for name in name:
		message.append(name.get_text())

	# 天气状况
	for wendu in body.select('.weather span'):
		message.append(wendu.get_text())

	# 空气
	kongqi = body.select('.kongqi h5')
	for name in kongqi:
		message.append(name.get_text())

	body = ""
	for text in message:
		body = body + text + "\n"

	return body

# time.sleep(3)
# print(time.strftime('%Y年%m月%d日', time.localtime(time.time())))
# onedata = 60*60*24
# print(time.strftime('%Y.%m.%d', time.localtime(time.time()-onedata)))
# print("Hello")


# text = text()
# print(text)


account_sid = "ACf63c8345f9212b2d15077e8c4a802426"
# Your Auth Token from twilio.com/console
auth_token = "47b8571e03fb408baa522f7dd495d6a8"
client = Client(account_sid, auth_token)
message = client.messages.create(
	from_="+12247650007",
	body=text(),
	to="+8613211232124",
)
print(message.sid)
