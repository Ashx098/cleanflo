import pandas as pd
from cleanflo_pipeline import clean_numeric_data, clean_categorical_data, clean_text_data, clean_datetime_data

# Sample Test DataFrame

data = {
    "Age": [25, 30, 22, 40, 29, None, 45, 50, None, 27],
    "Salary": [50000, 60000, 70000, 80000, None, 75000, 90000, None, 72000, 58000],
    "Department": ["HR", "Finance", "IT", "IT", "Finance", "IT", "Sales", "HR", "IT", "Marketing"],
    "Review": ["Great product! 😊", "Worst experience!!!", "Would buy again.", "Just okay.", None, "Fantastic experience.", "Not good 😡", "Nice deal.", "Loved it!", "Superb."],
    "Joining_Date": ["2023-01-15", "15-02-2022", "March 3, 2021", "2020/07/19", "18-Aug-2019", "2017-11-25", "2016-06-30", "2021-09-10", "2019-04-05", "2018-12-20"]
}

df = pd.DataFrame(data)
print("\n🔹 Original DataFrame:")
print(df)

# ✅ Test Numeric Cleaning
df_numeric = clean_numeric_data(df)
print("\n✅ Numeric Data Cleaning:")
print(df_numeric)

# ✅ Test Categorical Encoding
df_categorical = clean_categorical_data(df)
print("\n✅ Categorical Data Encoding:")
print(df_categorical)

# ✅ Test Text Cleaning
df_text = clean_text_data(df)
print("\n✅ Text Cleaning:")
print(df_text)

# ✅ Test Datetime Processing
df_datetime = clean_datetime_data(df)
print("\n✅ Datetime Processing:")
print(df_datetime)
