#! python3

from formatMcasExcel import use_pandas_script
from tkinter.filedialog import askopenfilename
import tkinter
import tkinter.filedialog
import glob



filename = tkinter.filedialog.askdirectory()

		
target_directory = (filename)
file_list = glob.glob(target_directory + "/*.csv")

print(file_list)

# Loop files
for file in file_list:                
	df_result = use_pandas_script(file)   
	new_filename = file.replace('.csv', '_processed.csv')
	df_result.to_csv(new_filename, index=False)
	print(df_result.info())
