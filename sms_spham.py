

from gensim import corpora
from collections import defaultdict
import pandas as pd
import re




texts = []
for t in open("data/SmsCollection.csv"):
    # s = re.sub("[^a-zA-Z\ \']+", " ", t)
    texts.append(s)


texts_d = {}
for l in texts:
    key = l[:4]
    value = l[4:]

    if key == "ham;":
        key = key[:3]
    elif key == "spam":
        value = value.strip(";")

    texts_d.setdefault(key, []).append(value)

print(texts_d["ham"])

len(texts_d["ham"])
len(texts_d["spam"])

'''looking good:
the ratio ham:spam is 4827 to 747'''



stoplist = set("for a of the and to in i you is that it have but".split())

# ham List of Lists
ham_lol = [[word for word in text.lower().split() if word not in stoplist]
           for text in texts_d["ham"]]

# spam List of Lists
spam_lol = [[word for word in text.lower().split() if word not in stoplist]
            for text in texts_d["spam"]]

print(len(ham_lol))
print(len(spam_lol))
#ok, numbers check out

# let's print a parsed sample sentence
print(spam_lol[5])
print(ham_lol[5])

# re-build dictionary with parsed sentences
texts_d = {}
texts_d["ham"] = ham_lol
texts_d["spam"] = spam_lol



'''as a specific case of SLPL task, we could be interested in typos and
shorthands commonly used when texting. Let's check if that's the case'''


frequency = defaultdict(lambda: [0, 0, 0])

# count frequency for the words in each category

for k, v in texts_d.items():
    if k == "ham":
        i = 0
    elif k == "spam":
        i = 1
    for sms in v:
        for token in sms:
            frequency[token][i] += 1


# checking absolute words count

sorted_freq_ham = sorted(((value[0], key) for (key, value) in frequency.items()), reverse=1)
sorted_freq_spam = sorted(((value[1], key) for (key, value) in frequency.items()), reverse=1)

print("most and least frequent words for ham over {}:".format(len(sorted_freq_ham)))
print(sorted_freq_ham[:30])
print(sorted_freq_ham[-30:])

print("most and least frequent words for spam: {}".format(len(sorted_freq_spam)))
print(sorted_freq_spam[:30])
print(sorted_freq_spam[-30:])



# printing spam vs total ratio

spam_vs_total_ratio = sorted(((value[1] / sum(value), key) for (key, value) in frequency.items()), reverse=True)

print("most common spam words (spam word count / total count for the same word in the whole dataset")
print(spam_vs_total_ratio[:100])
print("least common spam words against total count")
print(spam_vs_total_ratio[-100:])

"""
most common:
[(1.0, '“harry'), (1.0, '“'), (1.0, '£s'), (1.0, '£900'), (1.0, '£800'), (1.0, '£79'), (1.0, '£750'), (1.0, '£75,000.'), (1.0, '£71.'), (1.0, '£600.'), (1.0, '£54.'), (1.0, '£50award.'), (1.0, '£5000.00'), (1.0, '£5000,'), (1.0, '£5000'), (1.0, '£500.'), (1.0, '£500'), (1.0, '£50-£500.'), (1.0, '£50'), (1.0, '£5/month'), (1.0, '£5'), (1.0, '£400'), (1.0, '£4.50.'), (1.0, '£350!'), (1.0, '£350'), (1.0, '£33:50'), (1.0, '£3/wk'), (1.0, '£3.00'), (1.0, '£3'), (1.0, '£250k'), (1.0, '£250'), (1.0, '£2000'), (1.0, '£200'), (1.0, '£2.50'), (1.0, '£2,000'), (1.0, '£1million'), (1.0, '£1500'), (1.0, '£150'), (1.0, '£1450'), (1.0, '£1250'), (1.0, '£125'), (1.0, '£12'), (1.0, '£1000call'), (1.0, '£1000.'), (1.0, '£1000'), (1.0, '£100,000'), (1.0, '£100'), (1.0, '£10,000'), (1.0, '£10)'), (1.0, '£10'), (1.0, '£1/minmobsmorelkpobox177hp51fl'), (1.0, '£1.50pmmorefrommobile2bremoved-mobypobox734ls27yf'), (1.0, '£1.50pm'), (1.0, '£1.50perwksub'), (1.0, '£1.50perweeksub.'), (1.0, '£1.50ea.'), (1.0, '£1.50/wk.'), (1.0, '£1.50/week.'), (1.0, '£1.50/msg.'), (1.0, '£1.50/msg'), (1.0, '£1.50.'), (1.0, '£1.50'), (1.0, '£1.'), (1.0, '£1,500'), (1.0, '£1'), (1.0, "\x93it's"), (1.0, '\x93harry'), (1.0, 'zouk'), (1.0, 'zed'), (1.0, 'zebra'), (1.0, 'yourinclusive'), (1.0, 'you!to'), (1.0, 'yo-here'), (1.0, 'ymca'), (1.0, 'yesterday!'), (1.0, 'yes-910'), (1.0, 'yes-762'), (1.0, 'yes-440'), (1.0, 'yes-434'), (1.0, 'yes-165'), (1.0, 'yer'), (1.0, 'years,'), (1.0, 'yards'), (1.0, 'yahoo!'), (1.0, 'y87.'), (1.0, 'xxxxxx'), (1.0, 'xxxxx'), (1.0, 'xxxx'), (1.0, 'xxxmobilemovieclub:'), (1.0, 'xxxmobilemovieclub.com?n=qjkgighjjgcbl'), (1.0, 'xxuk'), (1.0, 'xxsp'), (1.0, 'xt'), (1.0, 'xmas?'), (1.0, 'xclusive@clubsaisai'), (1.0, 'xchat.'), (1.0, 'xchat,'), (1.0, 'xafter'), (1.0, 'x49.your'), (1.0, 'x49.')]

least common:
[(0.0, '"you"'), (0.0, '"yeh'), (0.0, '"x"'), (0.0, '"wylie'), (0.0, '"wow'), (0.0, '"woah"'), (0.0, '"with'), (0.0, '"what'), (0.0, '"wen'), (0.0, '"welcomes"'), (0.0, '"walk,'), (0.0, '"walk'), (0.0, '"valued'), (0.0, '"valentines'), (0.0, '"usf'), (0.0, '"ur'), (0.0, '"this'), (0.0, '"thinking'), (0.0, '"the'), (0.0, '"symptoms"'), (0.0, '"sweet"'), (0.0, '"speak'), (0.0, '"song'), (0.0, '"sometimes'), (0.0, '"smokes'), (0.0, '"sleep'), (0.0, '"si.como'), (0.0, '"shit'), (0.0, '"she'), (0.0, '"shah'), (0.0, '"response"'), (0.0, '"power'), (0.0, '"petey'), (0.0, '"pete'), (0.0, '"paths'), (0.0, '"our'), (0.0, '"oh"'), (0.0, '"oh'), (0.0, '"nver'), (0.0, '"not'), (0.0, '"none!nowhere'), (0.0, '"morning"'), (0.0, '"miss'), (0.0, '"me'), (0.0, '"margaret'), (0.0, '"life'), (0.0, '"kudi"yarasu'), (0.0, '"keep'), (0.0, '"julianaland"'), (0.0, '"jeevithathile'), (0.0, '"its'), (0.0, '"it'), (0.0, '"im'), (0.0, '"i;m'), (0.0, '"i'), (0.0, '"hurt'), (0.0, '"how'), (0.0, '"hi'), (0.0, '"hey!'), (0.0, '"hey'), (0.0, '"hello-/@drivby-:0quit'), (0.0, '"hello"'), (0.0, '"hello'), (0.0, '"happy'), (0.0, '"gud'), (0.0, '"gran'), (0.0, '"goodmorning'), (0.0, '"gimme'), (0.0, '"getting'), (0.0, '"get'), (0.0, '"find'), (0.0, '"ey!'), (0.0, '"er,'), (0.0, '"enjoy"'), (0.0, '"drive'), (0.0, '"drink".'), (0.0, '"don\'t'), (0.0, '"cheers'), (0.0, '"checkmate"'), (0.0, '"cha'), (0.0, '"can'), (0.0, '"boost'), (0.0, '"boo'), (0.0, '"best'), (0.0, '"because'), (0.0, '"be'), (0.0, '"aww'), (0.0, '"are'), (0.0, '"alrite'), (0.0, '"alright'), (0.0, '"ah'), (0.0, '"a'), (0.0, '"1.u'), (0.0, '".'), (0.0, '"'), (0.0, '!:-)'), (0.0, '!1'), (0.0, "!!''."), (0.0, '!!!!'), (0.0, '!!')]


This is a good point. This can allow us to take off overall most common words knowing that they're not going to be 
essential in order to set apart spam from ham (ideally we should also check the inverse ratio, but we'll do without it)
"""

# add total count to the 2nd index in the frequency dictionary

for k, v in frequency.items():
    tot = sum(v)
    frequency[k][2] = tot

total_freq_sorted = sorted(((value[2], key) for (key, value) in frequency.items()), reverse=True)

fifty_most_frequent = total_freq_sorted[:50]
print(len(total_freq_sorted))
thousands_least_frequent = total_freq_sorted[-11000]

new_dict = {}

for k, v in texts_d.items():
    for sms in v:
        list = []
        for token in sms:
            if token not in stoplist and token not in fifty_most_frequent:
                if token.isdigit() == False and token not in thousands_least_frequent:
                    list.append(token)
        new_dict.setdefault(k, []).append(list)

print(texts_d)
print(new_dict)

