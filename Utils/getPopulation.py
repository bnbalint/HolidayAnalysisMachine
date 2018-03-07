from Utils.soupUtils import getSoup, parse_html_table
import pandas as pd


def getPopulation(CITY, COUNTRY):
    country = COUNTRY[0].upper() + COUNTRY[1:].lower()
    webCommand = "http://www.citypopulation.de/" + country + "-Cities.html"
    outString = ""

    try:
        soup = getSoup(webCommand)
    except Exception as error:
        return 'Error during requests to {0} : {1} \nNo population for you!'.format(webCommand, str(error))

    # Find the object
    df = parse_html_table(soup.find_all('table')[2]).set_index("Name")
    popColumn = df.columns[len(df.columns)-3]  # In case there is a different population column for different countries
    try:
        cityPop = df[df.index.str.contains(CITY)][popColumn]  # This is complex since city can have multiple names
        outString += "Population of " + CITY + " is " + str(max(cityPop))
    except:
        return "Error - city not found in population table!"

    df.sort_values(by=popColumn, ascending=False, inplace=True)
    valueInCountry = min([df.index.tolist().index(i) for i in df.index.tolist() if CITY in i]) + 1
    outString += "\nRanking of " + str(valueInCountry) + " overall in " + COUNTRY
    return outString


print(getPopulation("Naples", "Italy"))
