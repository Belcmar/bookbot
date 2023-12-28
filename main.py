with open("book.txt",'r') as file:
    var = file.read()
    print(var)
    file.close()
    pass 

    words = var.split()
    print("word count: ", len(var))