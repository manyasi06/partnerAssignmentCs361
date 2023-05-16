# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hashlib
import json
import math
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


def seed_compound_interest():
    with open('calculator_input.json', 'w+') as myfile:
        out = []
        for i in range(0, 4):
            dict = {
                'amount': 5,
                'rate': .3,
                'time': 5,
                'years': random.randint(1, 10)
            }
            out.append(dict)
        json.dump(out, myfile)


def readFromInput():
    map_set = []
    current_file_hash = None
    init = False

    while True:
        fileIn = open('calculator_input.json', 'rb')
        curr_hash = hashlib.md5(fileIn.read()).hexdigest()
        print(curr_hash)
        if (current_file_hash == None and init == False) or curr_hash == current_file_hash:
            print("File hasn't changed")
            if current_file_hash == None:
                current_file_hash = curr_hash
                init = True
        else:

            with open('calculator_input.json', 'r') as myfile:
                try:
                    local_data = json.load(myfile)
                    out = []
                    for i in local_data:
                        principal = i['amount']
                        rate = float(i['rate'])
                        time_compound_a_year = i['time']
                        years = i['years']
                        amt = principal * math.pow((1 + rate / time_compound_a_year), time_compound_a_year * years)

                        out.append({'total_amount': amt, 'interest_earned': amt - principal})
                    f = open('calculator_output.json', 'w+')
                    json.dump(out, f)
                    f.close()
                except JSONDecodeError:
                    pass
            current_file_hash = curr_hash
        fileIn.close()
        time.sleep(2.0)


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
        # init_inventory_file(self.calculated_file)

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

                f = open(self.calculated_file, 'r')
                f2 = open(self.RECIEVE_DATA_FILE, 'r+')
                local_data = json.load(f)
                for m in local_data:
                    if curr_name in m:
                        json.dump(m, f2)
                f.close()
                f2.close()


            except JSONDecodeError:
                print('someError')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starting service")
    # seed_compound_interest()
    readFromInput()
    # my = MyInventoryClass()
    # my.readlines_inventory_total()
    # time.sleep(2.0)
    # my.getCertain_item()
    # time.sleep(2.0)
