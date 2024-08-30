import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('social_media_sentiment_data.csv')

sentiment_counts = df['Sentiment'].value_counts()

plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color=['lightgreen', 'salmon', 'lightblue'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Posts')
plt.show()
