# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import random
from json import JSONDecodeError
import time


def init_inventory_file(name):
    f = open(name, "w+")
    f.close()


def seed_inventory():
    fruits = ["apple", "orange", "orange",
              "pineapple", "tomato",
              "chili", "onion", "peanut",
              "almond", "cashew"]

    with open("inventory.json", "r+") as myfile:
        out = []
        for i in range(0, 10):
            dict = {
                'name': fruits[i],
                'quantity': random.randint(1, 10),
                'price': random.randint(1, 10)
            }
            out.append(dict)
        json.dump(out, myfile)


class MyInventoryClass:
    offset = -1
    INVENTORY_FILE = "inventory.json"
    calculated_file = "inventory_total.json"
    GET_DATA_FILE = "GetSaleForItem.json"
    RECIEVE_DATA_FILE = "RequestItemStat.json"
    data = []

    map_of_last_sell = {}

    def __init__(self):
        self.offset = 0
        init_inventory_file(self.INVENTORY_FILE)
        seed_inventory()
        #init_inventory_file(self.calculated_file)

    def getoffset(self):
        return self.offset

    def setoffset(self):
        self.offset += 1

    def readlines_inventory_total(self):
        with open(self.calculated_file, 'r') as i:
            try:
                self.data = json.load(i)
                print(self.data)
            except JSONDecodeError:
                print("empty file")

    def getCertain_item(self):
        with open(self.GET_DATA_FILE, 'r') as i:
            try:
                curr = json.load(i)
                curr_name = curr[0].get('name')

                f = open(self.calculated_file,'r')
                f2 = open(self.RECIEVE_DATA_FILE, 'r+')
                local_data = json.load(f)
                for m in local_data:
                    if curr_name in m:
                        json.dump(m,f2)
                f.close()
                f2.close()


            except JSONDecodeError:
                print('someError')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starting service")
    my = MyInventoryClass()
    my.readlines_inventory_total()
    time.sleep(2.0)
    my.getCertain_item()
    time.sleep(2.0)
