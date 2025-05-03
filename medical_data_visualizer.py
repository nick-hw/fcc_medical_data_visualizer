import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = ((df['weight']/((df['height']/100)**2))>25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol']>=2).astype(int)
df['gluc'] = (df['gluc']>=2).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat_melted = pd.melt(df, id_vars = ['cardio'], value_vars = ['active', 'alco', 'cholesterol', 'gluc','overweight', 'smoke'])

    # 6, 7
    df_cat = df_cat_melted.reset_index().groupby(['variable', 'cardio', 'value']).agg('count').rename(columns={'index': 'total'}).reset_index()
    
    # 8
    fig = sns.catplot(data=df_cat, x = 'variable', y = 'total', col = 'cardio', hue = 'value',kind='bar')

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) 
                 & (df['height'] >= df['height'].quantile(0.025)) 
                 & (df['height'] <= df['height'].quantile(0.975)) 
                 & (df['weight'] >= df['weight'].quantile(0.025)) 
                 & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool), k=0)

    # 14
    fig, ax = plt.subplots(figsize=(6,5))

    # 15
    sns.heatmap(corr, mask=mask, cmap = 'coolwarm', square = True)


    # 16
    fig.savefig('heatmap.png')
    return fig
