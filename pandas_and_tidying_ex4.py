sampleruns.index.name = None
mutations.index.name = None
merged_df = pd.merge(
    sampleruns,
    mutations,
    left_on = ['Strain ID', 'Population', 'Generation'],
    right_on = ['Strain ID', 'Population', 'Generation'],
    how = 'left',
)
