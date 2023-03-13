import re
from DataProcesor import DataProcessor

def main():
    data_processor = DataProcessor()
    open_file("./log.txt", data_processor)
    write_file("./analysis_result.txt", data_processor)

def open_file(file_name, data_processor):
    with open(file_name, 'r') as file:
        for line in file.readlines():
            line = line.rstrip()
            if re.search('^\[VIP\]', line):
                vip_customer_name = line.split(' ')[1]
                item = line.split(' ')[3]
                price = line.split(' ')[5].replace("$", "")
                
                data_processor.vip_excute(vip_customer_name, item, price)
            else:
                member_customer_name = line.split(' ')[0]
                item = line.split(' ')[2]
                price = line.split(' ')[4].replace("$", "")

                data_processor.member_excute(member_customer_name, item, price)
            
            data_processor.items_excute(item, price)

def write_file(file_name, data_processor):
    with open(file_name, 'w+') as file:
        file.write("[VIP]\n")
        for vip_customer_name, data in data_processor.vip_customers.items():
            file.write(f"{vip_customer_name} buys ")

            temp = []
            for item, price in data.items():
                temp.append(f"{item}: {price}")
            
            file.write(", ".join(temp)+"\n")

        file.write("\n[Member]\n")
        for member_customer_name, data in data_processor.member_customers.items():
            file.write(f"{member_customer_name} buys ")

            temp = []
            for item, price in data.items():
                temp.append(f"{item}: {price}")

            file.write(", ".join(temp)+"\n")

        file.write("\n")
        for item, total_price in data_processor.items.items():
            file.write(f"Total {item} sales: {total_price}\n")

main()