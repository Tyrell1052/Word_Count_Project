file_to_open = input("Please Enter the name of the file:")
file = open(file_to_open, "r")
file_to_count = []
#total_characters_with_white_space = []
total_characters_without_white_space = []




def total_lines():

    line_counter = 0

    for line in file:
        line_counter += 1
    print("Total number of lines:", line_counter)

def total_words():

    word_counter = 0

    for line in file:
        words = line.split()

        for word in words:

            word_counter += 1

    print("Total number of words:", word_counter)


def total_characters_with_white_space():

    char_counter = 0

    for line in file:
        words = line.split()


        for word in words:
            char = word.split()


            char_counter += 1

    print("Total number of characters (excluding whitespace):", char_counter)



#total_lines()
#total_words()


#for line in file:
  #  line = line.rstrip()
    #print(line)
    #words = line.split()

    #print(words)
    #for w in words:
     #   print(w)

#for line in file:
    #for word in line.split():
        #file_to_count.append(file_to_count)
        #total_words += len(file)



#print(len(total_words))
#file_to_count = file.
#print(file_to_count)

#for index in range(len(file_to_count)):
   # file_to_count[index] =