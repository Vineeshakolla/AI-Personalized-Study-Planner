import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("dataset/student_dataset.csv")

# Create encoders
goal_encoder = LabelEncoder()
skill_encoder = LabelEncoder()
focus_encoder = LabelEncoder()

# Convert text columns into numbers
df["goal"] = goal_encoder.fit_transform(df["goal"])
df["skill_level"] = skill_encoder.fit_transform(df["skill_level"])
df["focus"] = focus_encoder.fit_transform(df["focus"])

# Features and Target
X = df[["year", "goal", "hours", "skill_level"]]
y = df["focus"]

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

print("Model Trained Successfully!")

# Save model
joblib.dump(model, "model/study_planner.pkl")

# Save encoders
joblib.dump(goal_encoder, "model/goal_encoder.pkl")
joblib.dump(skill_encoder, "model/skill_encoder.pkl")
joblib.dump(focus_encoder, "model/focus_encoder.pkl")

print("Model Saved Successfully!")