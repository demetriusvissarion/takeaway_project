class Order:
    def __init__(self):
        self.menu = ['Fish and chips - £12', 'English breakfast - £10']

    def show_menu(self):
        return self.menu
    
    def build_numbered_menu(self):
        self.numbered_menu = []
        counter = 1
        for item in self.menu:
            self.numbered_menu.append(str(counter) + ': ' + item)
            counter += 1
        return self.numbered_menu
    
    def build_order(self):
        print(self.numbered_menu)
        self.itemised_receipt = []
        self.food_and_quantity = input('Enter menu item number and quantity, example: 13 for three portions of "Fish and chips":')
        # print('int(self.food_and_quantity[0]): ', int(self.food_and_quantity[0]))
        # print('int(self.food_and_quantity[1]): ', int(self.food_and_quantity[1]))
        if int(self.food_and_quantity[0]) not in range(1, 3):
            raise Exception("There is no item menu with that number")
        elif int(self.food_and_quantity[1]) not in range(1, 6):
            raise Exception("Wrong quantity, you can only order minimum 1 and maximum 5 of each item")
        else: 
            self.itemised_receipt.append(f'{str(self.food_and_quantity[1])}x' + self.numbered_menu[int(self.food_and_quantity[0]) - 1][2:-3] + f'£{int(self.food_and_quantity[1]) * int(self.numbered_menu[int(self.food_and_quantity[0]) - 1][-2:])}')
            return self.itemised_receipt