import pandas as pd
import sys
import os

def process_csv(expense_data_path):
    directory, base_name = os.path.split(expense_data_path)
    file_date = base_name.split('.')[0]

    # Set the output file paths
    clean_output_path = os.path.join(directory, f'{file_date}-cleaned.csv')
    ytd_totals_output_path = os.path.join(directory, f'{file_date}-ytd-totals.csv')

    # Read the CSV file
    df = pd.read_csv(expense_data_path)

    # Remove unnecessary columns
    df.drop(['selected', 'No.', 'Payee', 'Action'], axis=1, inplace=True)

    # Filter out rows where Type is 'Credit Card Payment'
    df_filtered = df[df['Type'] != 'Credit Card Payment']

    # Remove the day from the dates
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%m/%Y')

    # Write the cleaned data to a new CSV file
    df_filtered.to_csv(clean_output_path, index=False)

    # Calculate YTD totals for each category
    ytd_totals = df_filtered.groupby('Category')['Total'].sum().reset_index()

    # Write YTD totals to another CSV file
    ytd_totals.to_csv(ytd_totals_output_path, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    expense_data_path = sys.argv[1]
    process_csv(expense_data_path)
