# name PascalCase difference from camelCase , snake_case
class User:
    #initialise attributes 
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        
user_1 = User("111","sajjad")
print(user_1.id)
print(user_1.username)
