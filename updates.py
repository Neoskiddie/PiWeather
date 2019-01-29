from sense_hat import SenseHat
from time import sleep
import tweepy
from threading import Thread
sense = SenseHat()

e = (0,0,0)
g = (0,255,0)
b = (0,0,255)

#my logo that is displayed when no updates are send 
logo = [
    e,g,g,g,g,g,g,e,
    g,e,e,e,g,e,e,g,
    g,e,e,e,g,e,e,g,
    g,e,g,g,g,g,g,e,
    g,e,e,e,g,e,e,g,
    g,e,e,e,g,e,e,g,
    e,g,g,g,g,g,g,e,
    e,e,e,e,e,e,e,e
    ]

#Twitter 
def get_api():
    auth = tweepy.OAuthHandler("password","password")
    auth.set_access_token("password","password")
    return tweepy.API(auth)

#Collecting informations 
def getWeather():
    
    tempInt = round(sense.get_temperature())
    humInt = round(sense.get_humidity())
    presInt = round(sense.get_pressure())

    sense.clear() #just clear the screen
    temp = str(tempInt) + "C "
    humidity = str(humInt) + "% "
    pressure = str(presInt) + "mbar "

    message = temp + humidity + pressure 

    sense.show_message(message, scroll_speed=0.1)
    #Tweet
    api = get_api()

    tweet = "The current measurements from the room: \n\n The temperature: " + temp + "\n advice: \n" 
    if tempInt < 18:
        tweet += "To low temperature - Start heating ASAP!\n"
    elif tempInt == 21:
        tweet += "Ideal temperature - Try to keep it this way :)\n"
    elif tempInt < 24:
        tweet += "Good room temperature\n"
    else:
        tweet += "To hot stop heating\n"

    tweet +=  "\n\nThe pressure: " + pressure +"\n means: \n" 
    if presInt < 965:
        tweet += "It is stormy "
    elif presInt < 980:
        tweet += "It is raining "
    elif presInt < 1005:
        tweet += " Weather is changing"
    elif presInt < 1030:
        tweet += "fair"
    else:
        tweet += "\n very dry"

    tweet += "\n\nThe humidity is: " + humidity + "\n which is:\n" 
    if humInt < 30:
        tweet += "to dry"
    elif humInt < 50:
        tweet += "ideal humidity"
    else: 
        tweet += "to humid"

    status = api.update_status(status=tweet)

    sense.set_pixels(logo) #sets the screen of Sense Hat to my logo
    
if __name__ == '__main__':
    Thread(target = getWeather).start()
    while True:
        sleep(1800)#time in seconds until next update
        Thread(target = getWeather).start()

