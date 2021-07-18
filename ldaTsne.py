# -*- coding: utf-8 -*-
# author：xuanlong
# 创建：2021-07-18
# 更新：2012-07-18
# 用意：LDA 模块
# ：param fencioutput :分词路径，流式写入分词文件，否则会直接 killed: 9，建议按月写入
# MacOS 无法读取文件时，注意删除.DS_Store文件
        
import numpy as np
import lda

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.manifold import TSNE


fencioutput = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/fenciFolder/Feb.txt'
news = open(fencioutput,'r',encoding='utf-8')

n_topics = 3 # number of topics
n_iter = 200 # number of iterations
n_top_words = 5 # number of keywords we show

stopVcb = open('/Users/xuanlongqin/Documents/data/covid-19/Data/stopWords/cn_stopwords.txt','r',encoding='utf-8')

cvectorizer = CountVectorizer(min_df=5, stop_words=stopVcb)
cvz = cvectorizer.fit_transform(news)

# Lda 模型导入
lda_model = lda.LDA(n_topics=n_topics, n_iter=n_iter)
X_topics = lda_model.fit_transform(cvz)

    
# threshold = 0.6
# _idx = np.amax(X_topics, axis=1) > threshold  # idx of doc that above the threshold
# X_topics = X_topics[_idx]


# a t-SNE model
tsne_model = TSNE(n_components=2, verbose=1, random_state=0, angle=.99, init='pca')

# 20-D -> 2-D
tsne_lda = tsne_model.fit_transform(X_topics)



import bokeh.plotting as bp
from bokeh.plotting import save
from bokeh.models import HoverTool


# 20 colors
colormap = np.array([
    "#1f77b4", "#aec7e8", "#ff7f0e", "#ffbb78", "#2ca02c",
    "#98df8a", "#d62728", "#ff9896", "#9467bd", "#c5b0d5",
    "#8c564b", "#c49c94", "#e377c2", "#f7b6d2", "#7f7f7f",
    "#c7c7c7", "#bcbd22", "#dbdb8d", "#17becf", "#9edae5"
])

_lda_keys = []
for i in range(X_topics.shape[0]):
  _lda_keys +=  X_topics[i].argmax(),

topic_summaries = []
topic_word = lda_model.topic_word_  # all topic words
vocab = cvectorizer.get_feature_names()
for i, topic_dist in enumerate(topic_word):
  topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words + 1):-1] # get!
  topic_summaries.append(' '.join(topic_words)) # append!

title = 'Feb.2020 - LDA cluster topics - topic 7 - no threshold'
num_example = X_topics.shape[0]

plot_lda = bp.figure(plot_width=1400, plot_height=1100,
                     title=title,
                     tools="pan,wheel_zoom,box_zoom,reset,hover",
                     x_axis_type=None, y_axis_type=None, min_border=1)

plot_lda.scatter(x=tsne_lda[:, 0], y=tsne_lda[:, 1],
                 color=colormap[_lda_keys][:num_example]
                #  source=bp.ColumnDataSource({
                #    "content": news[:num_example],
                #    "topic_key": _lda_keys[:num_example]
                #   })
                )


# randomly choose a news (within a topic) coordinate as the crucial words coordinate
topic_coord = np.empty((X_topics.shape[1], 2)) * np.nan
for topic_num in _lda_keys:
  if not np.isnan(topic_coord).any():
    break
  topic_coord[topic_num] = tsne_lda[_lda_keys.index(topic_num)]


# plot crucial words
for i in range(X_topics.shape[1]):
  plot_lda.text(topic_coord[i, 0], topic_coord[i, 1], [topic_summaries[i]])

# hover tools
hover = plot_lda.select(dict(type=HoverTool))
hover.tooltips = {"content": "@content - topic: @topic_key"}

# save the plot
save(plot_lda, '{}.html'.format(title))






