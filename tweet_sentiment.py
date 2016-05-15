import sys
import json

def affin_dict(scores,sent_file):
    afinnfile = sent_file.readlines()
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    affin_dict(scores,sent_file)

    lines_in_tweet_file = tweet_file.readlines()

    for everyline in lines_in_tweet_file:
        temp_line = json.loads(everyline)
        if 'text' in temp_line:
           tweet_text = temp_line['text']
           tweet_words = tweet_text.split()
           sentiment_score = 0
           for word in tweet_words:
               if scores.has_key(word):
                  sentiment_score += scores[word]
	   print(sentiment_score)
        

if __name__ == '__main__':
    main()
