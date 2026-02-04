from PythonClass.restaurant import Restaurant
from PythonClass.menu.drinks import drinks
from PythonClass.menu.item import item

restaurant = Restaurant("Burguer", "Hamburguers")
drink1 = drinks("Coke", 5.0, "small")
item1 = item("Bread", 2.0, "The best bread of the city!")
restaurant.add_item_menu(drink1)
restaurant.add_item_menu(item1)

def main():
    restaurant.show_menu

if __name__ == "__main__":
    main()