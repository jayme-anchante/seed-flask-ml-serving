# core
import os
import glob
import pickle
import datetime
# external
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def save_to_disk(obj):
    timestamp = str(int(round(datetime.datetime.timestamp(datetime.datetime.now()) * 1e6)))
    filename = f"{timestamp}.model"
    algo_path = os.path.join(os.getenv("PROJECT_PATH"), "algorithms")
    if not os.path.exists(algo_path):
        os.mkdir(algo_path)
    filepath = os.path.join(algo_path, filename)
    with open(filepath, "wb") as file:
        pickle.dump(obj, file)
    print(f"Model saved to {filepath}")
    pass

def load_from_disk(filename):
    filepath = os.path.join(os.getenv("PROJECT_PATH"), "algorithms", filename)
    with open(filepath, "rb") as file:
        model = pickle.load(file)
    return model

def get_latest_model():
    path = os.path.join(os.getenv("PROJECT_PATH"), "algorithms")
    models = glob.glob(os.path.join(path, "*.model"))
    timestamps = []
    for model in models:
        timestamps.append(int(os.path.basename(model).split(".")[0]))
    filename = models[timestamps.index(max(timestamps))]
    return filename

def delete_all_except_latest():
    path = os.path.join(os.getenv("PROJECT_PATH"), "algorithms")
    models = os.listdir(path)
    latest_model = get_latest_model()
    for model in models:
        if model != latest_model:
            os.remove(os.path.join(path, model))
            print(f"Removed file {model}")
    pass
