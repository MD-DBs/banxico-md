import pandas as pd
from extract import extract
from df_utils import order, save, stationarize_panel, slice_df_from_date, remove_outliers, apply_transformations, set_date_index

if __name__ == "__main__":
    # Extract the data from the data source API
    df = extract()
    
    print(df)
    (
        df.pipe(order)
        .pipe(save)
        .pipe(set_date_index)
        .pipe(slice_df_from_date, start_date='2000-01-01')
        .pipe(stationarize_panel, ['SP74663', 'SF4782'])
        .pipe(remove_outliers, ['SP74663', 'SF4782'])
        .pipe(apply_transformations)
        .pipe(save, prefix='balanced_', index=True)
    )
