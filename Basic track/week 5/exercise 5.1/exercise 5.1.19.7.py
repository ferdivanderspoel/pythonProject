def reverse(input):
    rev_string = input[::-1]
    return rev_string

text = input("Type the string you would like to reverse.")
print("Here is your string, in reverse: " + reverse(text))

print("Tests:")
reverse("happy"), "yppah"
reverse("Python"), "nohtyP"
reverse(""),""