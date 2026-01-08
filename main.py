import brain as br

brains = []

amount_of_brains = 5

for i in range(amount_of_brains):
    brains.append(br.Brain(i))
    print(brains[i], brains[i].id)

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

# for i in range(context_lenght):
#     text_new += text[i]

while True:
    print("\n")
    user_input = input("User: ")
    raw_input = ""
    for i in range(br.Brain.input_size):
        if i < len(user_input):
            raw_input += user_input[i]    

    for i in brains:
        for j in range(br.Brain.input_size):
            # print(j)
            if j < len(raw_input):
                i.information[j] = ord(raw_input[j])
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
        i.prev_token = biggest
        print(f"{raw_input}{ascii_dict[biggest]}, prev token: {i.prev_token}")

    expected_output = input("Expected Output: ")

    found_match = False
    prev_mean = 0
    mean = 0
    closer = False
    mult = 1

    while not found_match:
        mean = 0
        for i in brains:
            mean += i.prev_token
            if ascii_dict[i.prev_token] == expected_output:
                found_match = True
                for j in brains:
                    if i.id != j.id:
                        j.W1 = i.W1
                        j.b1 = i.b1
                        j.W2 = i.W2
                        j.b2 = i.b2
                        j.W3 = i.W3
                        j.b3 = i.b3
                        j.W4 = i.W4
                        j.b4 = i.b4
                        j.W5 = i.W5
                        j.b5 = i.b5
                        j.W6 = i.W6
                        j.b6 = i.b6
                        j.W7 = i.W7
                        j.b7 = i.b7
                        j.brainMutate()
                break
            else:
                i.revertToPreviousBrain()
                mean = mean / amount_of_brains

                i.brainMutate()
                
                biggest = 0
                thoughts = i.brainThink()
                
                count = 0
                for j in thoughts:
                    if j > thoughts[biggest]:
                        biggest = count
                    count += 1
                biggest += 29
                i.prev_token = biggest
                print(f"{raw_input}{ascii_dict[biggest]}, prev token: {i.prev_token}")

        print(f"Mean: {mean}, Expected Value: {ord(expected_output)}")
    


