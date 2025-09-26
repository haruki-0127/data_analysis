import pandas as pd
from filter_conditions import get_range_mask, get_2choices_mask
from stats_output import calc_stats, output_stats, output_counts

def main():
    file_name = input("ファイル名：")
    df = pd.read_csv(file_name)

    mode = input("複数条件（and / or）: ").strip().lower()

    numeric_columns = ["縦幅(cm)", "横幅(cm)", "体重(g)", "触覚本数"]
    masks = []

    for col in numeric_columns:
        mask = get_range_mask(df, col)
        masks.append(mask)

    choices_columns = ["食事", "目の潰れ"]
    for col in choices_columns:
        mask = get_2choices_mask(df, col)
        masks.append(mask)
    
    if mode == "or":
        combined_mask = pd.Series(False, index=df.index)
        for m in masks:
           if m.all():   
             continue
           combined_mask |= m
    else:
        combined_mask = pd.Series(True, index=df.index)
        for m in masks:
           combined_mask &= m


    filtered_df = df[combined_mask]

    stats = calc_stats(filtered_df)
    output_stats(stats)
    output_counts(filtered_df)

if __name__ == "__main__":
   main()







