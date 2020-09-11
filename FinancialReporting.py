import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = "Financial Reporting.xlsx"
df = pd.read_excel(excel_file_path)
print(df)

# The Code Below is to identify the column names in the excel file
#df = pd.read_excel(excel_file_path)
#print(df.columns)

# The code below is to get information about the number of rows, column and information about data in the cell
#df = df.info()
#print(df)


df_plot = df.loc[(df['Country'] == 'United States of America') & (df['Product'] == 'Carretera') & (df['Segment'] == 'Midmarket')]
df_plot = df_plot.sort_values(by=['Date'])

#df_plot.plot(x='Month Name', y='Profit')
#plt.show()

df_products = df.groupby(['Country']).sum()
df_products['Profit'].plot.pie()
plt.show()
