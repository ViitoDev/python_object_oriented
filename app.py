from PythonClass.restaurant import Restaurant

restaurant = Restaurant("Burguer", "Hamburguers")
restauran1 = Restaurant("Akemi", "Sushi")
restaurant.receive_avaluate("Edu", 10)
restaurant.receive_avaluate("Rossi", 8)


restauran1.state_alternate()

def main():
    Restaurant.show_restaurants()

if __name__ == "__main__":
    main()