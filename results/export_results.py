"""
Export optimizer results to CSV.
"""

import pandas as pd
import os


def export_results(results):

    os.makedirs("results", exist_ok=True)

    df = pd.DataFrame(results)

    filename = "results/optimization_results.csv"

    df.to_csv(

        filename,

        index=False

    )

    print("\n" + "=" * 60)
    print("RESULTS SAVED")
    print("=" * 60)
    print(f"Saved to : {filename}")