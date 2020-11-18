import sys
import datetime
import requests
import json
import re
import os


# Translations to Dutch
DAY_NAMES = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
MONTH_NAMES = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]


class TrelloApi:
	def __init__(self):
		self.baseUrl = "https://api.trello.com/1"
		self.config = {}


	def initConfig(self):
		try:
			with open(os.getcwd()+'/_config.txt', 'r') as f:
				data = f.read()
		except:
			print(f"Config '{os.getcwd()+'/_config.txt'}' could not be opened")
			sys.exit()

		print("Config read successful\n")
		data = data.split("\n")
		for i in range(len(data)):
			data[i] = data[i].split("=")
			self.config[data[i][0]] = data[i][1]


	def readCardFile(self):
		contents = [{}]

		try:
			with open(self.config.get('contentFilePath')) as f:
				data = f.read()
		except:
			print(f"File '{self.config.get('contentFilePath')}' could not be opened")
			sys.exit()

		data = data.split("\n")
		for i in range(len(data)):
			if data[i] == '&&':
				contents.append({})
				continue

			data[i] = data[i].split("=")

			if data[i][0] == 'LIST_NAME':
				contents[len(contents)-1]['idList'] = self.getListIdByName(data[i][1])
				continue

			contents[len(contents)-1][data[i][0]] = data[i][1]

		print("CardFile read successful\n")
		return contents


	def Api(self, url, params={}, method="GET"):
		res = requests.request(
			method,
			self.baseUrl+url+f"?key={self.config.get('KEY')}&token={self.config.get('TOKEN')}",
			params=params
		)

		if res.status_code not 200:
			print(f"Api error:\n{res.status_code}\n{self.baseUrl+url}")
			sys.exit()

		return res


	def getListIdByName(self, name):
		lists = self.Api(f"/boards/{self.config.get('boardId')}/lists")
		json = lists.json()
		listId = None

		for i in range(len(json)):
			print(f"Checking list: '{json[i].get('name')}'")
			if name == 'DEFAULT_TODAY':
				date = getToday()
				if re.search(f"{date[0][:2]}({date[0][2:]})?(.*)?{date[1]}(.*)?({date[2][:3]}({date[2][3:]})?|{date[3]})", json[i].get('name'), flags=re.IGNORECASE):
					listName = json[i].get('name')
					listId = json[i].get('id')
					break
			if re.search(name, json[i].get('name'), flags=re.IGNORECASE):
				listName = json[i].get('name')
				listId = json[i].get('id')
				break

		try:
			print(f"\nMatch found with '{listName}'\n- - - - - - - - - - - - - - - - - - -")
		except:
			print(f"\nNo match found for: '{name}'\n- - - - - - - - - - - - - - - - - - - -")
			sys.exit()

		return listId


	def createCardByList(self, content):
		for i in range(len(content)):
			self.Api("/cards", content[i], "POST")
			print(f"Card created successfully with content:\n{content[i]}\n")


def getToday():
		# ('maandag', 1, 'januari', 1)
		today = datetime.date.today()
		return (DAY_NAMES[today.weekday()], today.day, MONTH_NAMES[today.month-1], today.month)


def main():
	t = TrelloApi()
	t.initConfig()
	content = t.readCardFile()
	t.createCardByList(content)


if __name__ == '__main__':
	main()