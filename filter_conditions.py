import pandas as pd

def get_range_mask(df, column):
    max_val = input(f'{column}の上限:')
    min_val = input(f'{column}の下限:')

    max_val = float(max_val) if max_val.strip() != '' else None
    min_val = float(min_val) if min_val.strip() != '' else None
    
    if max_val is not None and min_val is not None:
        mask = (df[column] <= max_val) & (df[column] >= min_val)
    elif max_val is not None and min_val is None:
        mask = (df[column] <= max_val)
    elif max_val is None and min_val is not None:
        mask = (df[column] >= min_val)
    else:
        mask = pd.Series(True, index=df.index)
    return mask

def get_2choices_mask(df,column):
    choise = input(f'{column}のYes/No:')
    choise = choise.strip().lower()

    if choise == 'yes':
        mask = (df[column] == 'yes')
    elif choise == 'no':
        mask = (df[column] == 'no')
    else:
        mask = pd.Series(True, index=df.index)
    return mask

