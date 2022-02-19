class Usd:
  def __init__(self) -> None:
    self.amount = 1000

  def to_btc(self, amount, current_price) -> float:
    if(amount <= self.amount):
      self.amount = self.amount - amount
      return((amount * current_price) * .98)
    else: raise TypeError("Amount exceeds amount in account")

  def to_gold(self, amount, current_price) -> float:
    if(amount <= self.amount):
      self.amount = self.amount - amount
      return((amount * current_price) * .99)
    else: raise TypeError("Amount exceeds amount in account")

  
