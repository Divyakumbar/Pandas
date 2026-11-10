import pandas as pd
data={
    "Category":["Cloths","Food","Accomodation","Travel","Cloths"],
    "Amount":[200,3000,90,5000,4000],
    "Date":["1-1-26","2-6-25","3-5-26","2-7-26","2-3-26"]
}
df=pd.DataFrame(data)
print(df)
print("Total:",df["Amount"].sum())
print("Total per category",df.groupby("Category")["Amount"].sum())
print(df[df["Amount"]>100])