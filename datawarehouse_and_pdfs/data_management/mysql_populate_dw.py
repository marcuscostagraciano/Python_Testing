import sys
sys.path.append(r"T:\\GitHub\\Python_Testing\\datawarehouse_and_pdfs\\")

import pandas                                               # noqa: E402
import mysql.connector                                      # noqa: E402
from configs.config import DATABASE_NAME, USER              # noqa: E402


cursor_config = {
    'user': USER,
    'database': DATABASE_NAME,
}


# cnx = mysql.connector.connect(**cursor_config)
# cursor = cnx.cursor()


df = pandas.read_csv('cleaned_factsales.csv')

print(df.head())
# print(df.dtypes)

# list_df = df.values.tolist()


# query = ('INSERT INTO factsales(CurrencyKey,DateKey,ProductKey,SalesReasonKey,SpecialOfferKey,TerritoryKey,productAmount,discounts,taxes,salesAmount,unitPrice)'
#          'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')

# for item in list_df:
#     ...
    # print(item)
    # cursor.execute(query, item)
    # cnx.commit()

# cursor.executemany(query, list_df)
# cnx.commit()

# cursor.close()
# cnx.close()
