from extract import create_db_engine, run_query, save_dataframe

import pandas as pd


def extract_rest_events(df):
    """
    Extract the first rest step immediately following a charge step and
    calculate ΔV and resistance.
    """

    # Work on a copy
    df = df.copy()

    df["voltage"] = pd.to_numeric(df["voltage"])
    df["current"] = pd.to_numeric(df["current"])

    # Previous row values (within each SampleID only)
    df["prev_step"] = df.groupby("SampleID")["step_type"].shift(1)
    df["prev_voltage"] = df.groupby("SampleID")["voltage"].shift(1)
    df["prev_current"] = df.groupby("SampleID")["current"].shift(1)
    #print(df.head(20))

    # First rest after a charge step
    rest_mask = (
        df["step_type"].str.lower().eq("rest")
        &
        df["prev_step"].str.lower().isin(["cc_chg", "cccv_chg"])
    )

    result = df.loc[
        rest_mask,
        [
            "SampleID",
            "dev_unit_chl",
            "test_id",
            "experiment_order",
            "voltage",
            "prev_voltage",
            "prev_current",
        ],
    ].copy()

    # Calculations
    result["delta_V"] = result["prev_voltage"] - result["voltage"]
    result["Resistance"] = result["delta_V"] / result["prev_current"]

    # Number cycles within each SampleID
    result["cycleID"] = (
        result.groupby("SampleID")
              .cumcount()
              .add(1)
    )

    # Final columns
    result = result[
        [
            "SampleID",
            "dev_unit_chl",
            "test_id",
            "experiment_order",
            "cycleID",
            "delta_V",
            "Resistance",
        ]
    ]

    return result

def main():
    engine = create_db_engine()

    try:
        df = run_query(engine)

        result = extract_rest_events(df)

        filepath = save_dataframe(result)
        print(f"\nData saved successfully to:\n{filepath}")

    finally:
        engine.dispose()
        print("\nDatabase connection closed.")


if __name__ == "__main__":
    main()