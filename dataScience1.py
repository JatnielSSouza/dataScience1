import pandas as pd

url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv"  # Fix the spacing in the URI
bebidas = pd.read_csv(url, on_bad_lines='skip', encoding='latin-1')  # Replace 'error_bad_lines' with 'on_bad_lines' and set it to 'skip' to ignore bad lines.
print(bebidas)
bebidas.columns = ["pais", "cervejas", "destilados", "vinhos", "total"]
print(bebidas)
print(bebidas.describe())
print(bebidas["cervejas"].mean())
print(bebidas["cervejas"].median())
print(bebidas["cervejas"].describe())
