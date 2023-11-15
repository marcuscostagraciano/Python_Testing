import numpy as np
import pandas


def replace_comma(data: str) -> float:
    return float(data.replace(',', '.'))


"""
# Currency
df = pandas.read_csv('data/dimcurrency.csv', sep=';')
df.to_csv('data/dimcurrency.csv', index=False)

# Date
df = pandas.read_csv('data/dimdate.csv', sep=';')
df.to_csv('data/dimdate.csv', index=False)

# Product
df = pandas.read_csv('data/dimproduct.csv', sep=';')
df = df.fillna(np.nan).replace([np.nan], [None])
df.to_csv('data/dimproduct.csv', index=False)

# Sales Reason
df = pandas.read_csv('data/dimsalesreason.csv', sep=';')
df.to_csv('data/dimsalesreason.csv', index=False)

# Special Offer
df = pandas.read_csv('data/dimspecialoffer.csv', sep=';')
df['discountPercentage'] = (df['discountPercentage'].apply(replace_comma))\
                                .astype('float64')
df.to_csv('data/dimspecialoffer.csv', index=False)

# Territory
df = pandas.read_csv('data/dimterritory.csv', sep=';')
df.to_csv('data/dimterritory.csv', index=False)

# Fact Sales
df = pandas.read_csv('data/factsales.csv', sep=';')
df = df.fillna(np.nan).replace([np.nan], [None])

df['taxes'] = (df['taxes'].apply(replace_comma)).astype('float64')
df['salesAmount'] = df['salesAmount'].astype('float64')
df['unitPrice'] = (df['unitPrice'].apply(replace_comma)).astype('float64')
df['discounts'] = (df['discounts'].apply(replace_comma)).astype('float64')
df['discounts'] = df['discounts'] * df['unitPrice']
df['dateKey'] = df['dateKey'].replace(0, 1)

df.to_csv('data/factsales.csv', index=False)
"""
