def insertionSort(s: list[int]):
    for i in range(1, len(s)):
        j = i
        while j > 0 and s[j] < s[j-1]:
            s[j],s[j-1] = s[j-1],s[j]
            j -= 1
    print(s)
    return(s)

insertionSort([5,6,4,3,7,2,1,8,9,0])