import os.path
import datetime
import schedule
import time
from googleapiclient.discovery import build
from google.oauth2 import service_account
from pars import arr


def main():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'credentials.json')

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SAMPLE_SPREADSHEET_ID = '1vZTFIwD-3QFbdNNxROXqNWJMXSScKzOzslx0SjrIfJA'
    SAMPLE_RANGE_NAME = 'Sheet1'

    service = build('sheets', 'v4', credentials=credentials).spreadsheets().values()

    result = service.get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                         range=SAMPLE_RANGE_NAME).execute()

    data_from_sheet = result.get('values', [])
    print(data_from_sheet)
    d = datetime.date.today()
    i = (d.day - 19) + 30 * (d.month - 12) + 365 * (d.year - 2022)  # для подсчета ячейи по дням
    range_ = f'Sheet1!A{i}'
    value_input_option = 'USER_ENTERED'
    value_range_body = {'values': [arr]}
    response = service.update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range_,
                              valueInputOption=value_input_option,
                              body=value_range_body).execute()


main()  # простой запуск программы


# schedule.every().day.at("01:00").do(main, 'It is 01:00') # если раскоментировать то логи будут
# записываться в час ночи каждый день
# while True:
#     schedule.run_pending()
#     time.sleep(60)
