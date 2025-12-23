"""import pandas as pd

def assert_unique_key(df,key,allow_na=False):
    if not allow_na:
         assert df[key].notna().all(),f"{key} contains NA"
    dup=df[key].duplicated(keep=False)&df[key].notna()
    assert not dup.any(),f"{key}not unique; {dup.sum()}duplicate rows"

def missingness_report(df):
     n=len(df)
     return(df.isna().sum().rename("n_missing").to_frame()
            .assign(p_missing=lambda t:["n_missing"]/n).sort_values("p_missing",ascending=False))

orders=pd.read_parquet("data/processed/ordrs.parquet")
rep=missingness_report(orders)
print(rep.head(5))

orders2=add_missing_flags(orders,["amount","quantity"])
output=orders2[["amount","amount__isna","quantity__isna"]]
print(output.head()) 
#####
#task1"""
