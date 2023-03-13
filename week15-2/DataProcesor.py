class DataProcessor:
    def __init__(self):
        self.vip_customers = dict()
        self.member_customers = dict()
        self.items = dict()

    def vip_excute(self, vip_customer_name, item , price):
        if vip_customer_name not in self.vip_customers:
                self.vip_customers[vip_customer_name] = dict()
        if item not in self.vip_customers[vip_customer_name]:
            self.vip_customers[vip_customer_name][item] = int(price)
        else:
            self.vip_customers[vip_customer_name][item] += int(price)

    def member_excute(self, member_customer_name, item , price):
        if member_customer_name not in self.member_customers:
                self.member_customers[member_customer_name] = dict()
        if item not in self.member_customers[member_customer_name]:
            self.member_customers[member_customer_name][item] = int(price)
        else:
            self.member_customers[member_customer_name][item] += int(price)

    def items_excute(self, item, price):
        if item not in self.items:
            self.items[item] = 0
        else:
            self.items[item] += int(price)