#import urllib2
#response = urllib2.urlopen('https://www.basketball-bund.net/public/ergebnisDetails.jsp?type=1&spielplan_id=1828276&liga_id=26155&defaultview=1')
#html = response.read()
#from xml.etree.ElementTree import fromstring

import pandas as pd

url = r'https://www.basketball-bund.net/public/ergebnisDetails.jsp?type=1&spielplan_id=1828276&liga_id=26155&defaultview=1'
tables = pd.read_html(url)

#check http://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/
