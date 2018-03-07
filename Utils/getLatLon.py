# Set up BeautifulSoup
from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException


def getLatLon(CITY, COUNTRY):
  webCommand = "https://en.wikipedia.org/wiki/" + CITY
  outString = ""

  ## retrieve the webpage
  try:
    response = get(webCommand, stream=True)
    webContent = response.content

  except RequestException as error:
    return 'Error during requests to {0} : {1} \nNo location for you!'.format(webCommand, str(error))

  ## create the parser
  try:
    soup = BeautifulSoup(webContent, 'html.parser')

  except:
    return "Failure to convert to minestrone. No location for you!"

  ## Find the object
  match = soup.find("span", class_="geo")

  ## Extract the text, remove empty lines
  matchText = (match.get_text()).split("; ")

  if len(matchText) == 2:
    lat = matchText[0]
    lon = matchText[1]
    return lat, lon

  else:
    return "0", "0"
