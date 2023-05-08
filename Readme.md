Python version 3.9 at least

My application will seed and inventory and write a json dump to a inventory.json file

My application will read from inventory_total.json files as well and output the latest quantity purchases in my application

If you need to clear the state just delete the inventory_total.json file

For my microservice I read and store the date locally that it can be retrieved by name:

REQUEST state of a certain inventory ITEM:
Write to GetSaleForItem.json file

RECIEVE state from RequestItemStat.json

```python
python main.py
```