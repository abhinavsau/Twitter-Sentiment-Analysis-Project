import sys
import json
#import operator

us_states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


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
    
    sentiment_per_state = {}
    tweets_per_state = {}

    lines_in_tweet_file = tweet_file.readlines()

    for everyline in lines_in_tweet_file:
        temp_line = json.loads(everyline)
	if 'text' in temp_line:
	    tweet_text = temp_line['text']
	    tweet_words = tweet_text.split()
            sentiment_score = 0.0

            for word in tweet_words:
               if scores.has_key(word):
                  sentiment_score += scores[word]

        if 'place' in temp_line:
           tweet_place = temp_line['place']
	   if tweet_place is not None and ((tweet_place["country_code"] == "US") or (tweet_place["country"] == "United States")) : 
	       if tweet_place["full_name"] is not None:
	          city,state = tweet_place["full_name"].split(", ")
	          if us_states.has_key(state):
                      if state not in sentiment_per_state:
		         sentiment_per_state[state] = 0.0
		         tweets_per_state[state] = 0.0
		      sentiment_per_state[state] += sentiment_score
		      tweets_per_state[state] += 1
        #calculate average sentiment per state - state sentiment score divided by total number of tweets

	
    for state,tweet_count in tweets_per_state.items():
       sentiment_per_state[state] = sentiment_per_state[state] / tweet_count
    
    #print(max(sentiment_per_state.iteritems(), key=operator.itemgetter(1))[0])
    happiest_score = 0.0
    happiest_state = ""

    for state,sentiment_score in sentiment_per_state.items():
        if sentiment_score > happiest_score:
            happiest_score = sentiment_score
            happiest_state = state
    print(happiest_state)

if __name__ == '__main__':
    main()
