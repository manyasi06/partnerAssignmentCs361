Python version 3.9 at least

My application will seed and inventory and write a json dump to a inventory.json file

My application will read from inventory_total.json files as well and output the latest quantity purchases in my application

If you need to clear the state just delete the inventory_total.json file

For my microservice I read from the inventory_json.txt and store the date locally.
To get data from my service you write getsaleforitem.json the actual item like 'apple' that it can be retrieved by name and written to pipe file:
RequestItemStat.json

REQUEST state of a certain inventory ITEM:
Write to GetSaleForItem.json file

RECIEVE state from RequestItemStat.json

```python
python main.py
```

### Updated

Service is the compound interest service:
Input is json array
Note rate should be a decimal string number from 0 to 1
```json
[
  {
    "amount": 100,
    "rate": ".05",
    "time": 1,
    "years": 3
  }
]
```

Write the following to ```calculator_input.json``` file for input request pipe

To read from the service the result of calculated compound interest amount go to the ```calculator_output.json``` file which out put the following:
```json
[{"total_amount": 115.76250000000002, "interest_earned": 15.762500000000017}]
```

To run the application:
```python
main.py
```