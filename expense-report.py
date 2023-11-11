import pandas as pd
import sys
import os

def process_csv(input_file_path, output_modified_path, output_ytd_totals_path):
    directory = os.path.dirname(input_file_path)

    # Set the output file paths
    output_modified_path = os.path.join(directory, 'modified_file.csv')
    output_ytd_totals_path = os.path.join(directory, 'ytd_totals_file.csv')

    # Read the CSV file, skipping the first row
    df = pd.read_csv(input_file_path, skiprows=1)

    # Remove unnecessary columns
    df.drop(['No.', 'Payee', 'Memo'], axis=1, inplace=True)

    # Remove the day from the dates
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%m/%Y')

    # Filter out rows where Type is 'Credit Card Payment'
    df_filtered = df[df['Type'] != 'Credit Card Payment']

    # Write the modified data to a new CSV file
    df_filtered.to_csv(output_modified_path, index=False)

    # Calculate YTD totals for each category
    ytd_totals = df_filtered.groupby('Category')['Total'].sum().reset_index()

    # Write YTD totals to another CSV file
    ytd_totals.to_csv(output_ytd_totals_path, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    process_csv(input_file_path)
