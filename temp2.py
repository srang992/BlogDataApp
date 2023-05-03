from oauth2client.service_account import ServiceAccountCredentials
import gspread
from pprint import pprint

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scopes=scope)
client = gspread.authorize(creds)

# [{'createdTime': '2023-04-22T15:56:35.653Z',
#   'id': '1bBPh5rv3HRpUFngkyqIqH3P8gbP1nnZQMy7PK9wxnro',
#   'modifiedTime': '2023-04-22T16:00:44.176Z',
#   'name': 'My Blogs List'},
#  {'createdTime': '2023-04-22T15:52:42.574Z',
#   'id': '1qad1XMoNOuuPVNYpeny6FYfsBxHqY-TuD9z9rfa1JXE',
#   'modifiedTime': '2023-04-22T15:52:45.830Z',
#   'name': 'My Blogs List'},
#  {'createdTime': '2023-04-22T15:46:58.074Z',
#   'id': '1sNgzA5SL9v32s4xo6qgYqJDcM8k7Yi4f27990Cb9WZQ',
#   'modifiedTime': '2023-04-22T15:46:58.085Z',
#   'name': 'My Blogs List'}]

sheet = client.create("My Articles")
sheet.share("subhradeeprang40@gmail.com", perm_type="user", role="writer")

# client.del_spreadsheet(file_id='1N9__rbZpt1IyOsuWhMTZ8rcM1zqjO1AsxkkbUe1nu6E')
# pprint(client.list_spreadsheet_files())
