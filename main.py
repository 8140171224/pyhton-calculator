print("Hello, World. \ni'm aakash padhiyar form ahmedabad.")

print("this a cal to do some simple task")
print("+\n -\n  *\n   /\n    %\n")

q = int(input("your value 1 :"))
a = input("Here use them = ")
w = int(input("your value 2 :"))

if a=="+":
    print(q,"+",w,"=",q+w)
elif a=="-":
    print(q,"-",w,"=",q-w)
elif a=="*":
    print(q,"*",w,"=",q*w)
elif a=="/":
    print(q,"/",w,"=",q/w)
elif a=="%":
    print(q,"%",w,"=",q%w)
else:
    print('invalid operation.')
