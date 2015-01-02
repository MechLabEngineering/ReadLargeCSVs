# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Reading Large CSV Data

# <codecell>

ftl = 'somerandom1GBsampledata.csv'

# <headingcell level=2>

# Native Python with CSV

# <codecell>

import csv

# <codecell>

#%%timeit -n 1
datacsv = []
with open(ftl, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        datacsv.append(row)

# <headingcell level=2>

# Pandas

# <codecell>

import pandas as pd

# <codecell>

#%%timeit -n 1
datapandas = pd.read_csv(ftl)

# <headingcell level=2>

# Blaze

# <codecell>

from blaze import Data

# <codecell>

!wc -l 'somerandom10GBsampledata.csv'

# <codecell>

# Load a 10GB Data File
data = Data('somerandom10GBsampledata.csv', columns=['UUID','Lat','Lon','Value'])
data

# <codecell>

data['Value'].mean()

# <codecell>


