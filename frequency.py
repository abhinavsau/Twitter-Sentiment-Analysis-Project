import sys
import json

def main():

    tweet_file = open(sys.argv[1])
    word_freq_dict = {}	
    global_word_count = 0.0
    lines_in_tweet_file = tweet_file.readlines()

    for everyline in lines_in_tweet_file:
        temp_line = json.loads(everyline)
        if 'text' in temp_line:
           tweet_text = temp_line['text']
           tweet_words = tweet_text.split()

           for word in tweet_words:
               if word not in word_freq_dict :
                  word_freq_dict[word]=0.0
               word_freq_dict[word]+=1
	       global_word_count+=1

    for word,word_freq in word_freq_dict.items():
	word_freq_dict[word] = word_freq / global_word_count

    for word,word_freq in word_freq_dict.items():
	print(word.encode("utf-8") + " " + "%.4f" % (word_freq))

if __name__ == '__main__':
    main()
