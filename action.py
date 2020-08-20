from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk import Tracker
import requests
import random
from rasa_core_sdk.executor import CollectingDispatcher


class ActionWeather(Action):
    def name(self):
        return "action_weather"
    
    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot('location')
     
       
        complete_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=eb31f2106de4654"
     
        response = requests.get(complete_url)

        data = response.json()
        
        x=data['main']
        temp = round(x['temp'] - 273.15, 2)
        place = data["name"]
        x = data['weather']
        desc = x[0]['main']

        weather_data = "It's {}*C currently in {}. The weather can be described as {}".format(temp, place, desc)
        dispatcher.utter_message(weather_data)

        return [SlotSet("location", city)]
		
		
