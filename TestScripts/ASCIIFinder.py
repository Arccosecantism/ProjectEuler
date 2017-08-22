def main():
    with open("Problem76.py") as fp:
        for i, line in enumerate(fp):
            if "\xe2" in line:
                print i, repr(line)
main()