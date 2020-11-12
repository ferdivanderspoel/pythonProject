current_time = int(input("What is the current hour?"))
alarm_remaining = int(input("How long do you have to wait?"))
alarm_goes_off = (current_time + alarm_remaining) % 24
print("The alarm will go off at", alarm_goes_off)