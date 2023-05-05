from oauth2client.service_account import ServiceAccountCredentials
import gspread
import re
import feedparser
from bs4 import BeautifulSoup

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scopes=scope)
client = gspread.authorize(creds)

sheet = client.open('My Articles').sheet1

feed1 = feedparser.parse("https://medium.com/feed/@srang992")
feed2 = feedparser.parse("https://www.analyticsvidhya.com/blog/author/subhradeep06/feed/")


sheet.clear()
sheet.append_row(['Title', 'Link', 'Author', 'Publication Date', "Description"])

for entry in feed1.entries:
    soup = BeautifulSoup(entry.description, "html.parser")
    sheet.append_row([entry.title, entry.link, entry.author, entry.published, soup.text])


for entry in feed2.entries:
    soup = BeautifulSoup(entry.description, "html.parser")
    text = re.sub(r'[^a-zA-Z .,]', "", soup.text)
    sheet.append_row([entry.title, entry.link, entry.author, entry.published, soup.text])

print("Data Updated Successfully!")