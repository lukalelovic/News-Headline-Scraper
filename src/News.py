from bs4 import BeautifulSoup
import requests

class News(object):
    def __init__(self):
        self.data = {'q':'goog'}
        self.headers = {'User-Agent': 'Chrome/80.0.3987.163'}

        ignoreFile = open('data/ignore.txt', 'r')
        self.ignore = set(ignoreFile.read().splitlines())

        self.words = {}
        self.headCount = 0

        sourceFile = open('data/sources.txt', 'r')
        tagFile = open('data/tags.txt', 'r')

        sources = sourceFile.read().splitlines()
        tags = tagFile.read().splitlines()

        # Iterate through each (url, HTML tag)
        for i, line in enumerate(zip(sources, tags)):
            self.addWords(line[0], line[1])

            if (i > 0):
                print('SCRAPING: ' + str(round(i / (len(sources) - 1) * 100)) + '% COMPLETE', end='\r')
        print()
        print()

        ignoreFile.close()
        sourceFile.close()
        tagFile.close()
    
    # Tally up words
    def addWords(self, url, element):
        page = requests.get(url, params=self.data, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        headlines = soup.findAll(element)
        for headline in headlines:
            self.headCount += 1
            for headWord in headline.get_text().split():
                headWord = headWord.upper()

                # Should the word be ignored?
                if headWord in self.ignore:
                    break
                elif any(c.isdigit() or c == "=" in self.ignore for c in headWord):
                    break

                if headWord in self.words:
                    self.words[headWord] += 1
                else:
                    self.words[headWord] = 0
