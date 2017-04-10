def main():
    av = 2
    bv = 2
    cv = 3
    lab = ((av+bv)**2+cv**2)**.5
    lac = ((av+cv)**2+bv**2)**.5
    lbc = ((bv+cv)**2+av**2)**.5
    print(lab,lac,lbc)

main()