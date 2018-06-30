#! python 3

'''This is a script to align sample-mcas.csv (AKA csv 1) with the format 
	found in sample-mcas-processed.csv (AKA csv 2)'''
	
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle
import datetime

# csv writer...


	
# Print info from csv 1


df = pd.read_csv(r'C:\Users\noona\Desktop\DIT Exercise Details\testing script\sample-mcas.csv', sep=',')

#print(df[:5])

# Isolated columns I need to work with
df2 = df[['district', 'sasid', 'stugrade', 'eperf2', 'mperf2', 'sperf2', 'escaleds', 'mscaleds', 'sscaleds', 'ecpi', 'mcpi', 'scpi']]
print(df2[:7], '\n')

# Checklist: NCESID= Default to 373737; StudentLocalID= Default to missing;	StudentTestID= sasid field;
# StudentGradeLevel= stugrade field; TestDate= Default Apr 1 for ELA May 1 for Math June 1 for Science;
# TestName= Default to MCAS; TestTypeName= Test name w/in cluster default to MCAS ELA MATH or SCIENCE; 
# TestSubjectName= test subject assoc w/name Default to ELA MATH SCIENCE; TestGradeLevel= Default to stugrade field;
# Score1Label= Score type assoc w/subject Default to Perf level Scaled score or CPI; Score1Type= Default to lvl for perf 
# lvl Default to scale for scaled score; Score1Value= value of score type; 
# Performance lvl(mapped)*= 'eperf' 'mperf' 'sperf'; Scaled score= 'escaleds' 'mscaleds'...; CPI= 'ecpi' 'mcpi' 

# Columns we need: sasid, stugrade==?stugrade level, performance level (eperf2)*, cpi(ecpi), level, scale, scaled score (escaleds)
# Level is 1,2,3,4-A, NI, P, F 
# Scale is 0-400 approx.


# I am assuming that score 1= performance level, score2= scaled score, score3= cpi  
# Also each student will have about 3 rows of data for each test: english, math, science

# Rename columns to new format
df3 = df2.rename(index=str, columns={'district':'NCESID','sasid':'StudentTestID','stugrade':'StudentGradeLevel',  
'eperf2':'Score1Value', 'mperf2':'Score1Value-For 2nd next row', 'sperf2':'Score1Value-For 3rd next row', 
'escaleds': 'Score2Value','mscaleds':'Score2Value-For 2nd next row(Math)', 'sscaleds':'Score2Value-For 3rd next row(Science)', 
'ecpi':'Score3Value', 'mcpi':'Score3Value-For 2nd next row(Math)', 'scpi':'Score3Value-For 3rd next row(Science)'})

print(df3[:5])

# Sol'n: https://stackoverflow.com/questions/31888871/pandas-replacing-column-values
df3['Score1Value'].replace(['F','W','NI','P','A','P+'],['1-F','2-W','3-NI','4-P','5-A','6-P+'], inplace=True)
df3.insert(2, 'StudentLocalID', 'missing') # inserted StudentLocalID
df3.drop('NCESID', axis='columns', inplace=True) # drop NCESID
df3.insert(0, 'NCESID', '373737') # insert NCESID
#df3.index.name='DROP'
#df3.set_index('NCESID')
#df3.index.name='DROP'
#df3.reset_index(drop=True)
#df4 = print(df3.to_string(index=False))

#TODO: Drop index numbers

xpos=4 # positioning of columns from here down

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


# Replicate each row 3 times
# sol'n: https://stackoverflow.com/questions/50788508/replicating-rows-in-pandas/50788670?noredirect=1#comment88583906_50788670 

df4 = pd.DataFrame(np.repeat(df3.values,3,axis=0))
df4.columns = df3.columns


##dd = pd.DataFrame(np.repeat['TestTypeName'](df3.values, 3, axis=0))


# Drop column
df4.drop('TestTypeName', axis='columns', inplace=True)



## This is another sol'n for repeating values in column ##
#testss = cycle(['ELA','Math','Science'])
#df4['TestTypeName'] = [next(testss) for tests in range(len(df4))]

#df4.insert(xpos+17, 'TestTypeName', ['ELA', 'Math', 'Science']*2671)

# Insert a new column and repeat values 
df4.insert(xpos+2, 'TestTypeName', ['MCAS ELA', 'MCAS Math', 'MCAS Science']*int(((len(df4))/3))) ##WORKS

df4.drop('TestSubjectName', axis='columns', inplace=True)
df4.insert(xpos+3, 'TestSubjectName', ['ELA', 'Math', 'Science']*int(((len(df4))/3)))

df4['TestGradeLevel'] = df4['StudentGradeLevel'] # Equal to values in stugrade

ELA_Date = datetime.date(2013,4,1)

Math_Date = datetime.date(2013,5,1)

Science_Date = datetime.date(2013,6,1)

#df4.drop('TestDate', axis='columns', inplace=True) #dropping TestDate column before for loop

# for x in df4['TestSubjectName']:
	# if x == 'ELA':
		# df4.insert(xpos+17, 'TestDate', ELA_Date)
	# elif x == 'Math':
		# df4.insert(xpos+17, 'TestDate', Math_Date)
	# elif x == 'Science':
		# df4.insert(xpos+17, 'TestDate', Science_Date)
	# break

### I could just repeat the dates as I did for TestTypeName	
	
	
# df4.insert(xpos+17, 'TestDate', 'place')	
# for i in df4['TestDate']:
	# if df4['TestSubjectName'] == 'ELA':
		# df4.loc[i] = ELA_Date
	# elif df4['TestSubjectName'] == 'Math':
		# df4.loc[i+1] = Math_Date
	# elif df4['TestSubjectName'] == 'Science':
		# df4.loc[i+2] = Science_Date
	# break


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


# If TestSubjectName = ELA then Score2Value = escaleds
# If TestSubjectName = Math then Score2Value = mscaleds
# If TestSubjectName = Science then Score2Value = scaleds


def fix_scores_scale(row):
	if row['TestSubjectName'] == 'ELA':
		val = row['Score2Value']
	elif row['TestSubjectName'] == 'Math':
		val = row['Score2Value-For 2nd next row(Math)']
	elif row['TestSubjectName'] == 'Science':
		val = row['Score2Value-For 3rd next row(Science)']
	return val

df4['Score2Value'] = df4.apply(fix_scores_scale, axis=1)	
	
	
# if TestSubjectName = 'ELA' then Score1Value row = eperf2
# if TestSubjectName = 'Math' then Score1Value row = mperf2
# if TestSubjectName = 'Science' then Score1Value row = sperf2

# if TestSubjectName = 'ELA' then Score3Value = ecpi
# if TestSubjectName = 'Math' then Score3Value = mcpi
# if TestSubjectName = 'Science' then Score3Value = scpi

def fix_scores_cpi(row):
	if row['TestSubjectName'] == 'ELA':
		val = row['Score3Value']
	elif row['TestSubjectName'] == 'Math':
		val = row['Score3Value-For 2nd next row(Math)']
	elif row['TestSubjectName'] == 'Science':
		val = row['Score3Value-For 3rd next row(Science)']
	return val

df4['Score3Value'] = df4.apply(fix_scores_cpi, axis=1)

	

# if df4['TestSubjectName'] == 'ELA':
	# df4['TestDate'] == ELA_Date
# elif df4['TestSubjectName'] == 'Math':
	# df4['TestDate'] == Math_Date
# elif df4['TestSubjectName'] == 'Science':
	# df4['TestDate'] == Science_Date




# df5 = df4.rename(index=str, columns={'Score1Value':'Score1Value ELA'}) # TODO: Rename columns to what they mean


columns_to_drop = ['Score1Value-For 2nd next row','Score1Value-For 3rd next row', 'Score2Value-For 2nd next row(Math)', 
'Score2Value-For 3rd next row(Science)', 'Score3Value-For 2nd next row(Math)', 'Score3Value-For 3rd next row(Science)']

df4.drop(columns_to_drop, axis='columns', inplace=True)


print(df4[:5])


##df4 = df3.iloc[np.arange(len(df3)).repeat(3)] # Other sol'n also repeats row 3 times


# You can add the data set 3 times and groupby StudentTestID


# You can even groupby StudentTestID if necessary


# if 
	# return df3['TestTypeName'] 
# else:
	# return 

# df3['TestTypeName'] = 

# Print dataframe without index: https://stackoverflow.com/questions/24644656/how-to-print-dataframe-without-index







#df4 = df3.loc[df3.index.repeat(df3['StudentTestID'])]
#print(df4[:5])


# Make TestTypeName based on cluster test



# Make TestSubjectName based on cluster test






try:
	df4.to_csv(r'C:\Users\noona\Desktop\DIT Exercise Details\testing script\testing2', sep='\t', encoding='utf-8')	
except IOError as e:
	print('Could not make Excel file' % e)

# Print info from csv 2


# Check data set integrity-describe-and types



# Use SQL to change column names




# Print final product to csv\excel 






# Make a script to process 20, 100, 1000s of similar files
# https://stackoverflow.com/questions/3241804/modify-python-script-to-run-on-every-file-in-a-directory
# https://www.google.com/search?q=how+to+apply+your+python+script+to+many+files&oq=how+to+apply+your+python+script+to+many+files&aqs=chrome..69i57.8217j1j7&sourceid=chrome&ie=UTF-8
	
	# Perhaps use input file selector to select files
	
	