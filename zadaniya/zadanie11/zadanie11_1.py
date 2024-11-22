import pandas as pd
#1
df = pd.read_csv('NISPUF17.csv', sep=',')
print(df["EDUC1"].unique())
def proportion_of_education(dataframe):
    prop_of_educ = dict()
    len_of_df = len(df)

    less_12 = round(float(df["EDUC1"].where(df["EDUC1"] ==1).count() / len_of_df),2)
    eq_12 = round(float(df["EDUC1"].where(df["EDUC1"] ==2).count() / len_of_df),2)
    more_12 = round(float(df["EDUC1"].where(df["EDUC1"] ==3).count() / len_of_df),2)
    college = round(float(df["EDUC1"].where(df["EDUC1"] ==4).count() / len_of_df),2)
    

    prop_of_educ = {"less than 12": less_12,
                    "12": eq_12,
                    "more than 12": more_12,
                    "college": college}
    print(prop_of_educ)
proportion_of_education(df)
