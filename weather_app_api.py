import requests
api_key = ('98a6767150dd85b5052b718a2afaf300')
user_input= input("\nEnter the City")
print(user_input)


weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}")

print(weather_data.json())
weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']
if(weather_data.json()['cod']=='404'):
    print("City does not exsist\n")
else:
    print(f"The weather in {user_input} is {weather}\n")
    print(f"The temperature in {user_input} is {temp}\n")

