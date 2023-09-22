m=int(input("Type of body(m)="))
n=int(input("Number of links(n)="))
j=int(input("Number of joints(j)="))
Fi1=int(input("Number of Revolute joints(Fi)="))
Fi2=int(input("Number of sperical joints(Fi)="))
Fi3=int(input("Number of universal joints(Fi)="))
S= m*(n-1-j) + Fi1*1 +Fi2*3 + Fi3*2
print("DOF of given body is", S)