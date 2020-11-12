def mirror(input):
    return input + input[::-1]

text = input("Type the string you would like to mirror.")
print("Here is your string, with its mirror: " + mirror(text))

print("Tests:")

mirror('good'),'gooddoog'
mirror('Python'),'PythonnohtyP'
mirror(''), ''
mirror('a'),'aa'