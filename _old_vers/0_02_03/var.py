# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 22:18:13 2017

@author: admin
"""

import os
import datetime as dt

app_name = "Zip All"
version = "0.02.03"
build_date = "06-27-2017"

email = "David@DREAM-Enterprise.com"
name = app_name + "  V" + version

#define system varibles
cwd = os.getcwd()
width = 60
lines = 28
cent_width = (width-1)
splash_wait = 5
wait = .5

currdate = dt.date.today().strftime("%Y%m%d")
currtime = dt.datetime.now().strftime("%H%M%S")

#define varibles
folder_bu_base = "!Archive"
folder_bu = folder_bu_base + "-" + currdate + "-" + currtime