# TypeTokenRatio---Reckoner
A information blog to show the usablitity of the Type-Token-Ratio Measure (TTR) as an introduction to Natural Language Procesing(NLP).
 ##### How to run: 
 
 ``` 
 python TTR_Rec.py
 ```
<div style="text-align:center"><h1>
Lets Start: 
</h1></div>
<Br>

**STEP 1:** 

##### We will have to import our dependencies. 
For this script, we are using fantastic NLP library called [NLTK](https://www.nltk.org/). 

To install NLTK in your terminal, simply type: 

``` bash
pip install nltk 
```

We will then import nltk and  regex by 
``` python
import nltk as nlp 
import re 
```
**STEP 2:**
Declare a string containing our string for which we need to calculate the TTR. 
``` python
document="""Natural language processing (NLP) is the ability of a computer program to understand human language as it is spoken and written -- referred to as natural language. It is a component of artificial intelligence!"""
```
**STEP 3:**
Remove all special characters using this regex.
``` python
document= re.sub(r'[^\w]', ' ', document)
```
**STEP 4:**
Convert Document to Lower Case
```
document=document.lower()
```
Tokenize the document to generate a list of words
```
tokens=nlp.word_tokenize(document)
```
**STEP 5:**
Group the tokens and find the count value of each token and store in dict types.
```
types=nlp.Counter(tokens)
```
 And finally, find the TTR by dividing the length of dict types by length of list tokens
 ```
TTR= (len(types)/len(tokens))*100
print(TTR)
```

##### And it is that simple! You can now use this simple measure to rank the quality of texts! 
