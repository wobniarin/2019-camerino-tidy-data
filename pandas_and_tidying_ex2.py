# answers to the second exercise

# Setting Strain ID as an index
mutations.index = mutations['Strain ID']

# Slicing the dataframe and printing it
print(mutations.loc[['REL11345'], ['Population', 'Generation', 'Total Mutations']])
