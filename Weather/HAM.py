import getWeather


CITY = "Palermo"
COUNTRY = "Italy"
MONTH = "April"
YEAR = "2018"

outString = "Holiday Analysis Machine Report\n"
outString += "{}, {}\n".format(CITY, COUNTRY)
outString += "{}, {}\n\n\n".format(MONTH, YEAR)

## get the weather
outString += "WEATHER\n"
outString += "-----------------------------------------------------\n"
weather = getWeather.getWeather(CITY, COUNTRY, MONTH)
outString += weather



print(outString)