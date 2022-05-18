with open("names.txt", "r") as file:
    loaded_config = file.readlines()
    for line in loaded_config:
        name = str(line)
        # split the string to list and take first argument which is name
        name = name.split('\n')[0]
        print(name)
        letter_template = "Dear " + name + ",\n\nYou are invited to my birthday this Saturday.\n\nHope you can make " \
                                   "it!\n\nXYZ"
        text_file = str(name + '.txt')
        with open(text_file, 'w') as invitation:
            invitation.write(letter_template)
