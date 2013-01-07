SYSTEM REQUIREMENTS TO RUN THE APPLICATION:
Python 2.6 : http://python.org/download/ : preferably use your package manager to install this
python-lxml : http://lxml.de/installation.html : preferably use your package manager to install this

TO RUN:
1 - go to src directory
2 - make sure main.py is still executable (run 'chmod a+x' if it isn't)
3 - run ./main.py. Assumes you have a python 2.6 interpreter installed (will probably work with 2.7 as well).

The design directory contains design documents and planning for the application.


APPROACH:

The language of choice for this project is Python because the project requirements allow me to greatly value speed of development over speed of execution.

The software engineering approach taken for this project is a hybrid between the waterfall model, where everything is planned out from the start before being coded, and the agile development model, where the software is incrementally revised and the general plan modified according to issues/realizations that come up.

Used the BeautifulSoup library to access DOM elements and look through factbook descriptions of various attributes. No need to reinvent the wheel...

Used Python's standard library urllib module to fetch data from factbook urls.

The program does require that you know roughly what you're looking for. (e.g. that the continent a country is in will be listed under it's location description, if it's landlocked that will be listed under coastline, etc.) The advantage of this approach is that you can query just about any attribute/value pair you can think of (flexible!)



ASSIGNED QUERIES & RESULTS:

General Notes:
- fetching data from the urls is a performance bottleneck in this application.
- One thing I noticed from running compound queries is that it probably would have been better to organize my system around a single fetch of data that happens at the start of a command, and then reuse that information for each refiner...

1.     List countries in South America that are prone to earthquakes.

QUERY@CIA_FACTBOOK>>> location=South America , natural hazards=earthquake 

 QUERY RETURNED THESE COUNTRIES:
Brazil
Falkland Islands (Islas Malvinas)
South Georgia and South Sandwich Islands
Chile
Suriname
Uruguay
French Polynesia
Peru
Saint Helena, Ascension, and Tristan da Cunha
Colombia
Guyana
Paraguay
Argentina
Bolivia
Venezuela
Ecuador


The results make sense, these are all countries in South America and have histories of earthquakes.


2.     List countries in Asia with more than 10 political parties.

QUERY@CIA_FACTBOOK>>> location=Asia , political parties > 10

 QUERY RETURNED THESE COUNTRIES:
Turkey                          
Afghanistan
Bangladesh
Bhutan
Nepal
Cambodia
Korea, South
Maldives
Laos
Paracel Islands
Turkmenistan
Brunei
Singapore
Oceans ::
Cocos (Keeling) Islands
China
Armenia
Thailand
Ashmore and Cartier Islands
Kazakhstan
Kyrgyzstan
Georgia
Philippines
Indonesia
Christmas Island
Mongolia
Spratly Islands
Russia
Korea, North
Burma
Pakistan
Macau
Egypt
Hong Kong
India
Azerbaijan
Uzbekistan
Malaysia
Vietnam
Timor-Leste
Sri Lanka
Japan
Taiwan
Tajikistan

The result makes sense for the most part.
There is a little bit of noise in this result... "Oceans ::" made it in there... not all the pages play nice.


3.     Find all countries that have the color blue in their flag.

QUERY@CIA_FACTBOOK>>> flag=blue

 QUERY RETURNED THESE COUNTRIES:
Cambodia                        
Ethiopia
Aruba
Swaziland
Argentina
South Georgia and South Sandwich Islands
American Samoa
Slovenia
Guatemala
Bosnia and Herzegovina
Liberia
Netherlands
Micronesia, Federated States of
Tanzania
Christmas Island
Gabon
Niue
New Zealand
European Union
Samoa
Guam
Uruguay
India
Azerbaijan
Lesotho
Saint Vincent and the Grenadines
Northern Mariana Islands
Solomon Islands
Turks and Caicos Islands
Saint Lucia
San Marino
Mongolia
France
Rwanda
Slovakia
Somalia
Laos
Nauru
Norway
Cook Islands
Cuba
Montenegro
Virgin Islands
Armenia
Dominican Republic
Ukraine
Cayman Islands
Finland
Central African Republic
Mauritius
Liechtenstein
British Virgin Islands
Russia
Bulgaria
United States
Romania
Chad
South Africa
Tokelau
Fiji
Sweden
Malaysia
Sint Maarten
Brazil
Faroe Islands
Panama
Congo, Democratic Republic of the
Costa Rica
Luxembourg
Cape Verde
Andorra
Ecuador
Czech Republic
Australia
El Salvador
Tuvalu
Pitcairn Islands
Saint Pierre and Miquelon
Marshall Islands
Chile
Puerto Rico
Kiribati
Haiti
Belize
Sierra Leone
Philippines
Moldova
Namibia
French Polynesia
Thailand
Korea, North
Seychelles
Estonia
Kosovo
Korea, South
Uzbekistan
Djibouti
Antigua and Barbuda
Colombia
Taiwan
Nicaragua
Barbados
Falkland Islands (Islas Malvinas)
Palau
Curacao
Nepal
Anguilla
Venezuela
Israel
Iceland
Saint Helena, Ascension, and Tristan da Cunha
Kazakhstan
Eritrea
British Indian Ocean Territory
Montserrat
South Sudan
Honduras
Equatorial Guinea
Serbia
Botswana
United Kingdom
Gambia, The
Greece
Paraguay
Croatia
Comoros

The result makes sense, I recognize these countries have blue in their flag.



4.     A landlocked country is one that is entirely enclosed by land. For example, Austria is landlocked and shares its borders with Germany, Czech Republic, Hungary, etc. There are certain countries that are entirely landlocked by a single country. Find these countries.

QUERY@CIA_FACTBOOK>>> coastline=landlock

 QUERY RETURNED THESE COUNTRIES:
Afghanistan                     
Czech Republic
Bhutan
Nepal
San Marino
Luxembourg
Andorra
Ethiopia
Rwanda
Slovakia
Swaziland
Laos
Bolivia
Burkina Faso
Belarus
Zambia
Malawi
Zimbabwe
Armenia
Holy See (Vatican City)
Kazakhstan
Kyrgyzstan
Central African Republic
Macedonia
Moldova
Paraguay
Liechtenstein
Mongolia
Mali
Switzerland
West Bank
Chad
Kosovo
Serbia
Azerbaijan
Uzbekistan
Lesotho
Austria
Uganda
Burundi
Hungary
Niger
Tajikistan
Botswana
South Sudan


I recognize these countries as landlocked, so result makes sense.


5.     I want to go on a vacation with a friend. Our goal is to visit as many capital cities as we can in as short a geographical distance as possible. To make things easier (and not worry about spherical geometry), we are fine with travelling to capitals that are within 10 degrees of latitude and longitude of each other. Find the lat/long coordinates and the list of countries/capitals so that the number of capitals is maximized.


QUERY@CIA_FACTBOOK>>> DO=lat_lon_vaca : 10

Saint Martin
Curacao
Saint Lucia
Montserrat
Trinidad and Tobago
British Virgin Islands
Grenada
Anguilla
Venezuela
Dominican Republic
Saint Kitts and Nevis
Virgin Islands
Saint Vincent and the Grenadines
Puerto Rico
Antigua and Barbuda
Saint Barthelemy
Dominica


This result makes a lot of sense. These island nations are very close together on the map! Go to these countries' capitals..


