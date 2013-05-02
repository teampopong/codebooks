#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import pandas as pd

inp = 'cb-administrative-divisions-20100401.csv' # Input filename
outp = 'cb-administrative-divisions-20100401-edited.csv'
df = pd.read_csv(inp, encoding='utf-8')

cb = df.ix[2:, 1:5]
cb.columns = ['code', 'ko', 'en', 'cn']
cb.to_csv(outp, encoding='utf-8', index=False)
