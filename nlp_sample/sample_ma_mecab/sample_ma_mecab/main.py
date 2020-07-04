import MeCab

mecab = MeCab.Tagger("")
print(mecab.parse("私はご飯を食べます。"))
