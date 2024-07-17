#CREEATE OWN CUSTOM CLASS
#class ClassName:

class User:
    #pass #tell python don't worry about it for now, otherwise if empty, indent error
    #constructor
    #call everytime an object is created for this class, can add parameter to construct an object
    def __init__(self, user_id, username): 
        #add to this object the parameter
        self.id = user_id 
        self.username = username
        #add a default value, doesn't to add as parameter
        self.followers = 0
        self.following = 0

    #add method to the class
    #always need self as first parameter
    def follow(self, user):
        user.followers += 1
        self.following += 1



user1 = User("001", "jojo")
user2 = User("002", "caca")
user1.follow(user2)
print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)
