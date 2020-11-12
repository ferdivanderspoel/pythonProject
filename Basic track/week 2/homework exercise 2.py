distance_str = input("What is the distance in KM?")
method_str = input("Which method of travel do you use?")

if method_str == "walking":
    method_str = 5
if method_str == "biking":
    method_str = 20
if method_str == "driving":
    method_str = 40

distance_int = int(distance_str)
method_int = int(method_str)

time_int = distance_int / method_int

print("The total time is: ", time_int)
