# Set up BeautifulSoup
from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException


def getSoup(webRequest):
    ## retrieve the webpage
    try:
        response = get(webRequest, stream=True)
        webContent = response.content

    except RequestException as error:
        return error

    ## create the parser
    try:
        soup = BeautifulSoup(webContent, 'html.parser')

    except Exception as error:
        return error

    return soup
