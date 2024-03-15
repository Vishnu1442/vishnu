# ! --------> common functions for list

# 11 = [6, 7, 8, 9, 0]
# print(len(11))

# print(max(11))
# print(min(11))

# 11 = [6, 8, 9, "p", "u"]
# print(max(11)) # --> error coz its a combination of int and string
# print(min(11)) # --> error coz its a combination of int and string

# 11 = [6, 7, 9, 0, 8.89, -5, 0.78]
# print(min(11)) # -5

# 11 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# index() --> to get index value of specific element
# print(11.index(9))

# 11 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
# count() --> how many num of times an element is reapeated
# print(11.count(6))

#! some functions which is specifically used for list

# To add element inside list
# ? insrert(index_value, element) --> to add element at specific index position
# 11 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
# 11.insert(2, "cars")
# print(11)

# ? To delete element from list
# 11 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5,  0.78]
#* pop() ---> last element will be deleted
# 11.pop()
# print(11)


# *remove(element) --> used to delete element directly
# 11.remove(8.89)
# print(11)

#* clear() --> to complete delete all element in list
# 11.clear()
# print(11)

# del -> to delete the list
# del 11 #or del(11)
# print(11)

# ? ----> join 2 lists

# 11 = [9, 0, 8]
# 12 = ["p", "o", "t", 34]
# * print(11+12)

# ! or

# * extend() --> to combine 2 lists
# 11.extend(12)
# print(11)

# ? ------> copy()
# 11 = [6, 7, 8, 9, 3]
# 12 = 11.copy()
# print(12)
# print(11)

# print(id(11))
# print(id(12))

# ! diff between shallow copy and deep copy
# sallow copy
# import copy
# 11 = [8, 9, 0,[5, 6], [3, 2, 1]
# 12 = copy.copy(11)
# 11.append(890)
# print(11)
# print(12)


# * deep copy --> used to copt the list with nested list
# import copy
# 11 = [8, 9, 0,[5, 6], [3, 2, 1]]
# print(11[-1][1]) --> to index nested list

# 12 = copy. deepcopy(11)
# 11[-1].append('cars')
# print(11)
# print(12)

# ? sort --> arrange elements in list in ascending or descending order
# 11 = [9, 7, 45, 0, -6, 5, 12]
# # 11.sort() # to arrange in ascending order
# # print(11)

# 11.sort(reverse=true) # to sort in descending order
# print(11)

# 11 = ['z', 'i', 'o', 'p', 9]
# 11.sort()
# print(11) # -->  error

# ? list  constructor
# * list() --> to conver other collection datatypwe to list
# 13 = ((8, 9, 0))
# print(list(13))

# 14 = (8, 9)
# print(list(14))

# ! ---> nested list
# 11 = [8, 9[0, 8, 7], ["p", "o", 'y'], [8, 't']]
# print(11[-2][1]) # --> o

# print(11[1:4])
# print(11[1:-1])

# ? to delete "t" from 11
# 11[-1]. remove('t')
# print(11)

# ? to combine these ["p", "o", 'y'], [8, 't'] lists in 11 to ["p", "o", 'y', 8, 't']
# 11[-2].extend(11[-1])
# 11.pop(-1)
# print(11)

# ! -------> tuole
# *car of tuple

# 1.) Tuple have to be surrounded by ()
# 2.) The elements inside tuple are not changable
# 3.) The elements inside tuple are indexed
# 4.) The element will execute in order
# 5.) It is heterogenous
# 6.) It allow duplicate elements

# eg:
# t1 = (8, 8, 9, 6, 5.78, [9, 0], (6, 8), "hey", 9+6j)
# print(t1)
# print(type(t1))

# ? indexing , slicing are all same as list

# ? indexing, slicing are all same as list

# 11 = (8)
# print(type(11)) # int

# 11 = (8,)
# print(type(11)) # tuple

t1 = 8,9
# print(type(t1)) # tuple

# t2 = 8,
# print(type(t2)) # tuple

# len(), min(), max(), index(),count() ----> all the same as list

# to add elements inside tuple --> cannot add
# cannot delete any element from tuple

# * join 2 tuples
# t1 = (8, 9, 0)
# t2 = (6, 7, 8)
# print(t1+t2)

# * To add  all element inside list and tuple
# sum()
# 11 = (8, 9, 0, 89, 12)
# print(tuple(sorted(t1)))
# print(tuple(sorted(t1, reverse = True)))

# * Iterate list and tuples

# 11 = [9, 8, 0, 6, 5]
# for i  in 11:
#    print(i)

# * Iterate based on index value
# 11 = [9, 8, 0, 6, 5]
# for i in range(0,len(11)):
#   print(11[i])

# ! print(11[1]
# s1 = 'o'
# printy(type(s1))

# s1 = "u"
# print(type(s1))

s1 = "hello world"
# * To access string
print(s1)
# indexing and slicing  --> same as list and tuple
print(s1[0.5])

# ---> common functions

# len(), min(), count()
s1 = "hello world"
# print(len(s1))
# print(max(s1))
# print(min(s1))

# ord () ---> used to find the ASCII value of a character
# s1 = 'u'
# print(ord(s1))

# ! Functions of string
# ? to convert all characters to upper case
# print(s1.upper())

# ? to conver to lower case
# s1 = "HFREDGiou"
# print(s1.lower())

# ? strip() --> to eliminate the space in beginning and end of spring
s1 = " Where are you?"
# print(s1.1strip())
# print(s1.rstrip())
# print(s1.strip())

# split() --> to split the words in  string based on a character
# s1 = "where are you?"
# print(s1.split())
# print(s1.split())

# print(s1. count('e'))

# * replace() --> to replace a specific char in the string
# s1 = "Where are you?"
# print(s1.replace())

# swapace() --> to convert capital to small and small to capital at a time
# s1 = "HEY there"
# print(s1.swapcase())

# * title() --> to write the string in format of title
# s1 = 'never giveUp'
# print(s1.capitalize())

# * capitalize() --> 1st char of string will be converted to capital
# s12 = never giveUP
# print(s1.capitalize())

# * join the strings
s1 = "hello"
s2 = "world"
print(s1+s2)

# s1 = '''how are you
# iam fine
# hey there
# '''
# # * splilines() --> used to split the string based on lines
# print(s1.splitlines())

#* find() --> to find the index based on a charachter
# s1 = "hello world"
# print(s1.find('z'))
# print(s1.index('z'))

# * join() -->
# 11 = ["hey", "there"]
# print(" ".join(11))
# print("$".join(11))

s1 = "Welcome to all"
# * print(s1.startswith('1'))
# * print(s1.startswitch('W'))

# s1 = "67"
# print(type(s1))
# print(s1.isdigit())

# * print the string in reverse manner
s1 = "Welcome to all"
# print(s1[::-1])

# ! ---> Eg:1
# wap to find the number of lower case letters
# s1 = "HEY there you aRE"
# count = 0
# for i in s1:
#    if i.islower():
#        count+=1
# print("The total num of lowercase letters: ",count)


# ! -----> Eg:2 r --> "$"
s1 = 'restarter'
s1 = "IMAGIN"
fst = s1[0]
bal [s1[1:]]
txt = bal.replace(fst, "$")
print(fst=txt)

     
# str1 = "bbbbbyyybbbaaioo"
# str 2 = "
     
# ! -----> Eg:3

s1 = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry  standard dummy text ever since the 1500 s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960 s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
s1
# chracters = len(s1)
# print(chracters)

# words = s1.split(" ")
# print(len(words))

sentences = s1.split('.')
for val in sentenses:
    if val =='':
        index = sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))

space = 0
for val in s1:
    space=" ":
print(space)

# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]
              


     











