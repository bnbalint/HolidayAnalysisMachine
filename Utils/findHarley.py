# Set up BeautifulSoup
from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException


def findHarley(CITY, COUNTRY, LAT, LON):
  webCommand = "https://www.harley-davidson.com/ap/en/find-a-dealer.html#locator?query=" + \
  CITY.lower() + "," + COUNTRY.lower() + \
  "&latlng=" + LAT + "," + LON + "&page=1"
  outString = ""

  ## retrieve the webpage
  try:
    response = get(webCommand, stream=True)
    webContent = response.content

  except RequestException as error:
    return 'Error during requests to {0} : {1} \nNo motorcycles for you!'.format(webCommand, str(error))

  ## create the parser
  try:
    soup = BeautifulSoup(webContent, 'html.parser')

  except:
    return "Failure to convert to minestrone. No motorcycles for you!"

  print(webCommand)

  ## Grab the title
  pageTitle = soup.title.get_text()


  outString += pageTitle
  outString += "\n\n"

  print(soup.prettify())

  #< h3 class ="find-a-dealer-results__total" > 31 DEALERS NEAR Palermo, Province of Palermo, Italy < / h3 >



  return outString



CITY = "Palermo"
COUNTRY = "Italy"
LAT = "38.117"
LON = "13.367"

findHarley(CITY, COUNTRY, LAT, LON)