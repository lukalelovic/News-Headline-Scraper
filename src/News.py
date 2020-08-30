from bs4 import BeautifulSoup
import requests

class News(object):

    def __init__(self):
        self.data = {'q':'goog'}
        self.headers = {'User-Agent': 'Chrome/80.0.3987.163'}

        ignoreFile = open('data/ignore.txt', 'r')
        self.ignore = ignoreFile.read().splitlines()

        self.words = []
        self.frequency = []

        self.headCount = 0

        sourceFile = open('data/sources.txt', 'r')
        tagFile = open('data/tags.txt', 'r')

        sources = sourceFile.read().splitlines()
        tags = tagFile.read().splitlines()

        for i, line in enumerate(zip(sources, tags)):
            self.addWords(line[0], line[1])

            if (i > 0):
                print('SCRAPING: ' + str(round(i / (len(sources) - 1) * 100)) + '% COMPLETE', end='\r')
        print()
        print()

        self.sortWords()

        ignoreFile.close()
        sourceFile.close()
        tagFile.close()
    
    #Check if word should be ignored
    def ignoreWords(self, thisWord):
        for ignore in self.ignore:
            if thisWord == ignore:
                return True
        return False

    #Check if word already exists
    def checkFreq(self, thisWord):
        for word in self.words:
            if thisWord == word:
                self.frequency[self.words.index(word)] += 1
                return True
        return False

    #Tally up words
    def addWords(self, url, element):
        page = requests.get(url, params=self.data, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        headlines = soup.findAll(element)
        for headline in headlines:
            self.headCount += 1
            for headWord in headline.get_text().split():
                headWord = headWord.upper()
                if self.ignoreWords(headWord):
                    break

                if self.checkFreq(headWord):
                    break

                self.words.append(headWord)
                self.frequency.append(1)
        
    #Sort/Rank the headlines
    def sortWords(self):
        self.words = [x for _,x in sorted(zip(self.frequency, self.words), reverse = True)]
        self.frequency = sorted(self.frequency, reverse = True)