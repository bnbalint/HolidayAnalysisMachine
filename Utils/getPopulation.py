from Utils.soupUtils import getSoup


def getPopulation(CITY, COUNTRY):
    country = COUNTRY[0].upper() + COUNTRY[1:].lower()
    webCommand = "http://www.citypopulation.de/" + country + "-Cities.html"
    outString = ""

    try:
        soup = getSoup(webCommand)

    except Exception as error:
        return 'Error during requests to {0} : {1} \nNo population for you!'.format(webCommand, str(error))

    # Find the object
    match = soup.find(id="citysection")
    for row in list(filter(lambda x: x != "\n", match.tbody.children)):
        # Get all city names out of this row of the table
        cityNames = [x.next for x in filter(lambda x: x != "\n", row.contents[1].find_all("span"))]
        for city in cityNames:
            if str.count(str.lower(city), str.lower(CITY)) > 0:
                outString += "Population of " + CITY + " is " + row.contents[-3].next
                return outString
    return "Error - city not found in population table!"


print(getPopulation("Alicante", "Spain"))
