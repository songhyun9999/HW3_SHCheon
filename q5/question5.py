def main():
    str='''Two roads diverged in a yellow wood, And sorry I could not travel both And
be one traveler, long I stood And looked down one as far as I could To where 
it bent in the undergrowth;'''
    str2='''Then took the other, as just as fair, And having perhaps the better claim, 
Because it was grassy and wanted wear; Though as for that the passing there 
Had worn them really about the same,'''
    str.replace('\n',' ')
    str2.replace('\n',' ')
    print("Original String 1 : ")
    print(str)
    list = reverse_words(str)
    print("Reversed String 1 : ")
    for s in list:
        print(s,end=" ")
    print("\n\n")

    print("Original String 2 : ")
    print(str2)
    print("Reversed String 2 : ")
    list2 = reverse_words(str2)
    for s in list2:
        print(s,end=" ")
    print("\n")

def reverse_words(str):
    list=str.split(" ")
    list.reverse()
    return list


if __name__=="__main__":
    main()  
