def area_of_circle(r):
    result = 3.1416 * (r * r)
    return result

answer = int(input("What is the radius?"))
t = area_of_circle(answer)
print("The area of circle is",t)