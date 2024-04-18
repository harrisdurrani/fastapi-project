import csv
import pandas as pd

# new_file = "cleaned_books.csv"



# with open('books_data/books.csv', newline='') as file:
#     # columns = ["ISBN","Book-Title","Book-Author","Year-Of-Publication","Publisher","Image-URL-S","Image-URL-M","Image-URL-L", 'text1', 'text2', 'text3']
#     reader = csv.reader(file, delimiter=';')
#     first_row = next(reader)

#     df = pd.DataFrame(reader, columns=["ISBN","Book-Title","Book-Author","Year-Of-Publication","Publisher","Image-URL-S","Image-URL-M","Image-URL-L", 'text1', 'text2', 'text3'])
# cleanded_df = df.drop(columns=['text1', 'text2', 'text3'], axis=1)


# print(cleanded_df)


df = pd.read_csv('books_data/books.csv', sep=';', encoding='latin-1')
print(df.to_string())