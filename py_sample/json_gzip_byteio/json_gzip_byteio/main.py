import gzip
import io
import json


def main():
    data = [
        {
            'id': 123,
            'name': 'abc',
            'age': 23
        },
        {
            'id': 456,
            'name': 'def',
            'age': 45
        }
    ]
    s = "\n".join(map(json.dumps, data))
    bdata = io.BytesIO()
    with gzip.open(bdata, 'wt') as gf:
        gf.write(s)
    bdata.seek(0)
    print(bdata)
    print('DONE')


if __name__ == '__main__':
    main()
