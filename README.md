# Approach

After splitting the input text into sentences using regular expressions, I used the pre-trained sentiment analyzer VADER from the Natural Language Toolkit (NLTK) in order to analyze each sentence. I took the "compound" value from each analysis, which is a score from -1 to 1 that summarizes the values for negative, neutral, and positive sentiment. Finally, I took the weighted average of the sentiment scores based on the number of characters in each sentence, which gave me a score for the input text as a whole.

# Conclusion

The average sentiment score of the input text is about 0.366, where a value closer to -1 represents negative sentiment and a value closer to 1 represents positive sentiment. This means that the text has an overall positive sentiment. You can view the sentiment scores for each sentence in [sentiment_scores.txt](/sentiment_scores.txt).

When I first read the input text, I predicted that its sentiment would be a bit closer to negative, just based off the general negative tone the text gave off to me, especially in the first paragraph. For example, two excerpts that stand out from this paragraph include `You towered with rage, yelled quotes at me.` and `Carcasses bleed at the sight of the murderer`. However, the second paragraph does spend a lot of time on the topic of the many good qualities of some man, which could contribute in the positive direction to the text's sentiment.

I decided to visualize this shift in sentiment using a scatterplot graph, where the x-axis represents how far along in the text each sentence is and the y-axis represents the score of each sentence.

![scatterplot of sentence position versus sentiment score](/scatterplot.png)

As the figure shows, the sentiment scores towards the end of the text are much more positive than those earlier in the text, and so we can conclude it's primarily the second paragraph which brings the overall sentiment score up.

# Evaluation

One issue with my approach is that VADER was not trained for sentences from fictional literature, but rather short texts from social media. This could lower the accuracy of the sentiment evaluations because that the model isn't used to the kind of language used in literature. One way to improve this aspect of my approach could be to develop and train my own sentiment analyzer using a corpus of older fiction.

# Resources Used

- [Matplotlib – matplotlib.pyplot.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)
- [Real Python – Sentiment Analysis: First Steps With Python's NLTK Library](https://realpython.com/python-nltk-sentiment-analysis)
- [Real Python – Working With Files in Python](https://realpython.com/working-with-files-in-python/)
- [Regular-Expressions.info – Lookahead and Lookbehind Zero-Length Assertions](https://www.regular-expressions.info/lookaround.html)
