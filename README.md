# News-Headline-Scraper

Uses [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) to scrape thousands of news headlines for the most used words currently in the news.

To use run 'py scraper.py' via the command line

### Structure:
data/ignore.txt contains a set of unique words to ignore in news headlines such as "the" or "at"
data/sources.txt contains a url link to all the news sources to scrape from
data/tags.txt contains all the corresponding HTML tags to check for headlines

Project could be expanded upon to write to files/perform data analysis on
