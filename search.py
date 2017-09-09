import itertools
def search(str):
    l={}
    with open("search.txt",mode="r") as ser:
        c = ser.readlines()
        c = map(lambda c: c.strip(), c)
        d = dict(itertools.zip_longest(*[iter(c)] * 2, fillvalue=""))
        for i in d:
            d = {i: d[i]}
            l.update(d)

