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


ASSIGNED QUERIES & RESULTS:

General Notes:
- fetching data from the urls is a performance bottleneck in this application.







