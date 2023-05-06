import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scopes=scope)
client = gspread.authorize(creds)

sheet = client.open("My Articles").sheet1

data = sheet.get_all_records()
df = pd.DataFrame(data, columns=data[0])
df.to_csv("BlogData.csv", index=False)
print("Data Updated Successfully!")

# data = pd.read_csv("BlogData.csv")
# print(data.head())
