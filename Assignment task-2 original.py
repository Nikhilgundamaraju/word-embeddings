Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> sentences = nltk.corpus.brown.sents()
>>> len(sentences)
57340
>>> sentences[0]
['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', 'Friday', 'an', 'investigation', 'of', "Atlanta's", 'recent', 'primary', 'election', 'produced', '``', 'no', 'evidence', "''", 'that', 'any', 'irregularities', 'took', 'place', '.']
>>> import gensim.downloader as api
>>> wv= api.load("word2vec-google-news-300")
>>> from gensim import models
>>> my_wv=models.Word2Vec(sentences,sg=1,vector_size=30,window=10,min_count=10,epochs=10)
>>> my_wv1=models.Word2Vec(sentences,sg=0,vector_size=60,window=20,min_count=20,epochs=20)
>>> import A1_helper
>>> x_vals, y_vals, labels = A1_helper.reduce_dimensions(my_wv.wv)
>>> A1_helper.plot_with_matplotlib(x_vals, y_vals, labels, ["An", "another", "an", "Another", "this", "take", "taken", "gave", "came", "taking", "says", "added", "noted", "explained", "stressed", "no", "Any", "or", "not", "nor"])
Plotting An at 1.8695253 22.978155
Plotting another at -0.6413935 23.38933
Plotting an at 0.8720877 23.494522
Plotting Another at 2.2196515 23.014042
Plotting this at -13.850099 13.134224
Plotting take at 44.945362 8.075911
Plotting taken at -3.0744183 -15.913337
Plotting gave at 23.20987 8.9906645
Plotting came at 53.139996 34.966362
Plotting taking at 25.277193 11.09386
Plotting says at 50.150963 -11.907098
Plotting added at 0.26553884 37.88997
Plotting noted at -25.098969 36.704144
Plotting explained at 26.522367 -14.286094
Plotting stressed at -19.384125 -13.770209
Plotting no at 2.133491 18.981583
Plotting Any at -1.7997825 19.961798
Plotting or at -3.2558246 20.753105
Plotting not at 1.2881984 15.464321
Plotting nor at 2.9904623 -4.148773
>>> x_vals, y_vals, labels = A1_helper.reduce_dimensions(my_wv1.wv)
>>> A1_helper.plot_with_matplotlib(x_vals, y_vals, labels, ["An", "another", "an", "Another", "this", "take", "taken", "gave", "came", "taking", "says", "added", "noted", "explained", "stressed", "no", "Any", "or", "not", "nor"])
Plotting An at -4.730792 -26.971724
Plotting another at -40.96527 14.208722
Plotting an at -8.483409 -11.204018
Plotting Another at -4.680915 -26.567764
Plotting this at 14.344465 -7.044216
Plotting take at 32.75515 -35.19494
Plotting taken at -43.775013 -10.844067
Plotting gave at -48.709023 -22.463377
Plotting came at -45.46538 -23.986027
Plotting taking at -11.267838 2.3512766
Plotting says at -29.993338 0.15955889
Plotting added at -35.030544 1.9066079
Plotting noted at -1.0042919 18.28619
Plotting explained at -34.237762 -3.9347825
Plotting stressed at 16.913795 6.845564
Plotting no at -10.968166 -10.340015
Plotting Any at 1.5131973 -17.742235
Plotting or at -12.029183 -22.5356
Plotting not at -10.672661 -11.896759
Plotting nor at 3.5543559 -16.679346
>>> 
