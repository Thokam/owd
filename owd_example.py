from owd import owd
import pprint

with open("openweathermap.key") as file:
    apikey=file.readline()

lang = "de"
location = "Oldenburg, de"
o = owd(apikey, location, lang)

#data = o.getCurrentData()
#print("Aktuelle Daten")
#pprint.pprint (data)

data = o.getCurrentTemperatureC()
print("Temp C: %.2f"%data)

data = o.getCurrentDescription()
print("Description: "+str(data))

print("Wind")
data, data1, data2 = o.getCurrentWind()
print("...Richtung: "+str(data))
print("...Richtung Human: "+str(data1))
print("...Speed: "+str(data2))

data = o.getHumidity()
print("Luftfeuchte: "+str(data))

data = o.getPressure()
print("Druck: "+str(data))

data = o.getVisibility()
print("Sichtweite: "+str(data))

data = o.getCloud()
print("Wolken: "+str(data))

#data = o.getForecastData()
#pprint.pprint(data)


time,werte = o.getForecastTempC()
o.plotForecast(time, werte, "Temp")
