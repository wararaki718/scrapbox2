from pytrends.request import TrendReq


def main():
    trends = TrendReq(hl='ja-JP', tz=360)
    
    # get related keywords
    keywords = ['Python', 'ML', 'Kotlin']
    trends.build_payload(keywords, cat=0, timeframe='today 5-y', geo='JP', gprop='')
    response = trends.related_queries()

    for key, value in response.items():
        print(f'key: {key}')
        for key2, value2 in value.items():
            print(key2)
            print(value2.head(5))
        print()
    
    print('DONE')


if __name__ == '__main__':
    main()
