import requests

api_address = 'http://api.openweathermap.org/data/2.5/forecast?&APPID=d83e284da19e7091b2bc27b9a220071e'
idOfCity = input('Please Enter the Id of city :')
ourUrl = api_address + idOfCity
Our_json_data = requests.get(ourUrl).json()
Our_final_add = Our_json_data['base']
print(Our_final_add)
