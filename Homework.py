#Exercise 1:
#Using in-place algorithm?
words = ['this' , 'is', 'a', 'sentence', '.']
def swap(lst1, w,x,y,z):
    lst1[w], lst1[x], lst1[y], lst1[z] = lst1[z], lst1[y], lst1[x], lst1[w]
    return lst1
swap(words,0,1,3,4) 

#list comprehension - reverses string too
def swap2(lst1):
    return [x[::-1] for x in lst1[::-1]]

#standard reverse
wordscopy = words[::-1]
print(wordscopy)

#Exercise 2:
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def countwords(string):
    string = string.lower()
    stringlist = string.split()
    dict1 = {}
    for x in stringlist:
        count = 0
        for item in stringlist:
            if x == item:
                count+=1
        dict1[x] = count
    return dict1
countwords(a_text)

#Exercise 3:
def linearsearch(list1, num):
    for i in range(len(list1)):
        if list1[i] == num: 
            return f'{num} is at index {i}' 


def linearsearch2(list1,num):
    count = 0 
    while count < len(list1):
        if list1[count] == num:
            return f'{num} is at index {count}'
        else:
            count+=1
linearsearch2([1,2,3,4,5,6,7,8],8)