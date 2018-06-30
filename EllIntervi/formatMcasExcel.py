#! python 3

'''This is a script to convert sample-mcas.csv to the format 
	found in sample-mcas-processed.csv'''
	
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from tkinter.filedialog import askopenfilename
import tkinter.filedialog
import glob


def use_pandas_script(file):	

	df = pd.read_csv(file, sep=',')

	#print(df[:5])

	# Isolated columns I need to work with
	df2 = df[['district', 'sasid', 'stugrade', 'eperf2', 'mperf2', 'sperf2', 'escaleds', 'mscaleds', 'sscaleds', 'ecpi', 'mcpi', 'scpi']]
	print(df2[:7], '\n')


	# Rename columns to new format
	df3 = df2.rename(index=str, columns={'district':'NCESID','sasid':'StudentTestID','stugrade':'StudentGradeLevel',  
	'eperf2':'Score1Value', 'mperf2':'Score1Value-For 2nd next row', 'sperf2':'Score1Value-For 3rd next row', 
	'escaleds': 'Score2Value','mscaleds':'Score2Value-For 2nd next row(Math)', 'sscaleds':'Score2Value-For 3rd next row(Science)', 
	'ecpi':'Score3Value', 'mcpi':'Score3Value-For 2nd next row(Math)', 'scpi':'Score3Value-For 3rd next row(Science)'})

	print(df3[:5])

	xpos=4 # positioning of columns from here down
	
	df3['Score1Value'].replace(['F','W','NI','P','A','P+'],['1-F','2-W','3-NI','4-P','5-A','6-P+'], inplace=True)
	df3.insert(xpos-2, 'StudentLocalID', 'missing') # inserted StudentLocalID
	df3.drop('NCESID', axis='columns', inplace=True) # drop NCESID
	df3.insert(xpos-4, 'NCESID', '373737') # insert NCESID

	df3.insert(xpos, 'TestDate', 'change for tests') #adding in columns
	df3.insert(xpos+1, 'TestName', 'MCAS')
	df3.insert(xpos+2, 'TestTypeName', 'change for tests')
	df3.insert(xpos+3, 'TestSubjectName', 'change for tests')
	df3.insert(xpos+4, 'TestGradeLevel', 'change for tests')
	df3.insert(xpos+5, 'Score1Label', 'Performance Level')
	df3.insert(xpos+6, 'Score1Type', 'Level')
	df3.insert(xpos+10, 'Score2Label', 'Scaled Score')
	df3.insert(xpos+11, 'Score2Type', 'Scale')
	df3.insert(xpos+15, 'Score3Label', 'CPI')
	df3.insert(xpos+16, 'Score3Type', 'Scale')

	print(df3[:7])


	df4 = pd.DataFrame(np.repeat(df3.values,3,axis=0))
	df4.columns = df3.columns


	# Drop column
	df4.drop('TestTypeName', axis='columns', inplace=True)

	# Insert a new column and repeat values 
	df4.insert(xpos+2, 'TestTypeName', ['MCAS ELA', 'MCAS Math', 'MCAS Science']*int(((len(df4))/3))) ##WORKS

	df4.drop('TestSubjectName', axis='columns', inplace=True)
	df4.insert(xpos+3, 'TestSubjectName', ['ELA', 'Math', 'Science']*int(((len(df4))/3)))

	df4['TestGradeLevel'] = df4['StudentGradeLevel'] # Equal to values in stugrade

	ELA_Date = datetime.date(2013,4,1)

	Math_Date = datetime.date(2013,5,1)

	Science_Date = datetime.date(2013,6,1)


	# Inserts test date based on value from TestSubjectName column	
	def fix_date(row):
		if row['TestSubjectName'] == 'ELA':
			val = ELA_Date
		elif row['TestSubjectName'] == 'Math':
			val = Math_Date
		elif row['TestSubjectName'] == 'Science':
			val = Science_Date
		return val
		
	df4['TestDate'] = df4.apply(fix_date, axis=1)


	def fix_scores_perf(row):
		if row['TestSubjectName'] == 'ELA':
			val = row['Score1Value']
		elif row['TestSubjectName'] == 'Math':
			val = row['Score1Value-For 2nd next row']
		elif row['TestSubjectName'] == 'Science':
			val = row['Score1Value-For 3rd next row']
		return val
		
	df4['Score1Value'] = df4.apply(fix_scores_perf, axis=1)


	def fix_scores_scale(row):
		if row['TestSubjectName'] == 'ELA':
			val = row['Score2Value']
		elif row['TestSubjectName'] == 'Math':
			val = row['Score2Value-For 2nd next row(Math)']
		elif row['TestSubjectName'] == 'Science':
			val = row['Score2Value-For 3rd next row(Science)']
		return val

	df4['Score2Value'] = df4.apply(fix_scores_scale, axis=1)	
		

	def fix_scores_cpi(row):
		if row['TestSubjectName'] == 'ELA':
			val = row['Score3Value']
		elif row['TestSubjectName'] == 'Math':
			val = row['Score3Value-For 2nd next row(Math)']
		elif row['TestSubjectName'] == 'Science':
			val = row['Score3Value-For 3rd next row(Science)']
		return val

	df4['Score3Value'] = df4.apply(fix_scores_cpi, axis=1)


	columns_to_drop = ['Score1Value-For 2nd next row','Score1Value-For 3rd next row', 'Score2Value-For 2nd next row(Math)', 
	'Score2Value-For 3rd next row(Science)', 'Score3Value-For 2nd next row(Math)', 'Score3Value-For 3rd next row(Science)']

	df4.drop(columns_to_drop, axis='columns', inplace=True)


	print('Last print of data\n',df4[:5])
	
	return df4
				
