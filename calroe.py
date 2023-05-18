import akshare as ak
import pandas as pd


def main():
    year = '2022'
    # getroe(year)
    mergeroe(year)


def mergeroe(year):
    # for i in range(5):
    '''
    把5年的数据合并到一个dataframe中，并且剔除一些空数据，然后输出到csv文件中
    :return:
    '''
    filename_n = year +'_roe_over15.csv'
    roe_n = pd.read_csv(filename_n, encoding='gb18030')
    roe_n = roe_n.drop (labels='Unnamed: 0', axis=1)
    print(roe_n)

    year_n_1 = str(int(year)-1)
    filename_n_1 = year_n_1 + '_roe_over15.csv'
    roe_n_1 = pd.read_csv(filename_n_1, encoding='gb18030')
    roe_n_1 = roe_n_1.drop(labels='Unnamed: 0', axis=1)
    print(roe_n_1)

    year_n_2 = str(int(year)-2)
    filename_n_2 = year_n_2 + '_roe_over15.csv'
    roe_n_2 = pd.read_csv(filename_n_2, encoding='gb18030')
    roe_n_2 = roe_n_2.drop(labels='Unnamed: 0', axis=1)

    year_n_3 = str(int(year)-3)
    filename_n_3 = year_n_3 + '_roe_over15.csv'
    roe_n_3 = pd.read_csv(filename_n_3, encoding='gb18030')
    roe_n_3 = roe_n_3.drop(labels='Unnamed: 0', axis=1)

    year_n_4 = str(int(year)-4)
    filename_n_4 = year_n_4 + '_roe_over15.csv'
    roe_n_4 = pd.read_csv(filename_n_4, encoding='gb18030')
    roe_n_4 = roe_n_4.drop(labels='Unnamed: 0', axis=1)
    print(roe_n_4)

    roe_4_3 = pd.merge( roe_n,roe_n_1,how='outer')  #合并
    roe_4_3_2 = pd.merge(roe_4_3,roe_n_2,how='outer')
    roe_4_3_2_1 = pd.merge(roe_4_3_2,roe_n_3,how='outer')
    roe_4_3_2_1_0 = pd.merge(roe_4_3_2_1,roe_n_4,how='outer')
    roe = roe_4_3_2_1_0.dropna(axis='rows')      # 清洗没有数据的行

    # print(roe)
    filename = year + '_5Y_roe_over15.csv'
    roe.to_csv(filename, encoding='gb18030')



def getroe(year):
    '''
    把年报中roe超过15的股票选出来
    '''

    date = year +'1231'
    stock_yjbb_em_df = ak.stock_yjbb_em(date=date)
    col_n = ['股票代码','股票简称','净资产收益率']
    df1 = pd.DataFrame(stock_yjbb_em_df,columns=col_n)     # 把一些其他的列去掉

    col_name = 'ROE'+year
    stock_roeover15 = df1[df1.净资产收益率 > 15].copy()
    stock_roeover15.rename(columns={'净资产收益率': col_name}, inplace=True)

   # 代码在储存的时候会变成数字，000100 变成 100，所以加上一些字母
    for i in range(len(stock_roeover15)):
        code = stock_roeover15.iloc[i]['股票代码']
        if code[0] =='6':
            stock_roeover15.iloc[i,0] = code + '.SH'
        if code[0] =='8':
            stock_roeover15.iloc[i,0] = code + '.BJ'
        if code[0] =='0' or code[0] == '3':
            stock_roeover15.iloc[i,0] = code + '.SZ'

    filename = year+'_roe_over15.csv'
    stock_roeover15.to_csv(filename, encoding='gb18030')    # 存起来
    # print( stock_roeover15)


if __name__ == '__main__':
    main()