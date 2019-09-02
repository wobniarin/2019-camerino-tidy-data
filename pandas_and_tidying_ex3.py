# Removing the Strain ID duplicated column on mutations2
mutations2 = mutations.drop(['Strain ID'], axis=1)

# Removing the Strain ID duplicated column on sampleruns2
sampleruns2 = sampleruns.drop(['Strain ID'], axis=1)

# Inner joint on both dataframes considering 3 columns to check unique values 
print(pd.merge(sampleruns2, mutations2, on = ['Strain ID', 'Population', 'Generation']))
