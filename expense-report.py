import pandas as pd

def process_csv(input_file_path, output_modified_path, output_ytd_totals_path):
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

# Example usage
input_file_path = 'path_to_your_input_file.csv'  # Replace with your input file path
output_modified_path = 'path_to_your_modified_file.csv'  # Desired path for the modified file
output_ytd_totals_path = 'path_to_your_ytd_totals_file.csv'  # Desired path for the YTD totals file

process_csv(input_file_path, output_modified_path, output_ytd_totals_path)
