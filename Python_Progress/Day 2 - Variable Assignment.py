#Day 2 - Variable Assignment
# a = 5
# print(a)
# a = 10
# print (a)
# a = a + a
# print(a)
# print(type(a)) # int
# print(type("abc")) # str
# print(type(("a", "b", "d"))) # tup
# print(type({"a": 1, "b" : 2})) # dict
# print(type({"a", "b", "c"})) # set
# print(type(False)) # bool
# print(type(["a", 1, 3])) # list

# my_income = 100
# tax_rate = 0.1
# my_taxes = my_income * tax_rate
# print(my_taxes)
# print(type(my_taxes)) # float

# my_string = "philip"
# letter = my_string[2]
# print(letter)
# sub_name = my_string[2:] # includes the character at 2
# print(sub_name)

# prefix = my_string[:3] # upto but not include character at index 3
# print(prefix) # phi
# substring = my_string[2:4]
# print(substring) #il

# alphabet = "abcdefghijkl"

# print(alphabet[::]) # equvalient to printing the whole string
# skip = alphabet[::2] # skips every other letter
# # this is the third parameter
# print(skip)
# skip2 = alphabet[::3] # skips 2 letters
# print(skip2)

# print(alphabet[2:7:3]) #cf

# print(alphabet[::-1]) # reverses a string
# #interviewers annoyed by this one line trick instead of looping

# #string properties and methods
# letter = "z"
# print(letter * 10) # 'zzzzzzzzzz'

# # built-in string methods
# # objects in python usually have their own methods
# # methods are functions inside the object

# x = "Hello World"
# print(x.upper()) # does not affect the original string
# # x = x.upper()
# # print(x)

# print(x.split()) # split by the white space into an array

# print(x.split('o')) # removes all the Os and splits the string
# # strings are not mutable

# # string interpolation
# print("This is a string {}".format(345))

# print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

# # the indexes of the strings in the format function can be entered into the {} in the string that we want to manipulation

# print('The {q} {b} {f}'.format(f = 'fox', b ='brown', q = 'quick'))

# #float formatting
# result = 100/777
# print(result)

# # {value:width.precision f}
# print("The result was {r:1.3f}".format(r = result))
# # 0.129
# print("The result was {r:10.5f}".format(r = result))
# # 0.12870 and adds more white space for the float number

# # f string syntax
# name = 'Philip'
# print(f'Hello, my name is {name}')
# # the f is the same as the format method

#Lists are ordered sequences that can hold a variety of objects (int, str, bool, etc)
# Lists use [] brackets and commas to separate objects in the list
# support indexing and slicing
# similar to arrays in javascript

# my_list =[1 ,2, 3]
# print(len(my_list))

# my_list = [100, "string", 102.34]
# print(len(my_list))
# print(type(my_list[0]))
# print(my_list[:3])
# print(my_list[1:])

# another_list = ['four', 'five']
# new_list = my_list + another_list
# print(new_list)
# new_list[0] = "future is here"
# print(new_list)

# new_list.append("123") # append = push in javascript

# print(new_list)
# # append effects the list in place

# popped_item = new_list.pop() # same in javascript array methods
# print(new_list)
# print(popped_item)

# #sort method sorts the list in place so it returns a noneType

# new_list = ['b', 'x', 'p', 'a']
# print(type(new_list.sort())) # noneType

# print(new_list.sort()) # none
# print(new_list)

# num_list = [ 4, 5, 1, 7]
# num_list.sort()
# print(num_list)

# num_list.reverse() # reverse list in place
# print(num_list)

# dictionaries are similar to objects in javascript

# d = {'k1': 100, 'k2': 200, 'k3':300}
# print(d.keys()) # dict_keys(['k1', 'k2', 'k3'])
# print(d.values()) # dict_values([100, 200, 300])
# print(d.items())

# #tuples - similar to list but are immutable - once an element is inside a tuple, it can not be reassigned - tuples use (1, 2, 3)

# t = ('a', 'a', 'b')
# print(t.count('a')) # 2 counts of a

# print(t.index('a')) # returns the first index location of the a

# # tuples are useful later when we are more advanced in python by restricting the changability of a variable - for error handling

# #sets - similar to set() in javascript

# myset = set()
# myset.add(1)
# print(myset)
# # unique values only

# mylist = [1,1,2,2,3,3]
# new_set = set(mylist)
# print(new_set)

print((4 ** (1/2)))
print (4 ** 2)

s ='hello'
print(s[4:])

s = [0]
print(s *3)
s.append(0)
s.append(0)
print(s)

list3 = [1,2,[3,4,'hello']]
list3[2][2] ='goodbye'
print(list3)

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

list5 = [1,2,2,33,4,4,11,22,3,3,2]

print(set(list5))

print(3.0 == 3)

print(4**0.5 != 2)