from datasketch import MinHash
from datasketch import WeightedMinHashGenerator
from datasketch import HyperLogLog
from datasketch import HyperLogLogPlusPlus


def get_minhash(data: list) -> MinHash:
    m_hash = MinHash()
    for d in data:
        m_hash.update(d.encode('utf8'))
    return m_hash


def get_hyperloglog(data: list) -> HyperLogLog:
    h_loglog = HyperLogLog()
    for d in data:
        h_loglog.update(d.encode('utf8'))
    return h_loglog


def get_hyperloglog_pp(data: list) -> HyperLogLogPlusPlus:
    h_loglog_pp = HyperLogLogPlusPlus()
    for d in data:
        h_loglog_pp.update(d.encode('utf8'))
    return h_loglog_pp


def main():
    data1 = ['this', 'is', 'a', 'pen']
    data2 = ['that', 'is', 'a', 'pen']
    data3 = ['it', 'is', 'a', 'pon']

    m1 = get_minhash(data1)
    m2 = get_minhash(data2)
    m3 = get_minhash(data3)

    print('minhash:')
    print(m1.jaccard(m2))
    print(m1.jaccard(m3))
    print(m2.jaccard(m3))
    print()

    v1 = [1, 2, 3, 4, 5, 6]
    v2 = [2, 5, 7, 9, 11, 13]
    v3 = [1, 2, 3, 4, 5, 7]
    wmg = WeightedMinHashGenerator(len(v1))
    wm1 = wmg.minhash(v1)
    wm2 = wmg.minhash(v2)
    wm3 = wmg.minhash(v3)
    
    print('weighted minhash:')
    print(wm1.jaccard(wm2))
    print(wm1.jaccard(wm3))
    print(wm2.jaccard(wm3))
    print()

    data = data1 + data2 + data3
    hll = get_hyperloglog(data)
    print('hyperloglog:')
    print(hll.count())
    print()

    hpp = get_hyperloglog_pp(data)
    print('hyperloglog++:')
    print(hpp.count())
    print()


    print('done')


if __name__ == "__main__":
    main()
