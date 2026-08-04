# from turtle import Turtle , Screen
# timmy = Turtle()
# print(timmy)

# # my_screen = Screen()
# # print(my_screen.canvheight)
# # my_screen.exitonclick()
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu" , "Squistle" , "charmander"])
table.add_column("Types", ["Electric" , "Water" , "Fire"])
table.align= 'l'
print(table)