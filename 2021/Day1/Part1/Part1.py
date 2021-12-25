from bs4 import BeautifulSoup as bs
from urllib import (
    urlopen, urlparse, urlunparse, urlretrieve
) 

import os
import sys

text = urlopen('https://adventofcode.com/2021/day/1/input')
