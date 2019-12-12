from janome.analyzer import Analyzer
from janome.charfilter import UnicodeNormalizeCharFilter, RegexReplaceCharFilter
from janome.tokenfilter import CompoundNounFilter, POSStopFilter, LowerCaseFilter
from janome.tokenizer import Tokenizer


def main():
    text = '自然言語処理の基礎でも読もうかな。'
    
    char_filters = [UnicodeNormalizeCharFilter(), RegexReplaceCharFilter('自然言語処理', 'NLP')]
    tokenizer = Tokenizer()
    token_filters = [CompoundNounFilter(), POSStopFilter(['記号', '助詞']), LowerCaseFilter()]

    analyzer = Analyzer(char_filters=char_filters, tokenizer=tokenizer, token_filters=token_filters)

    print(text)
    for token in analyzer.analyze(text):
        print(token)    
    print('DONE')


if __name__ == '__main__':
    main()
