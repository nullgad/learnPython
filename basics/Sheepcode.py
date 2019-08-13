##sheep code 


def transilator(phrase):
    res = ""
    space = ""
    for letter in phrase:
        if letter is " ":
            space = space + ""
            for letter in space:
                if letter in "aeiouAEIOU":
                    res = res+letter + "sheep"
                else:
                    res = res + letter
    

    return res
    

print(transilator(input("type in anything : ")))
