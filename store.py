class Store:

    def __init__(self, name:str, product_list = []):
        self.name = name
        self.product_list = product_list

    def add_product(self, new_product:str):
        self.product_list.append(new_product)
        print (f"{self.name} product list:")
        for x in range(0, len(self.product_list)):
            print(self.product_list[x].name)
        print("")
        return self

    def sell_product(self, id):
        for x in range(len(self.product_list)):
            if self.product_list[x].id == id:
                del self.product_list[x]
                break
        print (f"New {self.name} product list:")
        for y in range(0, len(self.product_list)):
            print(self.product_list[y].name)
        print("")
        return self

    def inflation(self, percent_increase):
        for x in range(0,len(self.product_list)):
            self.product_list[x].price += ((self.product_list[x].price) * percent_increase)
            print(f"New price for {self.product_list[x].name}: ${self.product_list[x].price:.2f}")
        print("")
        return self
    
    def set_clearance(self, category:str, percent_discount):
        for x in range(0,len(self.product_list)):
            if (self.product_list[x].category == category):
                self.product_list[x].price -= ((self.product_list[x].price) * percent_discount)
                print(f"New price for {self.product_list[x].name}: ${self.product_list[x].price:.2f}")
        print("")
        return self