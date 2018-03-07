from Utils.soupUtils import getSoup


def getWeather(CITY, COUNTRY, MONTH):
  webCommand = "http://www.holiday-weather.com/" + CITY + "/averages/" + MONTH + "/"
  outString = ""

  try:
      soup = getSoup(webCommand)

  except Exception as error:
      return 'Error during requests to {0} : {1} \nNo weather for you!'.format(webCommand, str(error))


  ## Grab the title
  pageTitle = soup.title.get_text()

  ## Check to see if the country matches (url uses city only)
  if COUNTRY.lower() not in pageTitle.lower():
    print("Incorrect Country?")


  outString += pageTitle
  outString += "\n\n"

  ## Find the parent object
  match = soup.find("ul", class_="destination-info")

  ## Extract the text from the child objects, remove empty lines
  matchText = (match.get_text()).split("\n")
  while "" in matchText:
    matchText.remove("")

  ## Parse content, based on values previously seen
  for index in range(len(matchText)):
    if matchText[index] == "Temperature":
      outString += "Avg Temperature  {}   ({})\n".format(matchText[index+2], matchText[index+1])

    elif matchText[index] == "High Temperature":
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
