import pandas as pd

df = pd.read_csv('books_data/books.csv', sep=';', encoding='latin-1', low_memory=False)
cleaned_df = df.drop(columns=['Image-URL-M','Image-URL-L'], axis=1)
cleaned_df.to_csv('cleaned_books.csv', index=False)