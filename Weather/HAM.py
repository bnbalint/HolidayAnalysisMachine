import getWeather
import getLatLon

## Arguments
CITY = "Palermo"
COUNTRY = "Italy"
MONTH = "April"
YEAR = "2018"

## Report header
outString = "Holiday Analysis Machine Report\n"
outString += "{}, {}\n".format(CITY, COUNTRY)
outString += "{}, {}\n\n\n".format(MONTH, YEAR)


## Get the lat/lon
LAT, LON = getLatLon.getLatLon(CITY, COUNTRY)
print("Lat = {}".format(LAT))
print("Lon = {}\n".format(LON))



## get the weather
outString += "WEATHER\n"
outString += "-----------------------------------------------------\n"
weather = getWeather.getWeather(CITY, COUNTRY, MONTH)
outString += weather



print(outString)