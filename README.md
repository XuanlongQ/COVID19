# COVID19
difference between media reports and netizen comments

# 概述
该Repository主要是数据后处理模块，用于对爬取后的新浪新闻进行相关的后处理，后处理模块包含 聚类分析模块 与 情感分析模块
- 聚类分析模块集成使用 LDA 算法。
  - [Introduction to topic model（Blei2012）](https://www.cnblogs.com/siegfang/archive/2013/01/30/2882391.html)
  - 赵鑫 ，李晓明．主题模型在文本挖掘 中的应用JR3．PKU-CSNCIS-TR2011Xx．June2011
- 情感分析模块集成使用 中文情感分词工具 [SnowNLP](https://github.com/isnowfy/snownlp)

*1、源数据请参考 [SinaNewsCrawler](https://github.com/XuanlongQ/SinaNewsCrawler/tree/master)，本文暂不开源，不支持引用*

*2、macOS 使用提前删除“.DS_Store”文件*

# 文件描述
文件功能请参见注释：
- basicProcess.py:执行后，评论即可获得情感值。
- cutPaper.py:执行后，文章即可获得分类、序号、情感值。
- gloPath.py:定义了几个关键路径。
- ldaAlg.py:LDA主题聚类模型，需要输入分词文件，分词方式参考cutPaper.cutWords函数。
- ldaTsne.py:LDA XD->2D 作图。
- sampleFile.py:采样文件，需要人工采样确认准确性。
- statistic.py:对加工后的数据进行统计。

