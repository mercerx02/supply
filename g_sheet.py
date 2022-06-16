from pprint import pprint

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
import requests


CREDENTIALS_FILE = 'creds.json'

spreadsheet_id = '1z_-ELTTMfosN1HQ68PLd0dTdcG7yrve3_CvIhkuhjcc'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])


httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:D1000',
    majorDimension='ROWS'
).execute()


class Supply:
    def __init__(self,id,order_number,price_usd,price_rub,date_supply):
        self.id = id
        self.order_number = order_number
        self.price_usd = price_usd
        self.price_rub = price_rub
        self.date_supply = date_supply


data2 = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

dollar = float(data2['Valute']['USD']['Value'])

data = []


for value in values["values"][1:]:
    data.append(Supply(value[0],value[1],int(value[2]),int(value[2])*dollar,value[3]))


