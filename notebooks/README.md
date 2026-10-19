This directory is for example notebooks and exploratory analysis.

You can create Jupyter notebooks here. To reproduce the example plot included in `src/plot_example.py`:

1. Create/activate your virtual environment and install requirements:

   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   pip install -r requirements.txt

2. Run the example script to generate a sample plot (it will create `reports/sample_plot.png`):

   python src/plot_example.py

3. Open a new notebook and either:
   - Use the generated PNG (reports/sample_plot.png), or
   - Import the functions from `src/plot_example.py` and generate plots inline.

Suggested notebook filename: `notebooks/example_visualization.ipynb` (create using Jupyter Lab or Notebook)
