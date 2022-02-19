import pandas as pd

def in_usd(amount, current_price):
  return(amount * current_price)

def transaction_cost(amount, currency):
  if currency.to_lower() == "btc":
    return(amount * 0.02)
  elif currency.to_lower() == "gold":
    return(amount * 0.01)
  else: raise ValueError("incorrect currency")

def compute():
  if(curent_score > prev_score):
    buy_amount = max( , )
    if(transaction_cost(buy_amount, curr) <= in_usd(buy_amount, curr_pc)):
      pass
    else: return(buy_amount)
  
df = pd.DataFrame()