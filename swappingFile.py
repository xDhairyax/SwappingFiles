def swapfile():
    file1=input("Enter first files name:")
    file2=input("Enter second files name:")

    with open(file1,"r") as a:
        data_a=a.read()

    with open(file2,"r") as a:
        data_b=a.read()

    with open(file1,"w") as a:
        a.write(data_b)

    with open(file2,"w") as a:
        a.write(data_a)  

    print(data_a)
    print(data_b)

swapfile()