import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import re

with open("input.txt","r") as myFile:
	myInput = myFile.read()

#Replace all the new lines in the input file with spaces, fix double spaces, and split the text into a list of sentences.
cleanInput = re.sub("\n"," ",myInput)
cleanInput = re.sub("  "," ",cleanInput)
sentences = re.split("(?<!Dr\.|Mr\.)(?<=[\.\!\?\;\:])[ \"\']+",cleanInput)

#For each sentence from the input file, compute a sentiment score from -1 (negative sentiment) to +1 (positive sentiment) and put the scores into a list. Also, store the length of each sentence in another list.
scores = []
lengths = []
for sentence in sentences:
	lengths.append(len(sentence))
	score = SentimentIntensityAnalyzer().polarity_scores(sentence)
	scores.append(score["compound"])

#Multiply each sentiment score by the length of the corresponding sentence.
weightedScores = []
for i in range(len(scores)):
	weightedScore = scores[i] * lengths[i]
	weightedScores.append(weightedScore)

#Find the weighted average of the sentiment scores.
averageScore = sum(weightedScores) / sum(lengths)

print(averageScore)

#Create a list of the sentences next to their corresponding sentiment scores.
sentimentScores = open("sentiment_scores.txt","w")
lines = []
for i in range(len(sentences)):
	lines.append(str(scores[i]) + "\t" + sentences[i] + "\n")
sentimentScores.writelines(lines)
sentimentScores.close()

#Create a scatterplot of the position of each sentence versus its sentiment score.
scatter_x = []
i = 0
for length in lengths:
	scatter_x.append(i)
	i += length
scatter_y = scores
plt.scatter(scatter_x,scatter_y)
plt.show()