import sys

from sklearn.feature_extraction.text import CountVectorizer


# define sample data
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?'
]
comma_corpus = [
    'This,is,the,first,document.',
    'This,document,is,the,second,document.',
    'And,this,is,the,third,one.',
    'Is,this,the,first,document?'
]

def space_analyzer(text):
    return text.split()


def comma_analyzer(text):
    return text.split(',')


def check(vectorizer):
    print('space text:')
    print(vectorizer.transform([corpus[0]]))
    print('comma text:')
    print(vectorizer.transform([comma_corpus[0]]))
    print('')


def main():
    # modeling
    vectorizer = CountVectorizer(analyzer=space_analyzer)
    vectorizer.fit(corpus)
    print(vectorizer.get_feature_names())
    print('')

    print('[space vectorizer]')
    check(vectorizer)

    print('[comma vectorizer]')
    vectorizer.analyzer = comma_analyzer
    check(vectorizer)

    print('[space vectorizer]')
    vectorizer.analyzer = space_analyzer
    check(vectorizer)

    return 0


if __name__ == '__main__':
    sys.exit(main())
