import pandas as pd
import sys
sys.path.append("src")
from data_pipeline import data_pipeline

def test_data_pipeline():
  '''call the data_pipeline and test it'''
  
  # Emily and Michael registered before 18, should not be in the transformed_df
  data = {
      'firstName': ['John', 'Jane', 'Bob', 'Emily', 'Michael'],
      'lastName': ['Doe', 'Smith', 'Johnson', 'Clark', 'Williams'],
      'dob': ['1980-05-15', '1995-12-10', '1973-09-25', '1988-07-03', '2000-02-18'],
      'dateRegistration': ['2022-03-01', '2022-02-20', '2022-01-15', '2000-03-10', '2017-02-05'],
      'age': [42, 26, 48, 33, 22],
      'gender': ['Male', 'Female', 'Male', 'Female', 'Male']
  }

  df = pd.DataFrame(data)

  transformed_df = data_pipeline(df)

  # Assertions to check the expected behavior
  assert "Emily" not in transformed_df["firstName"].values
  assert "Michael" not in transformed_df["firstName"].values
