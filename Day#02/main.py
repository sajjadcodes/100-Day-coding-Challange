# Data Types

#string : anything inside double qoute treated as a string

"Hello"
# We can also use string character using []
"Hello"[3]
# print first character. subscript and subscripting. Start accounting from zero
"Hello"[0]

# contacatinate : string will not be calculated in this case. 

print("123" + "345")

#Integer: number data type.

print(123 + 345)

# large Integers 342,654,896
print(342_654_896)

# Float: For dicimal number, float point number

3.14159

# Boolean : Booleans has two types
True
False


#Checking Type


num_char = len(input("What is your name: "))

#Type error: because characters and integer con not be conncatinate
#print("your name has " +num_char+ "characters." )

#type() will return the data type
#print(type(num_char))

#Type conversion or 

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")






 
