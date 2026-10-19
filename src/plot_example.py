"""
Example plotting script for the Tata Visualization Certification Project.
Generates a sample plot and saves it to reports/sample_plot.png
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

def generate_sample_data(n=100):
    rng = np.random.default_rng(42)
    df = pd.DataFrame({
        "x": np.arange(n),
        "y": np.cumsum(rng.normal(loc=0.0, scale=1.0, size=n)),
        "category": rng.choice(["A", "B"], size=n)
    })
    return df


def plot_example(df, out_dir="reports"):
    os.makedirs(out_dir, exist_ok=True)
    plt.figure(figsize=(10,6))
    sns.lineplot(data=df, x="x", y="y", hue="category")
    plt.title("Sample Cumulative Random Walk by Category")
    out_path = os.path.join(out_dir, "sample_plot.png")
    plt.savefig(out_path, bbox_inches="tight", dpi=150)
    plt.close()
    return out_path


if __name__ == "__main__":
    df = generate_sample_data(200)
    out = plot_example(df)
    print(f"Saved sample plot to: {out}")
