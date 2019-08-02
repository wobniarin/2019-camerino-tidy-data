# IPython log file


sales14 = pd.read_excel('house-sales.xlsx', sheet_name='untidy data', header=True, usecols='B:J', index_col=0, skiprows=list(range(4)), nrows=3, parse_dates=['sale date 1', 'sale date 2'])
sales14 = pd.read_excel('house-sales.xlsx', sheet_name='untidy data', header=0, usecols='B:J', index_col=0, skiprows=list(range(4)), nrows=3, parse_dates=['sale date 1', 'sale date 2'])
sales14
sales14['sale date 1']
sales14['sale date 2']
sales14 = pd.read_excel('house-sales.xlsx', sheet_name='untidy data', header=0, usecols='B:J', index_col=0, skiprows=list(range(4)), nrows=3)
sales14['sale date 2']
sales14['sale date 1']
sales14 = pd.read_excel('house-sales.xlsx', sheet_name='untidy data', header=True, usecols='B:J', index_col=0, skiprows=list(range(4)), nrows=3, parse_dates=False)
sales14 = pd.read_excel('house-sales.xlsx', sheet_name='untidy data', header=0, usecols='B:J', index_col=0, skiprows=list(range(4)), nrows=3, parse_dates=False)
sales14['sale date 1']
