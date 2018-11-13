from urllib.request import urlopen, Request

# start page for getting information
example_url = "http://example.webscraping.com/"


def get_page_from_server(page_url: str) -> str:  # getting page from server
    """Return information about the page in the string format"""

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'}
    request = Request(page_url, headers=headers)
    page = urlopen(request).read()

    return str(page)


def get_tag_info(tag: str, page: str) -> str:
    """Return information that has a tag"""

    # finding the place where tag is located
    tag_size = len(tag)
    tag_index = page.find(tag)
    start_value = tag_size + tag_index

    result = ''
    for item in page[start_value:]:
        if item != "<":
            result += item
        else:
            break

    return result


example_page = get_page_from_server(example_url)
print(example_page)