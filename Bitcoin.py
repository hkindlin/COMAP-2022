class Bitcoin:
  def __init__(self) -> None:
    self.amount = 0

  def to_usd(self, amount, current_price) -> float:
    if(amount <= self.amount):
      return((amount * current_price) * 0.98)
    else: raise TypeError("Amount exceeds amount in account")

  def to_usd_raw(self, current_price) -> float:
    return(self.amount*current_price)
