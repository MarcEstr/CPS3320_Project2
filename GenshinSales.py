# This program is used to show how much money each limited character made from Genshin Impact.

from matplotlib import pyplot as plt

#Import both numpy and pandas
import numpy as np
import pandas as pd


plt.style.use('ggplot')

data = pd.read_csv('GenshinSales.csv')
df = pd.DataFrame(data)

# Calculate each character sales and round it to the millions.
a = df['Sales']
a2 = a * 1

xmax = np.max(a2)
fig = plt.figure(figsize=(10,5))
plt.barh(df['Character'],a2) 


#Labeling
plt.title('Genshin Impact: Limited Character Sales')
plt.xlabel('Sales (per Million USD)')
plt.ylabel('Character')


#Parameters
plt.tick_params(axis = 'x', which='major', labelsize=10)
plt.show()
