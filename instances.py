import store
import products

costco = store.Store("Costco")
cheerios = products.Product("Cheerios", 5, "Cereal", 333)
frosted_flakes = products.Product("Frosted Flakes", 6, "Cereal", 444)
whole_milk = products.Product("Whole Milk", 4, "Milk", 229)

costco.add_product(whole_milk)
costco.add_product(cheerios)
costco.add_product(frosted_flakes)

cheerios.print_info()
frosted_flakes.print_info()
whole_milk.print_info()

costco.inflation(.05)
costco.set_clearance("Cereal", .3)
costco.sell_product(333)