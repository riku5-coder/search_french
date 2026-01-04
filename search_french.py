import requests, sys
from bs4 import BeautifulSoup
"""wiktionaryの単語ページは言語別になっていない。
つまり、同じつづりであれば同じページに複数の言語における
そのつづりの単語の意味が載っている。
なので、目当ての言語のセクションをページから抜いて、
そこから意味だけを抜き出さなければならない"""
def search_french(word):
    # 目当てのページを取得
    url = 'https://en.wiktionary.org/wiki/{}#French'.format(word) 
    headers = {
    "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")

    # 目当ての言語のセクションを探す
    french_header = soup.find("h2", id="French")
    if french_header is None:
        raise ValueError("French sectionが見つかりませんでした")
    french_heading_div = french_header.find_parent("div", class_="mw-heading2")
    
    section_nodes = []
    for elem in french_heading_div.next_siblings:
        if getattr(elem, "name", None) == "div" and \
            "mw-heading2" in elem.get("class", []):
            break
        section_nodes.append(elem)

    meanings = []
    for node in section_nodes:
        if getattr(node, "name", None) == "ol":
            for li in node.find_all("li", recursive=False):

                meanings.append(li.get_text())

    print(f'意味は{len(meanings)}あります。')
    for i, meaning in enumerate(meanings, 1):
        print(f'{i}. {meaning}')


if __name__ == '__main__':
    search_french(sys.argv[1])