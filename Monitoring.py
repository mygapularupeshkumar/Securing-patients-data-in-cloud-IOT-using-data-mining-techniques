import pandas as pd
import time
def determine_risk_label(num):
    if num in [0, 1]:
        return "Low", "Very low Risk for Heart Disease. Safe"
    elif num in [2, 3]:
        return "Medium", "There is a Risk for Heart disease. Should be cautious"
    elif num == 4:
        return "High", "Should be Treated Immediately. Danger"

def IoT_Monitor():
    input_file_path = 'Cloud_Server/Patient_HealthCare_Data.csv'
    output_file_path = 'Cloud_Server/Labels.csv'
    data = pd.read_csv(input_file_path)
    data['RiskLabel'], data['Message'] = zip(*data['num'].apply(determine_risk_label))
    data.to_csv(output_file_path, index=False)
    updated_data = pd.read_csv(output_file_path)
    for index, row in updated_data.iterrows():
        if (row['RiskLabel'] == "High"):
            print(f"Patient ID: {index}")
            print(f"Label = {row['RiskLabel']}")
            print(f"Message = {row['Message']}")
            time.sleep(0.5)
            print("===================================")
            print("             Alert! High Risk For Heart Attack               ")
            print("===================================\n")
        else:
            print(f"Patient ID: {index}")
            print(f"Label = {row['RiskLabel']}")
            print(f"Message = {row['Message']}\n")
        time.sleep(1)
