#! python3

from tkinter.filedialog import askopenfilename
import pandas as pd
import matplotlib.pyplot as plt


# Read the excel file
# Asks for user to select file
print('Select the file you want to use')
data = pd.ExcelFile(askopenfilename())

# Define columns to be read
columns1 = ['Income (USD)', 'Tax amt', 'After taxes', '%tax amt']

data_tax_pct = data.parse(u'Sheet1', skiprows=1, names=columns1)

print(data_tax_pct)

# Plot all
data_tax_pct.plot()
plt.show()

# Plot Income(USD) vs %tax amt
data_tax_pct['Income (USD)'].plot(label = 'Income')
data_tax_pct['%tax amt'].plot(label = '%tax amt')
plt.legend(loc = 'upper right')
plt.show()

# Plots a bar graph version--missing %tax amt??
data_tax_pct.plot.bar()
plt.show()

