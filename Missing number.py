def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1,n[-1]):
        if i not in numbers:
            output.append(i)
    return output
listofNumbers = [2,3,4,9,10,13,16,18,20,24,27,32] 
print(findMissingNumbers(listofNumbers)) 
          