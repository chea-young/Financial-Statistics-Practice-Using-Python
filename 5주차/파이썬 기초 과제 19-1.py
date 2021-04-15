#%% [과제 19-1] subset_iloc_range=df.iloc[[0,9,99],[0,3,5]]동일한 결과를 주는 코드를 
# loc속성을 이용하여 작성하시오.
import pandas as pd
df=pd.read_csv('gapminder.tsv', sep='\t')


subset_loc = df.loc[[0, 9, 99], ['country', 'lifeExp', 'gdpPercap']]
print(subset_loc )
print("---------------------")
# %%
