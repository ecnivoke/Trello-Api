# Trello Api
 Api for creating cards in Trello

Config:
	KEY, 				is your public KEY from Trello
	TOKEN, 				is your private TOKEN from Trello
	contentFilePath, 	is your full path to your card content example: C:\Users\{user}\OneDrive\Bureaublad\trellocard.txt
	boardId, 			is the ID of the board. You can easily find to by going to your board url and extend it with .json

	All these config variables are REQUIRED
	Don't move _config.txt from the same directory as main.py


Card:
	Use Query parameters from the Trello documentation (https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post)
	LIST_NAME, name of the list to search for in the board
		use DEFAULT_TODAY to search for todays date (D|l-d-M|m)
	&&, used to create a seperate card

	See example.txt

Batch:
	I recommend making a run.bat and running that instead of the .py file.
	That way the console stays open and you can actually read what the script is doing
