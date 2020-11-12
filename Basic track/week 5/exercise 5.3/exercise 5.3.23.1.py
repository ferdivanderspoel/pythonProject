start = 10
stop = 0
step = -2

if start > stop:
    if step < 0:
        fer = list(range(start, stop, step))
        print(fer)

    else: print("Not available")

if start < stop:
    if step > 0:
        fer = list(range(start, stop, step))
        print(fer)

    else: print("Not available")


