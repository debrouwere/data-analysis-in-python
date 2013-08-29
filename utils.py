# encoding: utf-8

"""
Utilities for normalizing column names, which is useful 
when you're using data from different data sources, 
all with their own naming conventions.
"""

import re
import math
import collections

def normalize_name(name, separator='-'):
    name = re.sub(r'([a-z])([A-Z])', r'\1-\2', name)
    return name \
        .replace(' ', separator) \
        .replace('_', separator) \
        .replace('-', separator) \
        .lower()

def normalize_columns(df, separator='-'):
    names = [normalize_name(name, separator) for name in df.columns]
    df.columns = names
    return df

"""
JSON can be arbitrarily nested, but tables and data frames are 
two-dimensional: there's columns and rows. This function can 
"flatten" a dictionary until it's essentially a table.
"""

def flatten(d, parent_key='', connector='-'):
    items = []
    for k, v in d.items():
        new_key = parent_key + connector + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, connector).items())
        else:
            items.append((new_key, v))
    return dict(items)

"""
Data structures with primary keys are easier for Pandas to work with.
"""

# turn array into a keyed data structure
def index_by(list, index):
    hash = {}
    for el in list:
        name = el[index]
        hash[name] = el
    return hash