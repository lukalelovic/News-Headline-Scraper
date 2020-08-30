from src.News import News
import time

start_time = time.time()
news = News()

print()
print('--TOP NEWS WORDS OF THE DAY--')
print()
for word in news.words:
    if news.frequency[news.words.index(word)] > 10:
        data = 'X' * news.frequency[news.words.index(word)]
        print(word + ': ' + data)
        print()

exec_time = round(time.time() - start_time, 2)
print()
print(str(news.headCount) + ' headlines scraped in ' + str(exec_time) + ' seconds')