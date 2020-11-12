def count_letters(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    print(count)