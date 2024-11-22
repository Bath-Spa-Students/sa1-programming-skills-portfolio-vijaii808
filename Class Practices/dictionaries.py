# Python have collection of data in the form of key pair value  , there is a key and there is a particular value against each key 
# key is immutable but value against key is mutable 
# Curly braces used in dictionary  - Operators are used to check data (in  ,  not in )
#Len function used for list -tuple -dictionary 


# Creation of  dictionary 

dictionary = {}
print(dictionary)

# Check the type of dictionary

dictionary = {}
print(dictionary, type(dictionary))

# Another way to create dictionary -
 
dictionary = dict()
print(dictionary, type(dictionary))

# To add something in dictionary 
example = {'color' : 'red '  , 'fruit' : 'apple' ,'place' : 'United arab emirates '}
print (example)


# To add some value in dictionary 

dictionary  = { 'Name' : 'Rafia' , 'Roll No ' :  '1234' , 'Fathers name ': 'Muhammad Murtaza' } 
print(dictionary,type(dictionary))
 # Name , roll no are keys , rafia  and 123 are values


# lets check if we want to return one value ,  so it is a dictionary 

dictionary  = { 'Name' : 'Rafia' , 'Roll No ' :  '1234' , 'Fathers name ': 'Muhammad Murtaza' } 
print(dictionary["Name"],type(dictionary))

# Testing dictionary 

dictionary  = { 'Name' : 'Rafia' , 'Roll No ' :  '1234' , 'Fathers name ': 'Muhammad Murtaza' } 
print(dictionary["student"])  # there is an exception that this key is not in the dictionary

# We can use get method to check whether the student is available in the dict or not 

dictionary  = { 'Name' : 'Rafia' , 'Roll No ' :  '1234' , 'Fathers name ': 'Muhammad Murtaza' } 
print(dictionary.get("student"))

# As student is not in dict we get None , lets assign a default value to avoid exception

dictionary  = { 'Name' : 'Rafia' , 'Roll No ' :  '1234' , 'Fathers name ': 'Muhammad Murtaza' } 
print(dictionary.get("student", "Anmol "))


# to test .items methods   


dictionary  = { 'Name' : 'Rafia' , 'Roll No ' :  '1234' , 'Fathers name ': 'Muhammad Murtaza' } 
print(dictionary.items())
 # in out put small braces bcz they are tuples , key value pair is in tuple form ---- There is a list and in the list every value is in tuple form 
 #   ('Name ', 'Rafia ')  -this is a element   -to secure our data not to change 



 # To check keys in our dictionary 


dictionary  = { 'Name' : 'Rafia' , 'Roll No ' :  '1234' , 'Fathers name ': 'Muhammad Murtaza' } 
print(dictionary.keys())

# output - in list form we get keys in our dict


# Delete method 


dictionary  = { 'Name' : 'Rafia' , 'Roll No' :  '1234' , 'Fathers name ': 'Muhammad Murtaza' } 
del dictionary ["Roll No"]
print(dictionary.items())


# Delete method -Cont


dictionary  = { 'Name' : 'Rafia' , 
               'Roll No' :  '1234' , 
               'Fathers name ': 'Muhammad Murtaza' } 
del dictionary ["Roll No"]
print(dictionary.items())
print(dictionary.keys())
print(dictionary.values())


# Pop Method  - to remove 

dictionary  = { 'Name' : 'Rafia' ,
                'Roll No' :  '1234' , 
                'Fathers name ': 'Muhammad Murtaza' } 
print(dictionary.pop("Name"))
print(dictionary.keys())
print(dictionary.values())


# pop items  - Ot delete items from last value dictionary always return element in the from of tuple 

dictionary  = { 'Name' : 'Rafia' ,
                'Roll No' :  '1234' , 
                'Fathers name ': 'Muhammad Murtaza' } 
print(dictionary.popitem())
print(dictionary.keys())
print(dictionary.values())



# Dictionary For Loop 
 # https://www.w3schools.com/python/python_dictionaries_loop.asp

example = {'color' : 'red '  , 
           'fruit' : 'apple' ,
           'place' : 'United arab emirates '}
print (example)








