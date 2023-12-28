with open("book.txt",'r') as file:
    var = file.read()
    print(var)
    file.close()
    pass 

    words = var.split()
    print("word count: ", len(var))
    
    
    print(var.lower())

    char_dict = {}
    for char in var:
        if char not in char_dict:
            char_dict[char] = 0

        char_dict[char] += 1

    print(char_dict)