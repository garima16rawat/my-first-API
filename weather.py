#from wsgiref.util import request_uri
import requests
API_KEY="9a3e61b241a670999308ba3189164005"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"
city=input("enter a city name :")
request_url=f"{BASE_URL}?appid={API_KEY}&q={city}"
responce=requests.get(request_url)
if responce.status_code==200:
    data=responce.json()
    weather=data['weather'][0]['description']
    print("weather :", weather)
    tempreture=round(data['main']['temp']-273.59)
    print(f"temprature is : {tempreture}in celsius")
    
else:
    print("An error occoured")
    
