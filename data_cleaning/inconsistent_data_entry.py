import pandas as pd
import numpy as np

import fuzzywuzzy
from fuzzywuzzy import process
import chardet

professors = pd.read_csv("../input/pakistan-intellectual-capital/pakistan_intellectual_capital.csv")
np.random.seed(0)
print(professors.head())

countries = professors['Country'].unique()
countries.sort()
print(countries)

professors['Country'] = professors['Country'].str.lower()
professors['Country'] = professors['Country'].str.strip()

# get the top 10 closest matches to "south korea"
matches = fuzzywuzzy.process.extract("south korea", countries, limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)
print(matches)


# function to replace rows in the provided column of the provided dataframe
# that match the provided string above the provided ratio with the provided string
def replace_matches_in_column(df, column, string_to_match, min_ratio=47):
    strings = df[column].unique()
    matches = fuzzywuzzy.process.extract(string_to_match, strings,
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]
    rows_with_matches = df[column].isin(close_matches)
    df.loc[rows_with_matches, column] = string_to_match
    print("All done!")

replace_matches_in_column(df=professors, column='Country', string_to_match="south korea")
