# Foundations of Data Visualization and Analysis (FDVA)

This repository contains a structured series of experiments focusing on Data Exploration, Data Cleaning, and Data Visualization techniques. Each experiment is designed to be fully self-contained and demonstrates key concepts using Python, Power BI, and Tableau.

## 📂 Repository Structure

The project is organized into seven core experiments:

### 1. [Experiment 01: Setting up the Python environment and libraries](./Experiment_01_Setting_up_the_Python_environment_and_libraries)
- **Focus:** Introduction to the Jupyter Notebook environment and IPython widgets.
- **Key Concepts:** Interactive UI components (Sliders), dynamic outputs.

### 2. [Experiment 02: EDA - Data Import and Export](./Experiment_02_EDA-Data_Import_and_Export)
- **Focus:** Importing data from diverse sources and exporting cleaned datasets.
- **Key Concepts:** Reading CSVs, Excel files, and Web Scraping using `pandas`.

### 3. [Experiment 03: EDA - Data Cleaning](./Experiment_03_EDA-Data_Cleaning)
- **Focus:** Preprocessing data for analysis.
- **Key Concepts:** Handling missing values, imputation techniques (mode/median), dropping duplicates, formatting data types, and scaling (MinMaxScaler, StandardScaler).

### 4. [Experiment 04: EDA - Data Inspection and Analysis](./Experiment_04_EDA-Data_Inspection_and_Analysis)
- **Focus:** Understanding statistical properties of the dataset.
- **Key Concepts:** Extracting unique values, and computing mean, median, mode, variance, and standard deviation.

### 5. [Experiment 05: EDA - Data Visualization](./Experiment_05_EDA_DATA_VISUALIZATION)
- **Focus:** Creating static visualizations using `matplotlib`.
- **Key Concepts:** Line Charts, Bar Charts, and Histograms.

### 6. [Experiment 06: Data Visualization Using PowerBi](./Experiment_06_Data_Visualization_Using_PowerBi)
- **Focus:** Introduction to Business Intelligence reporting.
- **Key Concepts:** Connecting datasets to PowerBI, Power Query transformations, DAX calculations, and Dashboard design.

### 7. [Experiment 07: Data Visualization Using Tableau](./Experiment_07_Data_Visualization_Using_Tableau)
- **Focus:** Enterprise Data Visualization.
- **Key Concepts:** Tableau Desktop interface, calculated fields, dashboard interactions, and filtering.

## 🚀 Getting Started

To run the Python-based experiments (01 - 05) locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Mukilan-s18/FDVA.git
   cd FDVA
   ```

2. Create a virtual environment and install the required dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pandas numpy matplotlib seaborn scikit-learn ipywidgets openpyxl lxml html5lib jupyter
   ```

3. Navigate into any experiment folder and run the respective Python script or Jupyter Notebook.

---
*This repository was built using professional Conventional Commits to maintain a clean and descriptive project history.*
