import os
import lightgbm as lgb 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from features_processing import createfeatures

workshop_home = os.environ.get("workshop")

# default parameters
parameters = {
    "Data_defaults": {
        "objective": "regression",
        "num_iterations": 300,
        "learning_rate": 0.1,
        "num_leaves": 31,
        "num_threads": 0,
        "deterministic": "true",
        "max_depth": -1,
        "min_data_in_leaf": 20,
        "bagging_fraction": 0.7,
        "feature_fraction_bynode": 1,
        "feature_fraction_seed": 2,
        "early_stopping_round": 0,
        "min_data_per_group": 100,
        "max_cat_threshold": 100000,
        "verbosity": -1,
        "max_bin": 10000,
    },
    "Training_defaults": {
        "objective": "regression",
        "num_iterations": 100,
        "num_leaves": 31,
        "num_threads": 0,
        "deterministic": "true",
        "max_depth": -1,
        "min_data_in_leaf": 20,
        "bagging_fraction": 0.7,
        "feature_fraction_bynode": 1,
        "feature_fraction_seed": 2,
        "early_stopping_round": 0,
        "min_data_per_group": 100,
        "max_cat_threshold": 100000,
        "verbosity": -1,
        "max_bin": 10000,
    },
}

def get_preprocessed_data(home):
    data = createfeatures.main(home)
    return data

def retrieve_X_y(data): 
    y = data.quantity.values 
    del data["quantity"]
    price = data["unitprice"]
    data = data.apply(LabelEncoder().fit_transform)
    data["unitprice"] = price
    X = data.values 
    cat_pos = [0,2,3,4,5,6]
    return X,y, cat_pos


def split_data(X,y):
    X, TX, y, Ty = train_test_split(X, y, test_size=0.1, random_state=42)  
    # lgb needs y as an array.
    y = y.reshape((-1))
    Ty = Ty.reshape((-1))
    return X, TX, y, Ty 
    


def xlgbm(X,TX,y,Ty,cat_inds): 
    
    data_params = parameters["Data_defaults"]
    tr_params = parameters["Training_defaults"]
    data_params["categorical_feature"] = cat_inds

    # Train the model
    lgb_train = lgb.Dataset(X, y, params=data_params)
    lgb_eval = lgb.Dataset(TX, Ty, reference=lgb_train, params=data_params)
    gbm = lgb.train(tr_params, lgb_train, valid_sets=lgb_eval)

    y_hat = gbm.predict(X, pred_leaf=False)
    Ty_hat = gbm.predict(TX, pred_leaf=False)
    # Grabr results 
    y_hat = np.reshape(y_hat, (y_hat.shape[0], 1))
    y = np.reshape(y, (y.shape[0], 1))
    Ty_hat = np.reshape(Ty_hat, (Ty_hat.shape[0], 1))
    Ty = np.reshape(Ty, (Ty.shape[0], 1))
    # Step - Outlier detection if applicable
    
    y_out = {"y": y, "y_pred": y_hat}
    Ty_out = {"y": Ty, "y_pred": Ty_hat}
    
    return y_out, Ty_out

if __name__ == "__main__":
    data = get_preprocessed_data(workshop_home)
    features, target , cat_pos = retrieve_X_y(data)
    X, TX, y, Ty = split_data(features, target)
    out, Tout = xlgbm(X,TX,y,Ty,cat_pos)
    