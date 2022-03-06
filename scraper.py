from src.News import News
import time

start_time = time.time()
news = News()

print()
print('--TOP NEWS WORDS OF THE DAY--')
print()
for word, freq in sorted(news.words.items(), key=lambda item: item[1]):
    if freq > 10:
        data = 'X' * freq
        print(word + ': ' + data)
        print()

exec_time = round(time.time() - start_time, 2)
print()
print(str(news.headCount) + ' headlines scraped in ' + str(exec_time) + ' seconds')
