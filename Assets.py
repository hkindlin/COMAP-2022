from Bitcoin import Bitcoin
from Gold import Gold
from Usd import Usd


class Assets:
  def __init__(self):
    self.usd = Usd()
    self.btc = Bitcoin()
    self.gold = Gold()
  
  def sum_accounts(self, btc_price, gold_price):
    return(self.usd.amount + self.btc.to_usd_raw(btc_price) + self.gold.to_usd_raw(gold_price))

  
