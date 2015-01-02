# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import numpy as np

# <codecell>

%matplotlib inline
import matplotlib.pyplot as plt

# <headingcell level=2>

# Timings to read CSV files

# <markdowncell>

# MacBook Pro, 2.5GHz Intel Core i5, 8GB 1600MHz DDR3-RAM, SSD

# <codecell>

zehnMB={}
zehnMB['CSV'] = 0.196
#zehnMB['numpy'] = 1.73
zehnMB['Pandas'] = 0.241
zehnMB['Blaze'] = 0.012

# <codecell>

hundertMB={}
hundertMB['CSV'] = 1.97
#hundertMB['numpy'] = 17.9
hundertMB['Pandas'] = 2.4
hundertMB['Blaze'] = 0.012

# <codecell>

einGB={}
einGB['CSV'] = 34.4
#einGB['numpy'] = 354.0
einGB['Pandas'] = 25.7
einGB['Blaze'] = 0.012

# <codecell>

timings = pd.DataFrame.from_dict([zehnMB, hundertMB, einGB])
timings.index = pd.Index(['10MB', '100MB', '1GB'], name='CSV File Size')
timings

# <codecell>

timings.T.plot(kind='bar', title='Read CSV files with different Python modules', logy=True, ylim=(1e-3, 1e2))
plt.xlabel('read time from SSD in [s]')

# <codecell>

timings.plot(kind='bar', title='Read CSV files with different Python modules', logy=True, ylim=(1e-3, 1e2))
plt.ylabel('read time from SSD in [s]')
plt.savefig('read-CSV-from-Disc-Blaze-CSV-Pandas-Python.png', dpi=150, bbox_inches='tight')

# <codecell>

timings.plot(logy=True)
plt.legend(loc=2)
plt.title('Read CSV files with different Python modules')
plt.ylabel('read time from SSD in [s]')

# <codecell>


