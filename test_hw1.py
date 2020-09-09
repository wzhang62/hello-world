def classify_triangle(a,b,c):
    if a == b or a == c or b == c:
        if a == b == c:
            return print('equilateral triangle')
        return print("isosceles triangle")
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return print("right triangle")
    if a != b != c:
        return print("scalene triangles")

a = float(input("please input A: "))
b = float(input("please input B: "))
c = float(input("please input C: "))

if a + b > c and a + c > b and b + c > a:
    classify_triangle(a, b, c)
else:
    print("length error!!")
    quit()