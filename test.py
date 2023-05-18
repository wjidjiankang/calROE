import  pandas as pd

file  = 'historycode.csv'
df = pd.read_csv(file,encoding='gb18030')
print(df)
code1 = df.iloc[0]['股票代码']
print(code1)
df.iloc[0]['股票代码'] =code1 +'ss'
print(df)
