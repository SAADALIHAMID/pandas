                                                        # step 1
my_list=[]
                                                        #  |step 2
my_list.append("apple")
my_list.append("banana")
my_list.append("grapes")
                                                        # step4
my_list.insert(1,"mango")
                                                        # step5
my_list.remove("grapes")
print(my_list)


                                        #    next assignment


# Step 1: Create a tuple my_tuple with at least five elements
my_tuple = (1, 2, 3, 4, 5)

# Step 2: Use tuple unpacking to assign values to multiple variables
a, b, c, d, e = my_tuple

# Step 3: Concatenate two tuples and print the result
tuple1 = (3, 4, 5)
tuple2 = (7, 8, 9)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)


# Step 4: Access and print the elements of my_tuple using both positive and negative indexing 
print("Positive indexing:")
print(f"Element 1: {my_tuple[0]}")
print(f"Element 2: {my_tuple[1]}")
print(f"Element 3: {my_tuple[2]}")
print(f"Element 4: {my_tuple[3]}")
print(f"Element 5: {my_tuple[4]}")

# print("\nNegative indexing:")
print(f"Element -1: {my_tuple[-1]}")
print(f"Element -2: {my_tuple[-2]}")
print(f"Element -3: {my_tuple[-3]}")
print(f"Element -4: {my_tuple[-4]}")
print(f"Element -5: {my_tuple[-5]}")

            # step5
a=list(concatenated_tuple)
print(a)
print(type(a))

                                        # 3rd assignment
# Step 1: Create a variable number and initialize it with an integer value
num = 18 # You can replace 17 with any integer value

# Step 2: Use the modulus operator to check if the num is even or odd
if num % 2 == 0:
 print("The number is even")
else:
 print("The number is odd")
# Step 3: Use a comparison operator to check if the num is greater than or equal to 10
if num >= 10:
 print(f"THe number{num} is greater than or equal to 10")
else:
 print(f"THe number{num} is less than 10")

# Step 4: Combine logical operators to create a complex condition and print the result
if num % 2 == 0 and num >= 10:
    print(f"The number {num} satisfies the complex condition (even and greater than or equal to 10)")
else:
    print(f"The number {num} does not satisfy the complex condition (even and greater than or equal to 10)")


