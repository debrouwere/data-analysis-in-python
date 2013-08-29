"""
Using `pandas` to analyze data in Python
======================================

Python has become one of the most-used scripting languages in the scientific community, 
and as a result, you'll find many, many libraries for doing calculations and transformations 
on all sorts of data. But when it comes to everyday data analysis and statistics, there's 
really only one way to go: Wes McKinney's [pandas](http://pandas.pydata.org/). So pandas is 
what we'll be exploring in this workshop.

There's a section at the very bottom that'll tell you how you can install Python and pandas 
and get the data you need to do the exercises. But let's start with an overview and some 
examples first.

To start with, let's load our data! (This'll take from 15 seconds to a minute.)
"""

from data import articles

"""
Let's explore a little bit.

* What columns does our dataset have.
* Can you give some example values?
* How about some summary statistics, like the mean or something?

(In a shell, you don't need to `print` this but can just type 
e.g. `articles.columns` to find out this information.)
"""

# available columns, explicitly
print articles.columns
# ... and then implicitly
print articles

# how about some example values, explicitly (with head and tail)...
print articles['fields-headline'].head()
print articles['section-name'].head()
print articles['twitter'].head()
print articles['twitter'].tail()
# ... and then implicitly
print articles['twitter']

"""
Counting is pretty easy.
"""

count = articles['url'].count()
tweets = articles['facebook-like-count'].sum()
print count, "articles published in 28 days"
print tweets, "tweets and retweets about Guardian stories published during that period"

"""
Sometimes, values are missing. It's pretty easy to spot, and also 
pretty easy to correct for.

When you calculate basic statistics, pandas will take care of it for you.
Otherwise, you can use `#dropna()`.
"""

print articles['twitter']
print len(articles['twitter'])
print len(articles['twitter'].dropna())
# you can also take the subset of rows that has 
# both valid twitter *and* facebook-likes values.
print len(articles.dropna(subset=['twitter', 'facebook-likes']))

# are any of the rows empty for certain columns?
edition = articles['fields-newspaper-edition-date']
print '% of articles also in print', float(len(edition.dropna())) / len(edition)

"""
How about some easy plots? Try this in an IPython shell.

    ipython qtconsole --pylab=inline

"""

articles['twitter'].hist(bins=range(0, 500, 50))

"""
From the histogram, you can see how many articles have more 
than 500 tweets, but maybe you want to know exactly. You can, 
by filtering.
"""

popular = articles[articles['twitter'] > 500]
print len(popular)

# Give some examples...
print popular['fields-headline'].head()

"""
Often, we want to group data by certain criteria. Those criteria can be 
existing columns... or we can make a new column ourselves.
"""

from dateutil.parser import parse as dateparse
articles['dow'] = articles['web-publication-date'].apply(lambda d: dateparse(d).weekday())
# this means: group articles by day, then make a sum of all the tweets per day, 
# and then put that on a plot
articles.groupby('dow')['twitter'].sum().plot()

"""
Here's that same example in plain Python. You'll see two things: 

    (1) nothing about this code is particularly hard
    (2) ... but it does get really cumbersome, really fast
"""

from pprint import pprint
import numpy as np

dow = {}

for ix, article in articles.iterrows():
    day = dateparse(article['web-publication-date']).weekday()
    tweets = article['twitter']

    if tweets is np.nan:
        tweets = 0

    dow.setdefault(day, []).append(tweets)

for day, counts in dow.items():
    dow[day] = sum(counts)

pprint(dow)

"""
Sometimes you get data in a stupid format. Like word counts as strings instead of integers.
But that's easy to fix.
"""

# Word counts as strings? That's absurd.
articles['fields-wordcount'] = articles['fields-wordcount'] \
    .dropna() \
    .map(lambda c: int(c))

# And now let's turn it into a histogram.
articles['fields-wordcount'].hist()

"""
I wonder, to what extent is the newspaper really "yesterday's news"?
"""

# some simple calculations
# To what extent is the newspaper really yesterday's news?
in_print = articles.dropna(subset=['fields-newspaper-edition-date'])

from dateutil.parser import parse as dateparse

def calculate_delta(row):
    web = dateparse(row['web-publication-date']).date()
    printed = dateparse(row['fields-newspaper-edition-date']).date()
    delta = printed - web
    return delta.days

# axis=0 means "column by column", axis=1 means "row by row"
delay = in_print.apply(calculate_delta, axis=1)

# as we can see, in some cases something is in print one or two 
# days before it shows up online, but usually the web is one 
# or two days ahead
delay.hist(bins=range(-4, 5))


"""
Some other simple calculations around word counts.
"""

count = lambda s: len(s.split())
wordcount_titles = articles['fields-headline'].map(count)
cast = lambda c: int(c)
wordcount_articles = articles['fields-wordcount'] = articles['fields-wordcount'].dropna().map(cast)

AVG_WORD_LENGTH = 5
charcount_articles = wordcount_articles * AVG_WORD_LENGTH

# histogram!
charcount_articles.hist(bins=range(0, 10000, 250))

# how many articles were published with fewer than 100 words?
# (but let's ignore those with absurdly small word counts because
# those are probably wrong)
realistic = articles[articles['fields-wordcount'] > 10]
short = realistic[realistic['fields-wordcount'] < 100]
print len(short)

"""
And sometimes plain old Python saves the day, as it does here 
with its built-in Counter data structure.

Let's try to figure out which tags are most common.
"""

# what tags are most common?

from collections import Counter
tags = (articles['tags'] + ', ').sum().split(', ')
counts = Counter(tags)

# hey, and we have day of the week from a previous exercise!
articles['about-sports'] = articles['tags'].map(lambda t: 'sport' in t)
sports_articles = articles[articles['about-sports'] == True]
count = sports_articles.groupby('dow')['url'].count()

# Think about what exactly this is doing: it will divide the sport story 
# count for each day against the total story count for each day, creating 
# seven averages / means, and then it will multiply them by 100, turning
# each number into a percentage. So you're doing many different calculations
# with almost no code whatsoever.
normalized_count = count.map(float) / articles.groupby('dow')['url'].count() * 100

# and why not plot this...
normalized_count.plot(kind='bar')