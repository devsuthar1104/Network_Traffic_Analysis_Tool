from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(data):
    feature_vectors = [list(packet.values()) for packet in data]
    model = IsolationForest(contamination=0.1)
    preds = model.fit_predict(feature_vectors)
    anomalies = [data[i] for i, pred in enumerate(preds) if pred == -1]
    return anomalies
