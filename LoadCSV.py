import os
from pathlib import Path
import shutil
import pandas as pd
from tkinter import filedialog
import warnings
warnings.filterwarnings("ignore")

def load_data():
    print("\nSelect Dataset CSV File:")
    file_path = filedialog.askopenfilename(title="Select Dataset", filetypes=[("CSV Files", "*.csv")])
    if not file_path.endswith('.csv'):
        print("\nUnsupported file format. Only CSV files are supported.\n")
        print("\nPlease Try again....!!!!!\n")
        return
    
    file_name = Path(file_path).name
    print(f"\nDataset CSV File Location: {file_path}")
    print("\n")
    print("Sample Data of Loaded Dataset:")
    df = pd.read_csv(file_path)
    print(df.head(10))
    input_dir = "Input"
    output_dir = "Output"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(input_dir, exist_ok=True)
    media_file = os.path.join(input_dir, "Input.csv")
    shutil.copy(file_path, media_file)
