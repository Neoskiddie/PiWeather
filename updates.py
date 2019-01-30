from sense_hat import SenseHat
import time 
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
    auth = tweepy.OAuthHandler("password","password") #change that 
    auth.set_access_token("password-password","password") #change that
    return tweepy.API(auth)

def tweet(tempInt, humInt, presInt):
    temp = str(tempInt) + "C "
    humidity = str(humInt) + "% "
    pressure = str(presInt) + "mbar "

    api = get_api()
    
    localtime = time.asctime( time.localtime(time.time()) ) #tweets that are same as previous get blocked - adding time prevents that
    tweet =  "Local current time :" + localtime + "\n\n" + "The measurements from the room: \n\n Temperature: " + temp + " - " 
    #advice
    if tempInt < 18:
        tweet += "to low temperature."
    elif tempInt == 21:
        tweet += "ideal temperature."
    elif tempInt < 24:
        tweet += "good room temperature."
    else:
        tweet += "to hot stop heating."

    tweet +=  "\n\nPressure: " + pressure +" - " 
    if presInt < 965:
        tweet += "it is stormy."
    elif presInt < 980:
        tweet += "it is raining."
    elif presInt < 1005:
        tweet += "weather is changing."
    elif presInt < 1030:
        tweet += "fair."
    else:
        tweet += "very dry."

    tweet += "\n\nHumidity is: " + humidity + " - " 
    if humInt < 30:
        tweet += "to dry."
    elif humInt < 50:
        tweet += "ideal humidity."
    else: 
        tweet += "to humid."

    status = api.update_status(status=tweet)



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
    tweet(tempInt,humInt,presInt)
    sense.set_pixels(logo) #sets the screen of Sense Hat to my logo
    
if __name__ == '__main__':
    Thread(target = getWeather).start()
    # you should use cron job to run this script, but instead you can uncomment following lines:
#    while True:
#        time.sleep(1800) #time in seconds until next update
#        Thread(target = getWeather).start()
