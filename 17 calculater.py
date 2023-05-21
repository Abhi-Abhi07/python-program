print('''
+ ADDITION
- SUBTRACTION
* MULTIPLICATION
/ DIVIDE
''')
num1=int(input("Enter the value:1 "))
num2=int(input("Enter the value:2 "))
op=input("Enter opration which you perform (+,-,*,/): ")

# # # Using Neasted if else statement
# if op=='+':
#     print(num1+num2)
# else:
#     if op=='-':
#         print(num1-num2)
#     else:
#         if op=='*':
#             print(num1*num2)
#         else:
#             if op=='/':
#                 print(num1/num2)
#             else:
#                 print("Invalid operation")


# # Using if elif else statement
# if op=='+':
#     print(num1+num2)
# elif op=='-':
#     print(num1-num2)
# elif op=='*':
#     print(num1 * num2)
# elif op == '/':
#     print(num1 / num2)
# else:
#     print("Invalid operation")


if op=='+':
    print(num1+num2)
if op=='-':
    print(num1-num2)
if op=='*':
    print(num1*num2)
if op=='/':
    print(num1/num2)
if (op!='+' and op!='-' and op!='*' and op!='/'):
    print("Invalid operation")