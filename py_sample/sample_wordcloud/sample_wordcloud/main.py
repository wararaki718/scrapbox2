import os

from wordcloud import WordCloud

from text_iterator import TextIterator
from text_tokenizer import TextTokenizer


def create_wordcloud(data_dir: str, image_path: str):
    texts = TextIterator(data_dir)
    tokens = []
    tokenizer = TextTokenizer()
    for text in texts:
        tokens.extend(tokenizer(text))
    data = " ".join(tokens)

    wordcloud = WordCloud(max_font_size=40).generate(data)
    wordcloud.to_file(image_path)


def main():
    create_wordcloud(
        'data/natsume/files/*.html',
        'images/natsume.png'
    )
    
    create_wordcloud(
        'data/dazai/files/*.html',
        'images/dazai.png'
    )

    print('DONE')


if __name__ == '__main__':
    main()
