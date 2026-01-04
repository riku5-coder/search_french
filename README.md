# プロジェクト名
**search_french**

wiktionaryのある単語ページからフランス語（または指定した言語）におけるその単語の語義と用例を抜き出すPythonファイル

---

## 機能
- フランス語（または指定した言語）の単語の語義と用例を調べことができる
- コマンドラインでファイルを実行する。ファイル名の後に調べたい単語と言語を指定する。言語はdefaultではフランス語

---

## セットアップ（ローカル実行方法）

```bash
git clone https://github.com/riku5-coder/search_french.git
cd search_french

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
python search_french.py [単語(dogなど)] [言語(Englishなど)]
```
