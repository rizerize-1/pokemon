import pandas as pd

dirtydata = pd.read_csv('data/modified/merged_pokemon.csv')
data = pd.read_csv('data/modified/pokemonML.csv')
combats = pd.read_csv('data/raw_data/combats.csv')

merged_data = pd.merge(combats, data, left_on='First_pokemon', right_on='ID', how='inner')
merged_data.drop(columns=['ID'], inplace=True)
merged_data.rename(columns={c: f"{c}_P1" for c in merged_data.columns[3:]}, inplace=True)

merged_data = pd.merge(merged_data, data, left_on='Second_pokemon', right_on='ID', how='inner')
merged_data.drop(columns=['ID'], inplace=True)
merged_data.rename(columns={c: f"{c}_P2" for c in merged_data.columns[3 + data.shape[1] - 1:]}, inplace=True)

merged_data.to_csv('data/modified/clean_model.csv', index=False)

dirty_data = pd.merge(combats, dirtydata, left_on='First_pokemon', right_on='ID', how='inner')
dirty_data.drop(columns=['ID'], inplace=True)
dirty_data.rename(columns={c: f"{c}_P1" for c in dirty_data.columns[3:]}, inplace=True)

dirty_data = pd.merge(dirty_data, dirtydata, left_on='Second_pokemon', right_on='ID', how='inner')
dirty_data.drop(columns=['ID'], inplace=True)
dirty_data.rename(columns={c: f"{c}_P2" for c in dirty_data.columns[3 + dirtydata.shape[1] - 1:]}, inplace=True)

dirty_data.dropna(inplace=True)

dirty_data.to_csv('data/modified/dirty_model.csv', index=False)