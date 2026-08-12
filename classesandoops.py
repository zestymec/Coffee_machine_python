class User:
    def __init__(self , user_id , username):
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User("001" , "umer")

print(user_1.username)

user_2 = User("213" , "name")
# user_2.id = "002"
# user_2.uname = "haumer"

print(user_2.followers)
# class Car:
#     def __init__(self , seats):
#         self.seats = seats
# def learning():
#     user_1.id = "001"
#     user_1.uname = "umer"
