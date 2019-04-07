import json
import urllib.request as req

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


class owd:
    
    def getCurrentData(self):
        
        uri="http://api.openweathermap.org/data/2.5/weather?q="+self.location+"&APPID="+self.apikey+"&lang="+self.lang
        response = req.urlopen(uri)
        self.data = json.loads (response.read())
        return self.data

    def getForecastData(self):
        
        uri="http://api.openweathermap.org/data/2.5/forecast?q="+self.location+"&APPID="+self.apikey+"&lang="+self.lang
        response = req.urlopen(uri)
        self.forecast = json.loads (response.read())
        return self.forecast

    def __init__(self, key, location, lang):
        self.apikey = key
        self.location = location
        self.lang = lang
        self.data=self.getCurrentData()
        self.forecast = self.getForecastData()

    #Refresh data for current weather and the forecast
    def update(self):
        self.data = self.getCurrentData()
        self.forecast = self.getForecastData()

#Current Weather

    #check if temperature exists
    def hasCTemp(self):
        return ("main" in self.data and "temp" in self.data["main"])

    #Return temperature in Kelvin. Returntype: Float. 
    #Error returns String 
    def getCurrentTemperatureK(self):
        try:
            return self.data["main"]["temp"]
        except KeyError:
            return "NotFound"
        
    #Return temperature in Celsius. Returntype: Float. 
    #Error returns String
    def getCurrentTemperatureC(self):
        try:
            return self.data["main"]["temp"] - 273.15
        except KeyError:
            return "NotFound"
    
    #check if description exists
    def hasCDesc(self):
        return ("weather" in self.data and "description" in self.data["weather"][0])


    #Return weather description. Returntype: Array of Strings. 
    #Error returns string in the Array
    def getCurrentDescription(self):
        wetter = []
        try: 
            for x in range (0, len(self.data["weather"])):
                wetter.append(self.data["weather"][x]["description"])
        except KeyError:
            wetter.append("NotFound")

        return wetter

    #check if wind exists
    def hasCWind(self):
        return ("wind" in self.data)


    #Return tupel of three wind informations. 
    # 1. direction as int. "NotFound" for error
    # 2. direction as string. "NotFound" for error
    # 3. speed as float. "NotFound" for error
    # Returntype: Float. 
    #Error returns String
    def getCurrentWind(self):
        
        if "wind" in self.data:
            wind = self.data["wind"]

        if "speed" in wind:
            speed = wind["speed"]
        else:
            speed = "NotFound"
                   
        if "deg" in wind:
            direction = wind["deg"]
        else: 
            direction = "NotFound"

        if direction == "NotFound":
            direction_human = "NotFound"
        else:
            direction_human = float(direction)

            if direction_human<= 11.25:
                direction_human= "Nord"
            elif direction_human> 11.25 and direction_human<= 33.75:
                direction_human= "NordNordOst"
            elif direction_human> 33.75 and direction_human<= 56.25:
                direction_human= "NordOst"
            elif direction_human> 56.25 and direction_human<= 78.75:
                direction_human= "OstNordOst"
            elif direction_human> 78.75 and direction_human<= 101.25:
                direction_human= "Ost"
            elif direction_human> 101.25 and direction_human<= 123.75:
                direction_human= "OstSüdOst"
            elif direction_human> 123.75 and direction_human<= 146.25:
                direction_human= "SüdOst"
            elif direction_human> 146.25 and direction_human<= 168.75:
                direction_human= "SüdSüdOst"
            elif direction_human> 168.75 and direction_human<= 191.25:
                direction_human= "Süd"
            elif direction_human> 191.25 and direction_human<= 213.75:
                direction_human= "SüdSüdWest"
            elif direction_human> 213.75 and direction_human<= 236.25:
                direction_human= "SüdWest"
            elif direction_human> 236.25 and direction_human<= 258.75:
                direction_human= "WestSüdWest"
            elif direction_human> 258.75 and direction_human<= 281.25:
                direction_human= "West"
            elif direction_human> 281.25 and direction_human<= 303.75:
                direction_human= "WestNordWest"
            elif direction_human> 303.75 and direction_human<= 326.25:
                direction_human= "NordWest"
            elif direction_human> 326.25 and direction_human<= 348.75:
                direction_human= "NordNordWest"
            elif direction_human> 348.75:
                direction_human= "NordOst"
            else: 
                direction_human= "Error"

        return direction, direction_human, speed

    #check if humidity exists
    def hasCHum(self):
        return ("main" in self.data and "humidity" in self.data["main"])


    #Return humidity in percent. Returntype: Int. 
    #Error returns String
    def getHumidity(self):
        try:
            return self.data["main"]["humidity"]
        except KeyError:
            return "NotFound"

    #check if pressure exists
    def hasCPres(self):
        return ("main" in self.data and "pressure" in self.data["main"])


    #Return Pressure in hPa. Returntype: Int. 
    #Error returns String
    def getPressure(self):
        try:
            return self.data["main"]["pressure"]
        except KeyError:
            return "NotFound"

    #check if visibility exists
    def hasCVis(self):
        return ("visibility" in self.data)


    #Return visibility in meters. Returntype: Int. 
    #Error returns String
    def getVisibility(self):
        try:
            return self.data["visibility"]
        except KeyError:
            return "NotFound"

    #check if cloud exists
    def hasCCloud(self):
        return ("clouds" in self.data and "all" in self.data["clouds"])


    #Return cloudiness in percent. Returntype: Int. 
    #Error returns String
    def getCloud(self):
        try:
            return self.data["clouds"]["all"]
        except KeyError:
            return "NotFound"

    #check if rain exists
    def hasRain(self):
        return ("rain" in self.data)


    #Return Rain volume for the last 3 hours in mm. Returntype: Int. 
    #Error returns String
    def get3hRain(self):
        try:
            return self.data["rain"]["3h"]
        except KeyError:
            return "NotFound"

    #Return Rain volume for the last 1 hours in mm. Returntype: Int. 
    #Error returns String
    def get1hRain(self):
        try:
            return self.data["rain"]["1h"]
        except KeyError:
            return "NotFound"

    #check if snow exists
    def hasSnow(self):
        return ("snow" in self.data)


    #Return snow volume for the last 3 hours in mm. Returntype: Int. 
    #Error returns String
    def get3hSnow(self):
        try:
            return self.data["snow"]["3h"]
        except KeyError:
            return "NotFound"

    #Return snow volume for the last 1 hours in mm. Returntype: Int. 
    #Error returns String
    def get1hSnow(self):
        try:
            return self.data["snow"]["1h"]
        except KeyError:
            return "NotFound"


#Forecast
    def getForecastTempC(self):
        
        temp_zeit=[]
        temp_werte=[]

        for condition in self.forecast["list"]:
            tz= condition["dt_txt"]
            temp_zeit.append(tz.split(" ")[0]+"\n"+tz.split(" ")[1])
            temp=condition["main"]["temp"]-273
            temp_werte.append(temp)

        return temp_zeit, temp_werte

    def getForecastConditions(self):
        temp_zeit=[]
        desc = []
        for condition in self.forecast["list"]:
            tz= condition["dt_txt"]
            temp_zeit.append(tz.split(" ")[0]+"\n"+tz.split(" ")[1])
            for con in condition["weather"]:
                desc.append(con["description"])
        return desc



#Utility
    def plotForecastTemp(self, zeit, temp):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(zeit, temp)
        ax.grid(True)
        fig.suptitle("Vorhersage Temperatur.")
        ax.xaxis.set_major_locator(ticker.MultipleLocator(4))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
        plt.show()
