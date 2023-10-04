# Automated CI pipeline with GitHub Actions

This repository contains a data processing pipeline written in Python for working with CSV data. The pipeline includes code for reading a CSV file, transforming the data using Pandas, and loading the transformed data into a new CSV file.

## Production Pipeline

The production pipeline consists of the following components:

### `read_csv(file)`

This function loads a CSV file specified by the `file` parameter into a Pandas DataFrame. It handles the case where the file is not found and prints an error message in that case.

### `data_pipeline(df)`

The `data_pipeline` function performs various transformations on the input Pandas DataFrame `df`. These transformations include converting date columns to datetime objects, calculating the age of individuals when they registered, and filtering the DataFrame to include only records where the age at registration is 18 or older.

### `load_results(df_transformed)`

This function takes the transformed DataFrame `df_transformed` and saves it as a new CSV file named "output_data.csv" in the "../data/" directory.

## Continuous Integration (CI)

A GitHub Actions workflow named "CI" has been set up to automate the testing of this code. The workflow runs the following steps:

1. Checks out the code from the repository.
2. Sets up Python with the specified version.
3. Installs the necessary dependencies listed in "requirements.txt".
4. Runs pytest to execute the unit tests.

## Unit Tests

The unit tests for this pipeline are located in the "test" directory. The main test file is "test_data_pipeline.py", and it contains the following test case:

### `test_data_pipeline()`

This test case calls the `data_pipeline` function with a sample dataset and asserts that the expected behavior is met. Specifically, it checks whether individuals who registered before the age of 18 are correctly excluded from the transformed DataFrame.

## Usage

To use this data processing pipeline, follow these steps:

1. Ensure you have Python installed, preferably version 3.10.7.
2. Clone this repository to your local machine.
3. Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt

