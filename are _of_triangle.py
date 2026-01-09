#when all the sides known
a = float(input("enter the first side of thr triangle"))
b =float (input("enter the second side of thr triangle"))
c = float(input("enter the third side of thr triangle"))
s = (a+b+c)/2
# result = pow((s*(s-a)*(s-b)*(s-c)),1/2)
 Area = (s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is",Area)
