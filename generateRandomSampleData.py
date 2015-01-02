# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import uuid
import random
import os
import numpy as np

# <codecell>

# name the file
outfile = 'somerandom10MBsampledata.csv'

outsize = 10 # MB
chunksize = 1000

# <markdowncell>

# This will generate the random sample csv data in following format:
# 
# c77b0056-7f10-41b0-9aa2-f714f0e5a3eb,12.124733,19.329938,506

# <codecell>

with open(outfile, 'wb') as csvfile:
    while (os.path.getsize(outfile)//1024**2) < outsize:
        data = [[uuid.uuid4() for i in range(chunksize)],
                np.random.random(chunksize)*50,
                np.random.random(chunksize)*50,
                np.random.randint(1000, size=(chunksize,))]
        csvfile.writelines(['%s,%.6f,%.6f,%i\n' % row for row in zip(*data)])

# <codecell>


