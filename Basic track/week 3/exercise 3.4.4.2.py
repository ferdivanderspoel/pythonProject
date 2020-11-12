weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

today = int(input("What is the start day? (0-6) "))
sleeps = int(input("How many sleeps?"))

print("You will return on", weekdays[(today + sleeps) % len(weekdays)])