import os

import pandas as pd
from sqlalchemy import create_engine

from config import DB_CONFIG

from sql_queries import QUERIES

from cell_IDs import CellIDs

def create_db_engine():
    """Create a SQLAlchemy engine."""

    connection_string = (
        f"mysql+pymysql://{DB_CONFIG['user']}:"
        f"{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:"
        f"{DB_CONFIG['port']}/"
        f"{DB_CONFIG['database']}"
    )

    return create_engine(connection_string)

def get_sample_ids():
    """Allow the user to enter a SampleID or select a predefined list."""

    print("\nSampleID Options")
    print("1. Enter a single SampleID")
    print("2. Choose a predefined list")

    option = input("\nSelect option: ").strip()

    if option == "1":
        return [input("Enter SampleID: ").strip()]

    elif option == "2":

        print("\nAvailable Sample Lists:\n")

        list_names = list(CellIDs.keys())
        
        for i, name in enumerate(list_names, start=1):
            print(f"{i}. {name}")

        choice = int(input("\nSelect list number: "))

        selected = CellIDs[list_names[choice - 1]]

        print("\nSelected SampleIDs:")
        for sample in selected:
            print(f"  {sample}")

        return selected

    else:
        print("Invalid choice.")
        return get_sample_ids()

def run_query(engine):
    
    print("\nAvailable queries:\n")

    query_names = list(QUERIES.keys())

    for i, name in enumerate(query_names, start=1):
        print(f"{i}. {name}")

    choice = int(input("\nSelect query number: "))

    query_function = QUERIES[query_names[choice - 1]]

    query = query_function()
    sample_ids = get_sample_ids()

    placeholders = ",".join(["%s"] * len(sample_ids))
    
    query = query.format(placeholders=placeholders)

    df = pd.read_sql(
        query,
        engine,
        params=tuple(sample_ids)
    )
    
    print(f"\nRetrieved {len(df)} rows")

    return df

def save_dataframe(df):
    """Save the DataFrame to a CSV file."""

    os.makedirs("output", exist_ok=True)

    while True:
        filename = input(
            "\nEnter the name for the output CSV file (without .csv): "
        ).strip()

        if filename:
            break

        print("Filename cannot be empty. Please try again.")

    if not filename.lower().endswith(".csv"):
        filename += ".csv"

    filepath = os.path.join("output", filename)

    df.to_csv(filepath, index=False)

    return filepath


def main():

    engine = create_db_engine()

    try:

        df = run_query(engine)

        if df is not None:

            save_choice = input(
                "\nDo you want to save the data as a CSV? (y/n): "
            ).strip().lower()

            if save_choice == "y":
                filepath = save_dataframe(df)
                print(f"\nData saved successfully to:\n{filepath}")

            else:
                print("\nData was not saved.")

    finally:

        engine.dispose()
        print("\nDatabase connection closed.")


if __name__ == "__main__":
    main()