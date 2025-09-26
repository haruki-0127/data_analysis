import pandas as pd
from tabulate import tabulate

def calc_stats(df):
    numeric_columns = ["縦幅(cm)", "横幅(cm)", "体重(g)", "触覚本数"]
    numeric_df = df[numeric_columns]

    stats = pd.DataFrame({
        '個体数': numeric_df.count(),
        '平均': numeric_df.mean(),
        '中央値': numeric_df.median(),
        '標準偏差': numeric_df.std(),
        '最大': numeric_df.max(),
        '最小': numeric_df.min()
    }).T
    return stats

def output_stats(stats, output_path='filtered_stats.csv'):
    stats.to_csv(output_path, encoding='cp932')
    print('【数値データの各統計量】')
    print(tabulate(stats, headers='keys', tablefmt='grid'))

def output_counts(df):
    counts1 = df['食事'].value_counts()
    counts2 = df['目の潰れ'].value_counts()

    print('【食事した個体の割合】')
    print(counts1)
    print('【目の潰れの割合】')
    print(counts2)