
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

# Authorize the clientsheet 
client = gspread.authorize(creds)

# Get the instance of the Spreadsheet
spreadsheet = client.open('Games_2022')

# Get the first sheet of the Spreadsheet
games_2022 = spreadsheet.worksheet('games_2022')
test = spreadsheet.worksheet('testing')

# Update a cell
test.update_acell('A1', '1')

# Get the value of a cell
val = test.acell('B1').value
print(val)