"""Fit preprocessing and a model on training samples only."""
import json
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

x,y = load_iris(return_X_y=True)
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=.25,random_state=7,stratify=y)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=500))
model.fit(train_x,train_y)
print(json.dumps({"held_out_samples":len(test_y), "accuracy":model.score(test_x,test_y)}))
