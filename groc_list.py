class Cart():

    def __init__ (self, dairy, veggies, meat, snacks):
        self.dairy = dairy
        self.veggies= veggies
        self.meat = meat
        self.snacks = snacks


    def kind_dairy(self):
        d = input("Add dairy items here: ")
        self.dairy.append(d)

    def vari_vegg(self):
        v = input("Add Veggies here: ")
        self.veggies.append(v)

    def any_meat(self):
        m = input("Add meats here: ")
        self.meat.append(m)

    def many_snac(self):
        s = input("Add snacks here: ")
        self.snacks.append(s)

    def get_rid(self):
        no_more = input("Is there anything you'd like to remove from the list? ")
        if no_more in self.dairy:
            self.dairy.remove(no_more)
        if no_more in self.veggies:
            self.veggies.remove(no_more)
        if no_more in self.meat:
            self.meat.remove(no_more)
        if no_more in self.snacks:
            self.snacks.remove(no_more)

def run():
    groc_list = Cart([], [], [], [])
    while True:
        print("This is your grocery list: ")
        menu = input("a for add to list, s to show list, r to remove items, q to quit. ")

        if menu == 'q':
            break
        elif menu == 'a':
            groc_list.kind_dairy()
            groc_list.vari_vegg()
            groc_list.any_meat()
            groc_list.many_snac()
        elif menu == 'r':
            groc_list.get_rid()
        elif menu == 's':
            print("Dairy: ", groc_list.dairy)
            print("Veggies: ",groc_list.veggies)
            print("Meat: ",groc_list.meat)
            print("Snacks:",groc_list.snacks)
        
            

run()


  
