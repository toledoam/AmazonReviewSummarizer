### Amazon Review Summarizer


import os
import json
import nltk
from tfidf import calculate_tfidf
from read_data import load_data

#data = [json.loads(line) for line in open('C:/Users/Ben Fresh/Documents/GitHub/AmazonReviewSummarizer/reviews_Musical_Instruments_5.json', 'r')]



product_dict = load_data()
product_list = sorted(product_dict.keys(), reverse = True) # sort descending order by num reviews
for productID in product_list:
        print('productID: ' + productID + '\n')
        tfidfs = calculate_tfidf(product_dict[productID])
        for reviewerID, tfidf in tfidfs.items():
                print('reviewerID: ' + reviewerID)
                threshold = sum(tfidf.values())/len(tfidf)
                sorted_tfidf = sorted([(k,v) for k,v in tfidf.items() if v > threshold], key=lambda x: -x[1]) #excludes term if tfidf is below threshold
                for x in sorted_tfidf:
                        print(x)
                print()
        break                                                       #stops after first product

