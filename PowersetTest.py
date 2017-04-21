

def powerset(tset):
    sl = int(len(tset))
    print(sl)
    tlist = list(tset)
    print(tlist)
    pset = set([])
    for i in range(2**sl-1):
        tx = i
        subset = set([])
        ctr = 0
        while tx:
            if tx&1:
                subset.add(tlist[ctr])
            ctr += 1
            tx >>= 1
        print(i,subset)
        pset.add(frozenset(subset))
    return pset


def main():
    print(powerset(set([0,2,3,4])))

main()