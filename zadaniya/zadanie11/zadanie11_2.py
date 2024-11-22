import pandas as pd
df = pd.read_csv('NISPUF17.csv', sep=',')
print(df["CBF_01"].unique())
def aid(dataframe): #average influenza doses
    df["CBF_01"]=df["CBF_01"].replace(1,"Yes", regex=True)
    df["CBF_01"]=df["CBF_01"].replace(2,"No", regex=True)
    df["CBF_01"]=df["CBF_01"].replace(77,"Dont know", regex=True)
    df["CBF_01"]=df["CBF_01"].replace(99,"miss", regex=True)

bm=df.groupby("CBF_01")["P_NUMFLU"].mean()
bm_turtle = (round(float(bm[1]),2), round(float(bm[2]),2))
print(bm_turtle)