class Menu:
    menu = {
        "juice": 10000,
        "soft_drink": 15000,
        "chicken": 30000,
        "beef": 45000,
        "tea": 10000,
        "desert": 25000
    }

    def __init__(self, order):
        self.order = order
    
    def create_order(self):
        dic = {}
        for i in self.order:
            i = i.strip()
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        return dic

    def output(self, created_order):
        print('List Belanja')
        total = 0
        for i in created_order.keys():
            sub_total = self.menu[i] * created_order[i]
            print(f'\t {created_order[i]} {i} @ {self.menu[i]} = {sub_total}')
            total += sub_total
        print(f'Total Harga: {total}')


inp = Menu(str(input("Enter menu (separated by ','): ")).split(','))
order_list = inp.create_order()
inp.output(order_list)
