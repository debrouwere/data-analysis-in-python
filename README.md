Data analysis in Python
=======================

The plan
--------

1. Talk about the advantages of analyzing data in a programming language, as opposed to analyzing data in statistical software or Excel.
2. Explain the basic functionality of pandas, a software library that makes data analysis in Python way more convenient than it would otherwise be.
3. Install Python and pandas on everyone's laptops.
4. Do some exercises! We're going to try and learn a thing or two about the social media response to Edward Snowden's leaks and other revelations. At The Guardian, we call these The NSA Files.

During the first half, you don't have to do anything other than listen. I'll give you all a quick overview of the basic pandas functionality.

During the second half, I will give you a dataset and ask a number of questions you can answer by using that data. Everyone can work at their own pace, and for those of you who don't have Python and pandas installed yet, this is the time to do it. I'll walk around the room to troubleshoot.

One last note before we get started: if things are going a little bit too fast for you, don't worry about it. Nobody can become an expert at this thing in only two hours. I sure didn't. But instead I can give you the names and show you the concepts, so that when next you want to do a data analysis project and you're stuck, you know what to google for.

Where to find things
--------------------

* You will find my introduction to pandas in `OVERVIEW.py.md`.
* You will find the exercises in `EXERCISES.md`.
* The will find answers to the exercises in the `exercises` folder. But try it on your own or ask a neighbor first.

If you're interested in the data: 

* We get raw-ish data from The Guardian's Content API (http://explorer.content.guardianapis.com) and SharedCount (http://www.sharedcount.com/). The fetchers are in `/fetchers/guardian.py` and `/fetchers/shares.py` respectively.
* We do the actual fetching in `/fetchers/__init__.py` which you can call on the command-line... but you don't have to, because we've included the output in the `/data` folder. Otherwise it takes a couple of hours to run.
* We then massage the data a little bit so that it's no longer arbitrary JSON but instead fits into a tabular format. We do this in `munge.py`.
* We then load the munged data in `data.py`. To get to our data set, simply do `from data import articles` in a script or in the REPL.
