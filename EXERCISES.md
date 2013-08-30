### A. How many articles did we publish about Snowden?

* This will make your life easier: `articles['is-nsa'] = articles.apply(lambda a: 'nsa' in a['tags'], axis=1)`
* Test for articles['is-nsa'] to be True. You can do so using the `articles[articles[myfield] < myvalue]` syntax.
* And to give yourself an easy way to refer to that subset, you can assign it to a variable with `nsa = articles[articles[myfield] < myvalue]`
* Now that you have the subset, count how many articles it contains.
* Give some example titles for articles about Snowden.

### B. How did interest in the NSA Files change over time?

* You can't group by date on the dataset because the dates look like `2013-06-17T10:30:17Z`.
* Instead, you'll want to simplify those dates first so you *can* group on them.
  Hint: `articles['date'] = articles['web-publication-date'].map(lambda d: d[:10])`
* On the filtered dataset, group by date, sum up the tweets and tadaah.
* With that information, create a nice little plot. In pandas you can always chain things, so just sticking `.plot()` on the end should work.
* How about `.plot(kind='bar')`?
* Can you spot any changes in social sharing *after* it was known Snowden was the leak, which was on June 9?

### C. How big were The NSA Files for the Guardian during that first month?

* What percentage of social sharing was about Snowden?
* What percentage... split out by day? Hint: you can multiply or divide one dataset by another, say, the dataset with tweetcounts about Snowden versus the dataset with all tweetcounts.
* How did the Tweet counts compare to Facebook counts? Can you give a "tweet counts as a percentage of facebook counts?