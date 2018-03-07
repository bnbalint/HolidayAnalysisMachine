from Utils.soupUtils import getSoup


def getLatLon(CITY, COUNTRY):
  webCommand = "https://en.wikipedia.org/wiki/" + CITY
  outString = ""

  try:
      soup = getSoup(webCommand)

  except Exception as error:
      return 'Error during requests to {0} : {1} \nNo location for you!'.format(webCommand, str(error))

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
