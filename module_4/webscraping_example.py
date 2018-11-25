"""This program prints a list of countries from the http://example.webscraping.com/
Asks the user to enter the country name from the list of the countries.
Prints following information about country: area, population, capital, currency name.
"""

import random
import time
from urllib.request import urlopen, Request

# start page for getting information
BASE_URL = "http://example.webscraping.com/places/default/index/"


def get_request_headers():
    """Return information for headers"""

    return {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'}


def get_page_from_server(page_url: str) -> str:  # getting page from server
    """Return information about the page in the string format"""

    request = Request(page_url, headers=get_request_headers())
    page = urlopen(request).read()

    return str(page)


def get_tags_info(tag: str, page: str, additional_characters=0) -> list:
    """Return information that has a tag"""

    # finding the place where tag is located
    # the tag for each country is the same but the last 11 characters are different
    # 11 - is a number of characters to reach the country name
    tag_size = len(tag) + additional_characters
    tag_count = page.count(tag)  # counts the number of times tag appears on the page
    countries_list = []

    while tag_count > 0:
        tag_index = page.find(tag)  # find the index where the tag appears on the page
        start_value = tag_size + tag_index  # start value for searching on the page
        result = ''

        # finds the country and adds it to the list of countries
        for item in page[start_value:]:
            if item != '<':
                result += item
            else:
                countries_list.append(result)
                break

        tag_count -= 1
        page = page[tag_index+1:]  # cut the part of the page with the found tag

    return countries_list


EXAMPLE_PAGE = get_page_from_server(BASE_URL)
COUNTRY_TAG = '<img src="/places/static/images/flags/'
# list of countries from the first page
COUNTRIES = get_tags_info(COUNTRY_TAG, EXAMPLE_PAGE, 11)  # third argument is additional characters
COUNTRIES_DICT = {'0': COUNTRIES}

# iterates through pages and adds countries on the page to the list of countries
for page_number in range(1, 26):
    time.sleep(random.randint(1, 5))
    next_page = BASE_URL + str(page_number)
    EXAMPLE_PAGE = get_page_from_server(next_page)
    # third argument is additional characters
    current_countries = get_tags_info(COUNTRY_TAG, EXAMPLE_PAGE, 11)
    COUNTRIES.extend(current_countries)
    COUNTRIES_DICT[str(page_number)] = current_countries

print(COUNTRIES)

COUNTRY_NAME = input("Enter the name of the country from the previous list: ")

# finds on what page is the country that the user asks
for page_number, country_list in COUNTRIES_DICT.items():
    if COUNTRY_NAME in country_list:
        next_page = BASE_URL + page_number

# finds position of the user country in the list of countries
COUNTRY_INDEX = COUNTRIES.index(COUNTRY_NAME) + 1
COUNTRY_NAME = COUNTRY_NAME.replace(' ', '-')  # convert name of the country to the url format
# country page for getting information
COUNTRY_URL_BASE = 'http://example.webscraping.com/places/default/view/'
COUNTRY_URL = COUNTRY_URL_BASE + COUNTRY_NAME + str(COUNTRY_INDEX)
COUNTRY_PAGE = get_page_from_server(COUNTRY_URL)

COUNTRY_TAG_INFO = '<td class="w2p_fw">'
COUNTRY_INFO = get_tags_info(COUNTRY_TAG_INFO, COUNTRY_PAGE)

print(f"\nInformation about {COUNTRY_NAME.replace('-', ' ').upper()}\n")
print(f"Area: {COUNTRY_INFO[1]}")
print(f"Population: {COUNTRY_INFO[2]}")
print(f"ISO 3166: {COUNTRY_INFO[3]}")
print(f"Capital: {COUNTRY_INFO[5]}")
print(f"Currency name: {COUNTRY_INFO[9]}")
print(f"Phone: {COUNTRY_INFO[10]}")
