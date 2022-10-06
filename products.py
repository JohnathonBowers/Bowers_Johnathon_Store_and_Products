class Product:
    def __init__(self, name:str, price, category:str, id):
        self.name = name
        self.price = price
        self.category = category
        self.id = id
    
    def update_price(self, percent_change, is_increased):
        change = self.price * percent_change
        if is_increased == True:
            self.price += change
            print (f"New price for {self.name} is: ${self.price:.2f}")
        if is_increased == False:
            self.price -= change
            print (f"New price for {self.name} is: ${self.price:.2f}")

    def print_info(self):
        print(f"Product name: {self.name}")
        print(f"Product price: ${self.price:.2f}")
        print(f"Product category: {self.category}")
        print(f"Product ID: {self.id}")
        print("")