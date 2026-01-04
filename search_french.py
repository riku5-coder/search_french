import re, requests, bs4, sys

def search_french(word):
    url = 'https://en.wiktionary.org/wiki/{}#French'.format(word) # formatの()内に検索したいフランス語の単語を入れる。
    res = requests.get(url)
    res.raise_for_status()
    regex2 = re.compile(r'<span class="mw-headline" id="French">French</span>.*?<h2>', re.DOTALL)
    mo = regex2.search(res.text)
    soup = bs4.BeautifulSoup(mo.group())
    meanings = soup.select('ol > li')
    print('意味は{}つあります。'.format(len(meanings)))
    meaning_list = []
    for i in range(len(meanings)):
        meaning_list.append(meanings[i].getText())
    for i, meaning in enumerate(meaning_list):
        print('{}.{}'.format(i+1, meaning))

if __name__ == '__main__':
    search_french(sys.argv[1])