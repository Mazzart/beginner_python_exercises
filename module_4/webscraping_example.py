"""This program prints a list of countries from the http://example.webscraping.com/
Asks the user to enter the country name from the list of the countries.
Prints following information about country: area, population, capital, currency name.
"""

import random
import time
from urllib.request import urlopen, Request

# start page for getting information
base_url = "http://example.webscraping.com/places/default/index/"


def get_page_from_server(page_url: str) -> str:  # getting page from server
    """Return information about the page in the string format"""

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'}
    request = Request(page_url, headers=headers)
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
            if item != "<":
                result += item
            else:
                countries_list.append(result)
                break

        tag_count -= 1
        page = page[tag_index+1:]  # cut the part of the page with the found tag

    return countries_list


example_page = get_page_from_server(base_url)
COUNTRY_TAG = '<img src="/places/static/images/flags/'
# list of countries from the first page
countries = get_tags_info(COUNTRY_TAG, example_page, 11)  # third argument is additional characters
countries_dict = {'0': countries}

# iterates through pages and adds countries on the page to the list of countries
for page_number in range(1, 26):
    time.sleep(random.randint(1, 10))
    next_page = base_url + str(page_number)
    example_page = get_page_from_server(next_page)
    current_countries = get_tags_info(COUNTRY_TAG, example_page, 11)  # third argument is additional characters
    countries.extend(current_countries)
    countries_dict[str(page_number)] = current_countries

print(countries)

country_name = input("Enter the name of the country from the previous list: ")

# finds on what page is the country that the user asks
for page_number, country_list in countries_dict.items():
    if country_name in country_list:
        next_page = base_url + page_number

country_index = countries.index(country_name) + 1  # finds position of the user country in the list of countries
country_name = country_name.replace(' ', '-')  # convert name of the country to the url format
# country page for getting information
country_url = 'http://example.webscraping.com/places/default/view/' + country_name + str(country_index)
country_page = get_page_from_server(country_url)

COUNTRY_TAG_INFO = '<td class="w2p_fw">'
country_info = get_tags_info(COUNTRY_TAG_INFO, country_page)

print(f"\nInformation about {country_name.replace('-', ' ').upper()}\n")
print(f"Area: {country_info[1]}")
print(f"Population: {country_info[2]}")
print(f"ISO 3166: {country_info[3]}")
print(f"Capital: {country_info[5]}")
print(f"Currency name: {country_info[9]}")
print(f"Phone: {country_info[10]}")
