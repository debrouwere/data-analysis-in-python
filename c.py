from data import articles

articles['is-nsa'] = articles.apply(lambda a: 'nsa' in a['tags'], axis=1)
nsa_files = articles[articles['is-nsa'] == True]

# how big the impact
float(nsa_files['facebook-share-count'].sum()) / articles['facebook-share-count'].sum()