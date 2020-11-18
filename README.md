# Trello Api
 Api for creating cards in Trello

## Config:
<ul>
	<li>KEY <small>your public KEY from Trello</small></li>
	<li>TOKEN <small>your private TOKEN from Trello</small></li>
	<li>contentFilePath <small>your full path to your card content example: C:\Users\{user}\OneDrive\Bureaublad\trellocard.txt</small></li>
	<li>boardId <small>the ID of the board. You can easily find to by going to your board url and extend it with .json</small></li>
</ul>

	All these config variables are REQUIRED
	Don't move _config.txt from the same directory as main.py


## Card:
<ul>
	<li>Use Query parameters from the Trello documentation <small>(https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post)</small></li>
	<li>LIST_NAME <small>name of the list to search for in the board</small><ul><li>DEFAULT_TODAY <small>search for todays date (D|l-d-M|m)</small></li></ul></li>
	<li>&& <small>used to create a another card</small></li>
</ul>

	See example.txt

## Batch:
```
	I recommend making a run.bat and running that instead of the .py file.
	That way the console stays open and you can actually read what the script is doing
```