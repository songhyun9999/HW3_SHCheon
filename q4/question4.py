def main():
    print(fact(0))
    print(fact(2))
    print(fact(4))
    print(fact(6))
    print(fact(8))
    print(fact(10))
    print(fact(12))
    print(fact(14))


def fact(n):
    if(n>=1):
        return n*fact(n-1)
    else:
        return 1
if __name__=="__main__":
    main()  