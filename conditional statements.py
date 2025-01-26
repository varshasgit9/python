Python conditional statements are used to control the flow of a program based on conditions or decisions. The following are the main types of Python conditional statements:

1. If Statement: Used to execute a block of code if a condition is true.
2. If-Else Statement: Used to execute a block of code if a condition is true, otherwise execute another block of code.
3. If-Elif-Else Statement: Used to check multiple conditions and execute different blocks of code.
4. Nested If Statement: Used to check multiple conditions and execute different blocks of code.

These statements use comparison operators, logical operators, and conditional expressions to evaluate conditions and make decisions.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
If Statement
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if condition:
    # code to be executed

Example:

x = 5
if x > 10:
    print("x is greater than 10")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
If-Else Statement
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if condition:
    # code to be executed if condition is true
else:
    # code to be executed if condition is false

Example:

x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
If-Elif-Else Statement
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if condition1:
    # code to be executed if condition1 is true
elif condition2:
    # code to be executed if condition1 is false and condition2 is true
else:
    # code to be executed if all conditions are false

Example:

x = 5
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Nested If Statement
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if condition1:
    if condition2:
        # code to be executed if both conditions are true
    else:
        # code to be executed if condition1 is true and condition2 is false
else:
    # code to be executed if condition1 is false

Example:

x = 5
y = 3
if x > 10:
    if y > 2:
        print("x is greater than 10 and y is greater than 2")
    else:
        print("x is greater than 10 but y is less than or equal to 2")
else:
    print("x is less than or equal to 10")
