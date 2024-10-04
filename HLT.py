import pandas as pd
import numpy as np
def HLT_Algorithm():
    def laplacian_encrypt(data):
        return data + np.random.laplace(loc=0, scale=1, size=len(data))

    def laplacian_decrypt(data, noise_scale=1):
        return data - noise_scale

    dataset = pd.read_csv("Output/extracted.csv")
    datast = pd.read_csv("Output/extracted.csv")
    columns_to_encrypt = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'num', 'PC1', 'PC2']
    for column in columns_to_encrypt:
        dataset[column] = laplacian_encrypt(dataset[column])

    print("\n===============\nEncrypted Data:\n===============\n")
    print(dataset)
    dataset.to_csv("Output/encrypted_dataset.csv", index=False)
    for column in columns_to_encrypt:
        dataset[column] = laplacian_decrypt(dataset[column], noise_scale=1)

    print("\n===============\nDecrypted Data:\n===============\n")
    print(datast)
    datast.to_csv("Output/decrypted_dataset.csv", index=False)
