# encoding: utf-8

from datetime import date, timedelta
import guardian, shares
import json


def load(dataset, start, stop=None):
    if not stop:
        stop = start + timedelta(days=1)

    days = (stop - start).days

    data = []
    for delta in range(days):
        day = start + timedelta(days=delta)
        iso = day.isoformat()
        filename = 'data/{date}-{dataset}.json'.format(date=iso, dataset=dataset)
        rows = open(filename).read().split('\n')[:-1]
        data += map(json.loads, rows)

    return data


def fetch(begin, days=28):
    for delta in range(days):
        day = begin + timedelta(days=delta)
        iso = day.isoformat()
        # fetch articles
        guardian.fetch(iso)

        # fetch share counts for each article, extracting
        # those articles' urls first
        articles = load('articles', day)
        urls = [article['webUrl'] for article in articles]
        shares.fetch(urls, prefix=iso)


if __name__ == '__main__':
    fetch(date(2013,6,3), days=28)