import itertools
def repl():
    p={}
    with open("reply.txt", mode="r") as rep:
        c=rep.readlines()
        print(c)
        c = map(lambda c: c.strip(), c)
        d = dict(itertools.zip_longest(*[iter(c)] * 2, fillvalue=""))
        for i in d:
            g={i:d[i]}
            p.update(g)
    print(p)
repl()