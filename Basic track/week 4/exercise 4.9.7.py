def sum_to(n):
    result = (n * (n + 1)) / 2
    return result

answer = int(input("What is n?"))
t = sum_to(answer)
print("The sum is",t)