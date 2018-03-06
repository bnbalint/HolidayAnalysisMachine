# Set up BeautifulSoup
from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException


def getWeather(CITY, COUNTRY, MONTH):
  webCommand = "http://www.holiday-weather.com/" + CITY + "/averages/" + MONTH + "/"
  outString = ""

  try:
    response = get(webCommand, stream=True)
    webContent = response.content

  except RequestException as error:
    print('Error during requests to {0} : {1}'.format(webCommand, str(error)))
    return "No weather for you!"


  try:
    soup = BeautifulSoup(webContent, 'html.parser')

  except:
    print("Failure to convert to minestrone")
    return "No weather for you!"

  ## Check the country
  pageTitle = soup.title.get_text()

  if COUNTRY.lower() not in pageTitle.lower():
    print("Incorrect Country?")



  outString += pageTitle
  outString += "\n\n"

  for match in soup.find_all("ul", class_="destination-info"):
    matchText = (match.get_text()).split("\n")
    while "" in matchText:
      matchText.remove("")


    for index in range(len(matchText)):
      if matchText[index] == "High Temperature":
        outString += "High Temperature {}   ({})\n".format(matchText[index+2], matchText[index+1])

      elif matchText[index] == "Low Temperature":
        outString += "Low Temperature  {}   ({})\n".format(matchText[index+2], matchText[index+1])

      elif matchText[index] == "Sea Temperature":
        outString += "Sea Temperature  {}   ({})\n".format(matchText[index + 2], matchText[index+1])

      elif matchText[index] == "Sunshine Hours":
        outString += "Sunshine Hours   {}\n".format(matchText[index+1])

      elif matchText[index] == "Chance Of Rain":
        outString += "Chance of Rain   {}\n".format(matchText[index+1])

      elif matchText[index] == "Rainfall days":
        outString += "Rainfall Days    {}\n".format(matchText[index+1])

      elif matchText[index] == "Chance Of Cloudy Day":
        outString += "Chance of Clouds {}\n".format(matchText[index + 1])

  return outString


## these will be inputs to HAM
CITY = "Palermo"
COUNTRY = "Italy"
MONTH = "March"
weather = getWeather(CITY, COUNTRY, MONTH)

print(weather)