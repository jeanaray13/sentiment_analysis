#Import Libraries
from classifier import *
import pandas as pd
import matplotlib.pyplot as plt

#Sentiment Classifier in Spanish (spanish_sentiment_analysis)
clf = SentimentClassifier()

df = pd.read_csv('FILE.csv')
message = df['msg']
message = message.to_numpy()

value = []
for e in message:
    value.append(clf.predict(e))

df['value'] = value

print('--------------------------')
print('Saving result in a csv file')
print('--------------------------')
df.to_csv('result.csv')

#Bar Chart
negative = df[df['value']<=0.3]['value'].count()
neutral = df[(df['value']>0.3) & (df['value']<0.6)]['value'].count()
positive = df[df['value']>=0.6]['value'].count()

plt.bar('Negative',negative,label='Negative',color='red')
plt.bar('Neutral',neutral,label='Neutral',color='gray')
plt.bar('Positive',positive,label='Positive',color='green')
plt.title('Sentiment chart')
plt.ylabel('Count')
plt.xlabel('Category')
plt.show()