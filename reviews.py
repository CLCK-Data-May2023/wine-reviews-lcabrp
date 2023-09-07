# add your code here
import pandas as pd

# Read the zip compressed csv into a dataframe
reviews = pd.read_csv(r"data\winemag-data-130k-v2.csv.zip", index_col=0, compression='zip')

# Perform group by operations to calculate the number of reviews and average points per country
summary_review = reviews.groupby('country').agg({'points': ['count', 'mean']})

# Remove the multi-index
summary_review = summary_review.reset_index()

# Matching column names with the requirements
summary_review.columns = ['country', 'count', 'points']

summary_review = summary_review.sort_values(by='count', ascending=False) # Required order
summary_review['points'] = summary_review['points'].round(1)# One decimal point

# Writing the summary dataframe to the new csv
summary_review.to_csv('data/reviews-per-country.csv', index=False)