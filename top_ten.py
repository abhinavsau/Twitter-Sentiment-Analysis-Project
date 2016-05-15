import sys
import json
import operator

def main():
    tweet_file = open(sys.argv[1])
    
    hashtag_count_dict = {}
    lines_in_tweet_file = tweet_file.readlines()

    for everyline in lines_in_tweet_file:
        temp_line = json.loads(everyline)
	if 'entities' in temp_line:
	   ht = temp_line["entities"]["hashtags"]
	   for every_hashtag in ht:
               ht_text = every_hashtag["text"]
	       if hashtag_count_dict.has_key(ht_text):
	          hashtag_count_dict[ht_text]+=1
	       else:
		  hashtag_count_dict[ht_text]=1

    
    sorted_hashtag_count_dict = sorted(hashtag_count_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    for i in range(0,10):
	print(sorted_hashtag_count_dict[i][0] + " " + str(sorted_hashtag_count_dict[i][1]))

if __name__ == '__main__':
    main()
