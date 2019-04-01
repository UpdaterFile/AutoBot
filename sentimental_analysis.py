#import pycorenlp
from pycorenlp import StanfordCoreNLP

#download stanfordnlp
#https://stackoverflow.com/questions/32879532/stanford-nlp-for-python

def get_sentiment(nlp, text):
    sentence = nlp.annotate(text, properties={
        'annotators': 'sentiment',
        'outputFormat': 'json',
        'timeout': 1000,
    })
    sentiment = 0

    for s in sentence["sentences"]:
        if s["sentiment"] == "Positive": 
            sentiment += 1
        elif s["sentiment"] == "Negative":
            sentiment -= 1

    if(sentiment >= 1):
        return "Positive"
    else:
        return "Negative"

#nlp = StanfordCoreNLP('http://localhost:9000')
'''
s = get_sentiment(StanfordCoreNLP('http://localhost:9000'),"I'm good, How are you?")
print(s)

'''
