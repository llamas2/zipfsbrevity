## Open in colab: https://colab.research.google.com/drive/1z1OpLn5DFvPwwKyIDNybRd_Gx9AdXVqi?usp=sharing ##
##**Does Zipf’s Law of Abbreviation holds for (i) a particular genre of text in English that is not a novel?**

print("Does Zipf’s Law of Abbreviation holds for a particular genre of text in
    English or German that is not a novel?")

#### ENGLISH ESSAYS ####
## Essay 1: Essays by Ralph Waldo Emerson by Ralph Waldo Emerson
## Essay 2: Essays of Michel de Montaigne — Complete by Michel de Montaigne
## Essay 3: Essays of Schopenhauer by Arthur Schopenhauer
## Essay 4: Bacon's Essays, and Wisdom of the Ancients by Francis Bacon
## Essay 5: How to Tell a Story, and Other Essays by Mark Twain

urlsEN={"https://www.gutenberg.org/ebooks/16643.txt.utf-8",
      "https://www.gutenberg.org/files/3600/3600-0.txt",
      "https://www.gutenberg.org/files/11945/11945-0.txt",
      "https://www.gutenberg.org/files/56463/56463-0.txt",
      "https://www.gutenberg.org/files/3250/3250-0.txt"
      }

#### GERMAN ESSAYS ####
## Essay 1: Gesichte: Essays und andere Geschichten by Else Lasker-Schüler
## Essay 2: Das österreichische Antlitz: Essays by Felix Salten
## Essay 3: Handbuch der deutschen Kunstdenkmäler, Bd.1, Mitteldeutschland, 1914 by Georg Dehio
## Essay 4: Deutsche Literaturgeschichte in einer Stunde by Alfred Henschke
## Essay 5: Die Organisation der Rohstoffversorgung by Walther Rathenau

urlsDE={"https://gutenberg.org/ebooks/53239.txt.utf-8",
          "https://gutenberg.org/files/53713/53713-0.txt",
          "https://gutenberg.org/files/19460/19460-0.txt",
          "https://gutenberg.org/ebooks/22517.txt.utf-8",
          "https://gutenberg.org/files/21031/21031-0.txt"
        }

#### LIBRARIES & PACKAGES ####

import urllib.request #to open and read the urls
import nltk
nltk.download("punkt") #to tokenize the text in German
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
import matplotlib.pyplot as plt #to plot the results in a graph
import re

#### ZIPF'S LAW OF ABBREVIATION IN ENGLISH ####
set(stopwords.words('english')) #to remove stopwords in English

word_frequencyEN = {} #We need a dictionary to store the frequency of each word

for url in urlsEN: #Since we have more than one url, we need a for loop to iterate over each of them
    responseEN = urllib.request.urlopen(url) #we use this module to retrieve the text from the urls
    htmlEN = responseEN.read()
    textEN = htmlEN.decode("utf-8").lower() #the text is converted to encoding UTF-8 and lowercase
    cleantextEN = re.sub("'<.*?>'", '', textEN, flags=re.DOTALL) #removing non alphanumeric characters from the text
    wordsEN = cleantextEN.split() #and tokenized using the .split() function
    wordsEN_without_sw = [word for word in wordsEN if not word in stopwords.words()] #removing all stopwords in English



for word in wordsEN_without_sw: #For each word in the text, its frequency is stored here.
  if word in word_frequencyEN:
    word_frequencyEN[word] += 1
  else:
    word_frequencyEN[word] = 1

sorted_word_frequencyEN = sorted(word_frequencyEN.items(), key=lambda x: x[1], reverse=True) #The words in the dictionary are sorted from most frequent to least.


ranksEN = []
for i, (word, frequency) in enumerate(sorted_word_frequencyEN): #With a for loop, we calculate the rank of each word's frequency and store it in a list.
    rankEN = i + 1
    ranksEN.append(rankEN)


plt.loglog(ranksEN, [frequency for (word, frequency) in sorted_word_frequencyEN])
plt.xlabel("Rank") #In the x axis of the graph, the rank is plotted.
plt.ylabel("Frequency") #In the y axis of the graph, the frequency is plotted.
plt.title("Zipf's Law of Abbreviation in English")
plt.show()

#### ZIPF'S LAW OF ABBREVIATION IN GERMAN ####
set(stopwords.words('german')) #to remove stopwords in German

word_frequencyDE = {} #We need a dictionary to store the frequency of each word
for url in urlsDE: #Since we have more than one url, we need a for loop to iterate over each of them
    responseDE = urllib.request.urlopen(url) #we use this module to retrieve the text from the urls
    htmlDE = responseDE.read()
    textDE = htmlDE.decode("utf-8").lower() #the text is converted to encoding UTF-8 and lowercase
    cleantextDE = re.sub("'<.*?>'", '', textDE, flags=re.DOTALL) #removing non alphanumeric characters from the text
    wordsDE = word_tokenize(cleantextDE, language="german") #instead of tokenizing the text with the .split() function, we have used NLTK
    wordsDE_without_sw = [word for word in wordsDE if not word in stopwords.words()] #removing all stopwords in German like "der", "die", "das"

for word in wordsDE_without_sw: #For each word in the text, its frequency is stored here.
  if word in word_frequencyDE:
    word_frequencyDE[word] += 1
  else:
    word_frequencyDE[word] = 1

sorted_word_frequencyDE = sorted(word_frequencyDE.items(), key=lambda x: x[1], reverse=True) #The words in the dictionary are sorted from most frequent to least.

ranksDE = []
for i, (word, frequency) in enumerate(sorted_word_frequencyDE): #With a for loop, we calculate the rank of each word's frequency and store it in a list.
    rankDE = i + 1
    ranksDE.append(rankDE)

plt.loglog(ranksDE, [frequency for (word, frequency) in sorted_word_frequencyDE])
plt.xlabel("Rank") #In the x axis of the graph, the rank is plotted.
plt.ylabel("Frequency") #In the y axis of the graph, the frequency is plotted.
plt.title("Zipf's Law of Abbreviation in German")
plt.show()
