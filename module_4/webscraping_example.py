"""This program prints a list of countries from the http://example.webscraping.com/"""

from urllib.request import urlopen, Request

# start page for getting information
example_url = "http://example.webscraping.com/"


def get_page_from_server(page_url: str) -> str:  # getting page from server
    """Return information about the page in the string format"""

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'}
    request = Request(page_url, headers=headers)
    page = urlopen(request).read()

    return str(page)


def get_tags_info(tag: str, page: str) -> list:
    """Return information that has a tag"""

    # finding the place where tag is located
    # the tag for each country is the same but the last 11 characters are different
    # 11 - is a number of characters to reach the country name
    tag_size = len(tag) + 11
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


example_page = get_page_from_server(example_url)
COUNTRY_TAG = '<img src="/places/static/images/flags/'
countries = get_tags_info(COUNTRY_TAG, example_page)

for country in countries:
    print(country)
