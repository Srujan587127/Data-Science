import pandas as pd

data={'OrderID':[101,102,103,104,105,106,107,108],
'CustomerName':['Mike','Sarah','John','Emily','Chris','Jessica','David','Ashley'],
'Category':['Electronics','Clothing','Electronics','Books','Electronics','Clothing','Home','Electronics'],
'Price':[2500,800,1200,350,1800,1500,950,700]}

df=pd.DataFrame(data)
print(df)

print("\norders above 1000")
print(df[df['Price']>1000])

print("\nelectronics orders")
print(df[df['Category']=='Electronics'])

print("\nelectronics and price >1500")
print(df[(df['Category']=='Electronics') & (df['Price']>1500)])