#Copy list to another veriable
a = [18, 20, 4, 6, 3, 1, 9]
b = a
print(id(a))
print(id(b))


print(f"value of a is : {a}")
print(f"value of b is : {b}")

a.append(100)

print(f"value of a is : {a}")
print(f"value of b is : {b}")

#Reverce python string using slicing

str = "Hello world"

print(str[::-1])
print(str[-5:], str[:5])

#append item in tuple list

my_tuple = ([4,9,2], [8,4], [6])
my_tuple[2].append(14)
print(my_tuple)


#pype of print statment

my_text = "hello world"

print(f"my print statment is: {my_text}")
print("my print statement is: ", my_text)
print(f"my print statement is: {my_text = }")

#