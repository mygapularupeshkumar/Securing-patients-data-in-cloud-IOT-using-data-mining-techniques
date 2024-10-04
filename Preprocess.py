import pandas as pd
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTEENN
def balance_data(X, y, target_size):
    smote_enn = SMOTEENN(smote=SMOTE(sampling_strategy='auto', random_state=42),
                         enn=None)
    X_resampled, y_resampled = smote_enn.fit_resample(X, y)
    df_resampled = pd.concat([pd.DataFrame(X_resampled, columns=X.columns), pd.DataFrame(y_resampled, columns=['num'])], axis=1)
    df_resampled = df_resampled.sample(n=target_size, random_state=42)
    return df_resampled

def SMOTE_Algorithm():
    df = pd.read_csv("Input/Input.csv")
    print("Original Dataset:")
    print(df.head(10))
    print("\n")
    df_numeric = df.select_dtypes(include=['number'])
    X = df_numeric.drop(columns=['num'])
    y = df_numeric['num']
    target_size = len(df) 
    df_resampled = balance_data(X, y, target_size)
    df_resampled.to_csv("Output/preprocessed.csv", index=False)
    print("Preprocessed Dataset:")
    print(df_resampled.head(10))
