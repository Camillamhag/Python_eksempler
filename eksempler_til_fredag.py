

#Ulike loops eksempler:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
print(x)


#Else in loop:
for x in range(6):
  print(x)
else:
    print("Finally finished!")


#nested loops:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


#FUNKSJONER:

def my_function():
  print("Hello from a function")

#calling a function:
def my_function():
  print("Hello from a function")

my_function()

#Argumenter

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Number of Argumenter:


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


#Arbitrary argument *args: 
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#Arbitrary argument Arguments **Kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Passing a list as a argument:
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#To let a function return a value, use value key:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#Python also accepts function recursion, which means a defined function can call itself. 
#Ofte brukt med matte spørsmål.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)



#VARIABLER:

#Variabler er en oppbevaring for lagring av dataverdi:
x = 5
y = "John"
print(x)
print(y)

#Assign value to multiple variabler:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Outputs variabler:
x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z =  x + y
print(z)

x = 5
y = 10
print(x + y)

x = "awesome"

#Variabler inside av function:
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


n = 10
print_lend = list(range(1, n+1))
print_lens = print_lens[0:-1] + print_lens