#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:41:14 2018

@author: gk
"""

import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame
import webbrowser

website = 'https://en.wikipedia.org/wiki/NFL_win%E2%80%93loss_records'
#webbrowser.open(website)

nfl_frame = pd.read_clipboard()
print(nfl_frame)