# write in file using with() function
with open('Pinterest.txt', 'w') as file:
    file.write("Hi! I am Penguin and I am 1 year old.")
file.close()

# split file into words
with open('Pinterest.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print (word)
file.close()
