'''input("What's your name? ")
print("hello, world")
#better
name=input("What's your name ? ")
print("Hello"+name)
print("Hello",name)'''
name=input("What's your name ? ")
print("Hello " , end="") ; print(name)
#most elegant
print(f"Hello , {name}")
name = input("What's your name? ")
print(name.title()) #Capitalize the first letter of each word, .capitalise=>only first letter of first word
name = input("What's your name? ").strip().title()
print(f"Hello , {name}")
print('================NUMBERS===================')
'''Let’s imagine, however, that you want to round the total to the nearest integer. 
Looking at the Python documentation for round you’ll see that the available arguments 
are round(number[n, ndigits]). Those square brackets indicate that something optional
 can be specified by the programmer. Therefore, you could 
do round(n) to round a digit to its nearest integer. Alternatively, you could code as follows:'''
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
z = round(x + y)

# Print the result
print(z)

print(f"{z:,}")
#Though quite cryptic, that print(f"{z:,}") creates a scenario where the outputted z will include commas where the result could look like 1,000 or 2,500.

z=round(2/3,2); print(z) # this will round the result to the nearest two decimal points.
h=2/3 ;print(f"{z:.2f}") #same as before but more formal