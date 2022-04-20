#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:50:42 2022

@author: pashamadwani
"""

import pandas as pd
import os



file1 = r'/Users/pashamadwani/PAPractice/python_projects/med_insurance_proj/archive/BusinessRules.csv'


dfFile1 = pd.read_csv(file1,sep = ',')

for i in dfFile1.columns:
    if str(dfFile1[i][0]).isnumeric() == False:
        print(i,' : ', dfFile1[i].unique())