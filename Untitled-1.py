from snownlp import SnowNLP

s1 = r'看看消费水平就知道了，啥也别说了吧？！'
s = SnowNLP(s1)
score = s.sentiments
print(score)



