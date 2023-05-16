Python version 3.9 at least

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