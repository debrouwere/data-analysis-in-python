from articles import data

# add some extra columns to our data set
articles['is-nsa'] = articles.apply(lambda a: 'nsa' in a['tags'], axis=1)
articles['date'] = articles['web-publication-date'].map(lambda d: d[:10])
# filter down
nsa_files = articles[articles['is-nsa'] == True]
# get those tweet counts
nsa_files.groupby('date')['twitter'].sum()
# and plot them
# as you can see, when Snowden revealed himself that caused a huge spike
nsa_files.groupby('date')['twitter'].sum().plot(kind='bar')

# and here's the article responsible for that
top = nsa_files.sort(columns=['twitter'])
top.tail()['web-title']
# or...
top.ix[-1]