News Reader
===========

This document shows how to implement a simple news reader using Ray. The reader
consists of a simple Vue.js `frontend`_ and a backend consisting of a Flask
server and a Ray actor. View the `code for this example`_.

To run this example, you will need to install NPM and a few python dependencies.

.. code-block:: bash

  pip install atoma
  pip install flask


To use this example you need to

* Start the server with ``python server.py``
* Clone the client code with ``git clone https://github.com/ray-project/qreader``
* Start the client with ``cd qreader;  npm install; npm run dev``
* You can now add a channel by clicking "Add channel" and for example pasting
  ``http://news.ycombinator.com/rss`` into the field.
* Star some of the articles and dump the database with ``sqlite3 newsreader.db``
  and enter ``SELECT * FROM news;``.

.. _`frontend`: https://github.com/saqueib/qreader
.. _`code for this example`: https://github.com/ray-project/ray/tree/master/examples/newsreader


Training the model
------------------

In the ``examples/newsreader`` folder, run the following:

.. code-block:: bash

  wget https://archive.org/download/14566367HackerNewsCommentsAndStoriesArchivedByGreyPanthersHacker/14m_hn_comments_sorted.json.bz2


Let's first have a look at the top comments:

.. code-block:: python

  import pandas as pd
  import training

  records = training.load_hn_submissions("14m_hn_comments_sorted.json.bz2")

  df = pd.DataFrame(records, columns=["title", "score"])
  df.sort_values(by="score", ascending=False)

Which will output the following:

.. code-block

  title  score
  595312                         Steve Jobs has passed away.   4339
  753452                       Show HN: This up votes itself   3536
  1545633                                 Tim Cook Speaks Up   3086
  1359046                                               2048   2903
  1079441                                                      2751
  1191375                           Don't Fly During Ramadan   2744
  763347                                                       2738
  1182593                                          Hyperloop   2666
  754294    Poll: What's Your Favorite Programming Language?   2423
  1556451  Microsoft takes .NET open source and cross-pla...   2376


We can get the 0.7 quantile of scores by evaluating

.. code-block:: python

  df['score'].quantile(0.7)

which outputs 2.0, so having 2 comments is a good cutoff.

.. code-block:: python

  datapoints = training.create_vowpal_wabbit_records(records, cutoff=2.0)

  with open("features.vw", "w") as f:
      for line in datapoints:
          f.write(line + "\n")

The model can now be trained with

.. code-block:: bash

  vw features.vw --binary -f hackernews.model


We need to install VowpalWabbit with (this does not work on Python 3.7)

.. code-block::bash

  sudo apt-get install libboost-python-dev
  pip install vowpalwabbit

learn_model(datapoints)
