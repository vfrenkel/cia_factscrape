import sys
sys.path.append('../libs/beautifulsoup4-4.1.3')

import urllib
import bs4

FACTBOOK_BASE_URL = "https://www.cia.gov/library/publications/the-world-factbook/"

def fetch_main_html():
    ciafb_main = urllib.urlopen(FACTBOOK_BASE_URL + "print/textversion.html")

    ciafb_main_html = '\n'.join(ciafb_main.readlines())

    return ciafb_main_html

def fetch_country_html(name):
    ciafb_main_html = fetch_main_html()
    ciafb_main_soup = bs4.BeautifulSoup(ciafb_main_html, "lxml")

    links = ciafb_main_soup.find_all('a')

    for a in links:
        if ('../geos/countrytemplate') in str(a.get('href')) \
                and name in a:
            country_source = urllib.urlopen(FACTBOOK_BASE_URL + str(a.get('href'))[3:])
            return '\n'.join(country_source.readlines())

def fetch_all_countries_html_list():
    ciafb_main_html = fetch_main_html()
    ciafb_main_soup = bs4.BeautifulSoup(ciafb_main_html, "lxml")

    links = ciafb_main_soup.find_all('a')

    country_htmls = []

    for a in links:
        if (('../geos/countrytemplate') in str(a.get('href'))):
            print "GATHERING " + FACTBOOK_BASE_URL + str(a.get('href'))[3:]
            country_source = urllib.urlopen(FACTBOOK_BASE_URL + str(a.get('href'))[3:])
            country_htmls.append('\n'.join(country_source.readlines()))

    print "COMPUTING..." # add message to let people know pulling of data finished, now computing.

    return country_htmls

def fetch_matching_countries(attribute, operator, value):
    matching_countries = []

    if operator == '=':
        matching_countries = string_equality_match(attribute, value)
    elif operator == '>':
        matching_countries = number_objects_match(attribute, operator, value)
    else:
        print "ERROR: unknown operator."

    return matching_countries


def string_equality_match(attribute, value):
    country_htmls = fetch_all_countries_html_list()
    matching_countries = []

    for html in country_htmls:
        country_soup = bs4.BeautifulSoup(html, "lxml")
        
        country_attributes= country_soup.find_all("a")

        for attr in country_attributes:
#            print "attribute: " + attribute + " attr.get_text(): " + str(attr.get_text()) + "\n"
            #valid ones have text (e.g. not images)
            if attribute.lower() in str(attr.get_text()).lower():
                #correct attribute located, now search for value in corresponding info area.
                if value.lower() in str(attr.parent.parent.parent.find_next_sibling().find('div').get_text()).lower():
                    matching_countries.append(str(country_soup.find("span").get_text()))

    return matching_countries

def number_objects_match(attribute, operator, value):
    country_htmls = fetch_all_countries_html_list()
    matching_countries = []

    for html in country_htmls:
        country_soup = bs4.BeautifulSoup(html, "lxml")
        
        country_attributes= country_soup.find_all("a")

        for attr in country_attributes:
            #valid ones have text (e.g. not images)
            if attribute.lower() in str(attr.get_text()).lower():
                #correct attribute located, now search for value in corresponding info area.
                try:
                    info_list = str(attr.parent.parent.parent.find_next_sibling().find('div').get_text()).split(";")
                except Exception:
                    continue

                if (operator == '>') and (len(info_list) > int(value)):
                    matching_countries.append(str(country_soup.find("span").get_text()))

    return matching_countries


def special_find_lat_lon_capital_vacation(lat_lon_separation):
    matching_countries = []
    country_lat_lon = find_all_lat_lon_dict()

    max_capitals_dict = {}

#    print country_lat_lon
    max_num_cities = 0
    # move this test square across entire map and use coords with max num of cities after completion of scan.
    test_area = [-90, -180, -90+lat_lon_separation, -180+lat_lon_separation]
    while test_area[0] <= 90: #loop until test area runs off the last top row in map.
        candidate_capitals_dict = {}

        # search all countries using the current test area.
        for country, lat_lon in country_lat_lon.iteritems():
            #compute how many (and which) cities are in this test_area.
            if lat_lon[0] > test_area[0] \
                    and lat_lon[1] > test_area[1] \
                    and lat_lon[0] < test_area[2] \
                    and lat_lon[1] < test_area[3]:
                candidate_capitals_dict[country] = lat_lon
                
            if len(candidate_capitals_dict) > max_num_cities:
                max_capitals_dict = candidate_capitals_dict.copy()
                max_num_cities = len(candidate_capitals_dict)

        #move twice as many lon positions as lat... 180:90 ratio
        # scan from left to right, every row.
        if test_area[3] >= 180: #right corner reached end of map, shift rect down and reset lon
            test_area[0] += 1 #lat_lon_separation
            test_area[2] += 1 #lat_lon_separation #would be less precise, but faster
            test_area[1] = -180
            test_area[3] = -180 + lat_lon_separation
        else: #move test area right...
            test_area[1] += 1 #lat_lon_separation
            test_area[3] += 1 #lat_lon_separation

    # return countries containing the capitals chosen.
    for country, lat_lon in max_capitals_dict.iteritems():
        matching_countries.append(country)

    return matching_countries

#S/N --> lat , E/W --> lon
def find_all_lat_lon_dict():
    countries_lat_lon = dict()
    country_htmls = fetch_all_countries_html_list()
#    country_htmls = [fetch_country_html("Afghanistan")]

    for html in country_htmls:
        country_soup = bs4.BeautifulSoup(html, "lxml")
        
        country_attributes= country_soup.find_all("a")

        for attr in country_attributes:
            #valid ones have text (e.g. not images)
            if "capital" in str(attr.get_text()).lower():
                #capital attribute located, now record lat and lon values in corresponding info area.
                try:
                    lat_lon_string = str(attr.parent.parent.parent.find_next_sibling().find_all('div')[1].get_text()).split(":")[1][-16:].split(",")
                    #if WEST (W) or SOUTH (S) specified, make that coordinate negative
                    lat_lon_list = [int(lat_lon_string[0][0:3]), int(lat_lon_string[1][0:3])]
#                    print lat_lon_list
#                    print lat_lon_string
                    if lat_lon_string[0][6] == 'S':
                        lat_lon_list[0] = -1 * lat_lon_list[0]
                    if lat_lon_string[1][6] == 'W':
                        lat_lon_list[1] = -1 * lat_lon_list[1]
#                    print lat_lon_list
                    countries_lat_lon[str(country_soup.find("span").get_text())] = \
                        (lat_lon_list[0], lat_lon_list[1])
                except Exception:
                    continue #there are some nasties in the html pages, skip them.

    return countries_lat_lon
