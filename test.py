import pandas as pd

def get_past_means(data, index, col_name):
  df = pd.DataFrame(data)
  return(df[col_name].mean())