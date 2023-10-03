import pandas as pd

def read_csv(file):
  '''Load csv file'''
  try:
    df = pd.read_csv(file)
    return df
  except FileNotFoundError as e:
    print(e)
    
def data_pipeline(df):
  '''Transform pandas DataFrame'''
  # Transformations
  df['dob'] = pd.to_datetime(df['dob'])
  df['dateRegistration'] = pd.to_datetime(df['dateRegistration'])
  
  # Adding column AgeWhenRegistered --> dateRegistration.year()
  df['AgeWhenRegistered'] = (df['dateRegistration'].dt.year) - (df['dob'].dt.year)
  
  # Filter DataFrame selecting people who registered after being 18
  df_transformed = df[df['AgeWhenRegistered'] >= 18]
  
  return df_transformed

def load_results(df_transformed):
  df_transformed.to_csv("../data/output_data.csv")

if __name__ == "__main__":
  input_file = "../data/input_data.csv"
  df = read_csv(input_file)
  df_transformed = data_pipeline(df)
  load_results(df_transformed) 