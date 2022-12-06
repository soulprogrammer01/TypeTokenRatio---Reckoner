#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Soulprogrammer
"""

import nltk as nlp
import matplotlib.pyplot as plt 
import re

# List to store the TTR values 
TTR_List=[]
#List to store the ID of the article
Article_Number=[]
for counter in range (1,12):
    file=open('Corpus-Collection/'+str(counter)+'.txt','r')
    document=file.read()
    #Remove all special characters using this regex 
    document= re.sub(r'[^\w]', ' ', document)
    #Convert Document to Lower Case
    document=document.lower()
    #Tokenize the document to generate a list of words 
    tokens=nlp.word_tokenize(document)
    #Group the tokens and find the count value of each token and store in dict types.
    types=nlp.Counter(tokens)
    #Find TTR by dividing the length of dict types by length of list tokens 
    TTR= (len(types)/len(tokens))*100 
    print(str(counter)+"\t"+str(TTR))
    #Append TTR to TTR_List 
    TTR_List.append(TTR)
    #Append counter to Article_Number
    Article_Number.append(counter)

# Draw Scatter Plot of Article_Number vs TTR 
plt.scatter(Article_Number,TTR_List)
# Draw Connecting Line Plot of Article_Number vs TTR
plt.plot(Article_Number,TTR_List)
plt.xlabel("Article Number")
plt.ylabel("TTR Score")
plt.show()

