from data import articles

articles['is-nsa'] = articles.apply(lambda a: 'nsa' in a['tags'], axis=1)

# how many stories
nsa_files = articles[articles['is-nsa'] == True]
float(len(nsa_files)) / len(articles)