from operator import index
from sklearn.datasets import make_classification
import pandas as pd
def creat_data():
    features, output = make_classification(n_samples = 100000000,
                                       n_features = 5,
                                       n_informative = 5,
                                       n_redundant = 0,
                                       n_classes = 2,
                                       weights = [.2, .3])

    df1=pd.DataFrame(features,  columns=["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"])
    df2=pd.DataFrame(output,  columns=["class"])

    dataset=pd.merge(df1, df2, left_index=True, right_index=True)
    dataset.to_csv("SOME_VERY_LARGE_FILE.csv")
if __name__=="__main__":
    creat_data()
