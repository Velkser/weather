from webbrowser import get
import eel
from pyowm.owm import OWM

owm = OWM("170be48aec5fb765f762fe41ef379013")

@eel.expose
def get_weather(city):
   
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)   
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    return "В городе " + city + " сейчас " + str(temp) + " градусов"
    #print("В городе " + city + " сейчас " + str(temp) + " градусов")
    
eel.init("web")
eel.start("main.html", size=(700, 700)) 