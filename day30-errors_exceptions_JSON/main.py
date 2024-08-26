# # try
# #     code block that might cause an exception
# # except
# #     do this if there is an exception
# # else
# #     do this if there were no exception
# # finally
# #     do this no matter what

# try:
#     #file doesn't exist
#     file = open("file.txt")
#     dictionary = {"key": "value"}
#     print(dictionary["ojkzpoe"])

# except FileNotFoundError: #if FileNotFoundError is not specified we won't get an error for the non existing key in dictionary
#     #this specific except is working only for fileNotFounException
#     #if it doesn't exist create it
#     open("file.txt", "w")

# except KeyError as error_message:
#     #execute when this error is caught, catch the key and print it 
#     print(f"the key {error_message} does not exist")

# else:
#     #execute when try is executed correctly, here when file exist and the correct key is printed
#     content = file.read()
#     print(content)

# finally:
#     #execute everytime
#     # file.close()
#     # print("file was closed")

#     #Generate own exceptions
#     raise KeyError("made up error") #always generate a keyerror with this message

# height = float(input("height: "))
# weight = int(input("weight: "))

# if height > 3:
#     raise ValueError("height should not be over 3m")

# bmi = weight / height ** 2
# print(bmi)

#UPDATE TO PASSWORD MANAGER WITH JSON 