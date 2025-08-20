a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
op = input("enter +, -, *, /: ")
if op == "+":
  print("result:", a+b) 
elif op == "-":
  print("result:", a-b)
elif op == "*":
  print("result:", a*b)
elif op == "/":
    if b != 0:
      print("result:", a/b)
    else:
      print("error: division by not allowed!")
else:
  print("invalid operation")
