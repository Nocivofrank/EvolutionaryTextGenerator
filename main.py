import brain as br

brains = []

amount_of_brains = 10

for i in range(amount_of_brains):
    brains.append(br.Brain(i))
    print(brains[i], brains[i].id)

context_lenght = 10

text = "Hello there world how are you today and how are we feeling?"
text_new = ""

ascii_dict = {
    # Whitespace
    29: "\t",   # Tab
    30: "\n",   # Newline
    31: "\r",   # Carriage Return
    32: " ",    # Space

    # Printable ASCII (33–126)
    **{code: chr(code) for code in range(33, 127)}
}

# print(repr(ascii_dict[29]))

for i in range(context_lenght):
    text_new += text[i]

while True:
    print("\n")
    user_input = input("User: ")
    refined_input = ""
    for i in range(context_lenght):
        if i < len(user_input):
            refined_input += user_input[i]

    for i in brains:
        for j in range(context_lenght):
            # print(j)
            if j < len(refined_input):
                i.information[j] = ord(refined_input[j])
            else:
                i.information[j] = 0

    biggest = 0

    for i in brains:
        biggest = 0
        thoughts = i.brainThink()

        count = 0
        for j in thoughts:
            if j > thoughts[biggest]:
                biggest = count
            # print(j)
            count += 1
            # print(i.brainThink())
        biggest += 29
        print(f"{refined_input}{ascii_dict[biggest]}")
