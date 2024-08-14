#open file, read content and close file
# file = open("text_file.txt")
# contents = file.read()
# print(contents)
# file.close()

#open with "with" keyword doesn't need to close the file and risking to forget
# with open("text_file.txt") as file:
#     contents = file.read()
#     print(contents)


#write with the file, delete old text set mode to "w"
#to add to previous text set mode to "a" for append
#if file doesn't exist as open and mode set to "w" it will create it 
# with open("new_file.txt", mode="w") as file:
#     file.write("creating a new file")


with open("./input/names/invited_names.txt") as data:
    list_of_names = data.readlines()

with open("./input/letters/starting_letter.txt") as letter_file:
   letter_contents = letter_file.read()
   for name in list_of_names:
       stripped_name = name.strip()
       new_letter = letter_contents.replace("[name]", stripped_name)
       with open(f"./output/ready_to_send/letter_to_{stripped_name}", "w") as letter:
           letter.write(new_letter)
