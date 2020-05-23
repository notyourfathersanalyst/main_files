import os
import pandas as pd 

# https://www.marsja.se/pandas-read-csv-tutorial-to-csv/,
# https://www.marsja.se/pandas-dataframe-read-csv-excel-subset/ data frames tutorials
# https://honingds.com/blog/pandas-read_csv/
# index_col = vilken kolumn jag börjar och ska inkludera
# nrows = vilka rader
df = pd.read_excel(r"C:/Users/Tim/Desktop/Concepts.xlsx", # kan läsa filer fårn URLs
                   sheet_name="Concepts", 
                   usecols = [1, 8, 7],
                   nrows=10,
                   header=0
                   )
# =============================================================================
#                    index_col=[1, 7], 
#                    header=0)
# =============================================================================
# =============================================================================
# df.to_excel("Nyfil.xlsx", sheet_name="NewName", index=False) skapa ny excel
# fil med data
# =============================================================================

df.to_excel("Nyfil.xlsx", sheet_name="NewName", index=False) #skapa ny excel


print(df)
   