import os
from features_processing import createfeatures

workshop_home = os.environ.get("workshop")

def get_preprocessed_data(home):
    data = createfeatures.main(home)
    return data

if __name__ == "__main__":
    data = get_preprocessed_data(workshop_home)
    