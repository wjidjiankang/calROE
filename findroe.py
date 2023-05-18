import akshare as ak
import pandas as pd


def main():
    year = '2022'
    file  = 'historycode.csv'
    df = pd.read_csv(file,encoding='gb18030')
    # print(df)
    list_code = df['股票代码'].values
    # print(list)
    list_code_no_suffix = []

    # 去掉 code中的后缀 .sh.sz等
    for i in range(len(list_code)):
        list_code_no_suffix.append(list_code[i][0:6])
    # print(list_code_no_suffix)

    roe_list = []
    date = year + '1231'
    stock_yjbb_em_df = ak.stock_yjbb_em(date=date)

    # 获取相应code对应的roe
    n = len(list_code_no_suffix)


    for i in range(n):
        index = stock_yjbb_em_df[(stock_yjbb_em_df.股票代码 == list_code_no_suffix[i])].index.tolist()
        roe = stock_yjbb_em_df.iloc[index]['净资产收益率'].values[0]
        roe_list.append(roe)

    col_name = 'ROE'+year
    df_roe  = pd.DataFrame()
    df_roe['code'] = list_code
    df_roe[col_name] = roe_list
    print(df_roe)

    file_name = 'historycode_' + year +'_roe.csv'
    df_roe.to_csv(file_name,encoding='gb18030')


if __name__ == '__main__':
    main()