import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
def PCA_Algorithm():
    df = pd.read_csv("Output/preprocessed.csv")
    df_numeric = df.select_dtypes(include=['number'])
    X = df_numeric.drop(columns=['num'])
    y = df_numeric['num']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca = PCA(n_components=2)  
    X_pca = pca.fit_transform(X_scaled)
    df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])  
    df_final = pd.concat([df, df_pca], axis=1)
    df_final.to_csv("Output/extracted.csv", index=False)
    print(df_final.head(10))
