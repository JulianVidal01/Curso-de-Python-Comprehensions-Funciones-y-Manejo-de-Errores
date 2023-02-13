import my_functions

def get_total(orders):
  ordenes = my_functions.get_totals(orders)
  suma_ordenes = my_functions.calc_total(ordenes)  
  return suma_ordenes

orders = [4
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)