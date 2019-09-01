# IPython log file

#TODO: find source webpage of the cost of publishing

subs15 = pd.read_excel(
    'data/Journalsubscost20152016v6.xlsx',
    sheet_name='2015',
    header=0,
    index_col=None,
    nrows=153,
    usecols='A:I'
).rename({'Unnamed: 0': 'university'}, axis=1)
subs15t = pd.melt(
    subs15, id_vars='university', var_name='publisher', value_name='cost'
)
subs15t['year'] = 2015

subs16 = pd.read_excel(
    'data/Journalsubscost20152016v6.xlsx',
    sheet_name='2016',
    header=0,
    index_col=None,
    nrows=153,
    usecols='A:I'
).rename({'Unnamed: 0': 'university'}, axis=1)
subs16t = pd.melt(
    subs16, id_vars='university', var_name='publisher', value_name='cost'
)
subs16t['year'] = 2016

subs10 = pd.read_excel(
    'data/Journal_publishing_cost_FOIs_UK_universities.xlsx',
    sheet_name='Responses',
    header=(0, 1),
    nrows=154
).rename(
    {'Unnamed: 0_level_0': 'university',
     'Unnamed: 0_level_1': 'university'},
    axis=1
)
subs10y = pd.melt(
    subs10,
    id_vars=[('university', 'university')],
    var_name=['publisher', 'year'],
    value_name='cost'
).rename({('university', 'university'): 'university'}, axis=1)

subs = pd.concat((subs10y, subs15t, subs16t), axis=0, sort=True)

subs.to_csv('data/publishers.csv', index=False)
gb = subs.groupby('year')
subs.query('publisher == "Elsevier"').groupby('year').agg(cost=('cost', 'sum'))

sns.barplot( 
    data=subs.groupby(['publisher', 'year']).sum().reset_index(), 
    x='year', 
    y='cost', 
    hue='publisher' 
)

sns.lineplot(
    data=subs.groupby(['publisher', 'year']).sum().reset_index(),
    x='year',
    y='cost',
    hue='publisher'
)


# Some numbers to compare:
#   - Annual Wellcome Trust grants: About £650M.
#   - Annual UK R&D expenditure: About £11B.
