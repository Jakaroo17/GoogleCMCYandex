from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


class GoogleDocs():
    # Файл, полученный в Google Developer Console
    CREDENTIALS_FILE = 'creds.json'
    # ID Google Sheets документа (можно взять из его URL)
    spreadsheet_id = '1daDN7zLsMCaJk-Y0XtOg4KSXwU55JM2QYVIh6uo8yEA'

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

    """Метод чтения из файла. sheet - нужная страница. StartRow - начала диапазона. EndRow - конец диапазона. Dimension - 
    мерность выдачи файла"""
    def get_data_from_sheets(self,sheet:str,StartRow:str,EndRow:str,Dimension:str = 'ROWS'):
        values = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=f"'{sheet}'!{StartRow}:{EndRow}",
            majorDimension=f'{Dimension}'
        ).execute()
        return values

    def write_to_sheet(self,sheet:str,StartRow:str,EndRow:str,parameters,Dimension:str = 'ROWS'):
        values = self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": f"'{sheet}'!{StartRow}:{EndRow}",
                    "majorDimension": f"{Dimension}",
                    "values": [parameters]}
            ]
            }
        ).execute()
    
    """Метод поиска в какой ячейке находится необходимая информация по строкам
    sheet - страница, startletter - начальная буква,
    endletter - конечная буква. 
    element - искомый элемент"""
    def find_by_row(self,sheet:str,startletter:str,endletter:str,element:str):
        pass

    """Метод поиска в какой ячейке находится необходимая информация по столбцам
    sheet - страница, startnumber - начальное число,
    endnumber - конечное число.
    letter - в каком столбце будет поиск 
    element - искомый элемент"""
    def find_by_column(self,sheet:str,letter:str,startnumber:int,endnumber:int,element:str):
        i = startnumber
        while i != endnumber:
            values = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=f"'{sheet}'!{letter}{i}:{letter}{i}",
                majorDimension=f'COLUMNS'
            ).execute()
            try:
                print(values['values'][0][0],element,values['values'][0][0] == element)
                if values['values'][0][0] == element:
                    return f'{letter}{i}'     
            except Exception as e:
                print(e)
            i+=1
        return None

# testgoogledocs = GoogleDocs()
# print(testgoogledocs.FindByColumn('Накопления','B',50,'126,29'))
