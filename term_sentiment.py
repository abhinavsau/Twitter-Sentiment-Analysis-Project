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
    absent_word_sentiment_dict = {}
    absent_word_wordcount_dict = {}	

    lines_in_tweet_file = tweet_file.readlines()

    for everyline in lines_in_tweet_file:
        temp_line = json.loads(everyline)
        if 'text' in temp_line:
           tweet_text = temp_line['text']
           tweet_words = tweet_text.split()

           total_sentiment_of_tweet = 0.0
	   word_contributing_to_sentiment = 0.0

           for word in tweet_words:
               if scores.has_key(word):
                  total_sentiment_of_tweet += scores[word]
		  word_contributing_to_sentiment +=1
	   #print(total_sentiment_of_tweet)
           length_of_tweet = len(tweet_words)
           for word in tweet_words:
	       if word not in scores:
		  if word not in absent_word_sentiment_dict:
		       absent_word_sentiment_dict[word]=0.0
		       absent_word_wordcount_dict[word]=0.0
		  absent_word_sentiment_dict[word] += total_sentiment_of_tweet / (length_of_tweet - word_contributing_to_sentiment)
		  absent_word_wordcount_dict[word]+=1

    for word,word_count in absent_word_wordcount_dict.items():
	absent_word_sentiment_dict[word] = absent_word_sentiment_dict[word] / word_count

    for word,word_sentiment in absent_word_sentiment_dict.items():
	print(word.encode("utf-8") + " " + "%.3f" % (word_sentiment))

if __name__ == '__main__':
    main()
