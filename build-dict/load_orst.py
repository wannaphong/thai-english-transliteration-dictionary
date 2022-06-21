import pandas as pd
import os
from pythainlp.util import isthaichar

_df = pd.read_csv(os.path.join('.','orst','orst.csv'))

orst_dict = [(i,j,k) for i,j,k in list(zip(_df['th'],_df['en'],[True]*len(_df['th']))) if isthaichar(i[0]) and 'acid' not in j]