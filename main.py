
# app/main.py
import joblib
from pathlib import Path
import pandas as pd
from fastapi import FastAPI, HTTPException
from schemas import StudentInputSchema
# 1. Get the directory where main.py actually lives
BASE_DIR = Path(__file__).resolve().parent

# 2. Build the absolute path to your joblib file relatively
# (Goes up one level from 'app', then into 'pipelines')
MODEL_PATH = BASE_DIR / "pipelines" / "logistic_regression.joblib"
MODEL_VERSION = "1.0.0"


app = FastAPI()

# Load your scikit-learn pipeline model
model_pipeline = joblib.load(MODEL_PATH)

# 2. Define human-readable labels to map numbers back to text
LABEL_MAP = {
    0: "Dropout",
    1: "Graduate",
    2: "Enrolled"
}


@app.get("/health")
def health():

    return {"status": "healthy", "model_version": MODEL_VERSION}


@app.post("/predict")
def predict_student_status(payload: StudentInputSchema):
    # Convert incoming payload to DataFrame using aliases
    input_dict = payload.model_dump(by_alias=True)
    input_df = pd.DataFrame([input_dict])

    # Intercept and clean known scikit-learn column naming discrepancies
    mapping = {
        "Marital status": "Marital Status",
        "Daytime/evening attendance\t": "Daytime/evening attendance"
    }
    input_df = input_df.rename(columns=mapping)

    try:
        # 3. Get the crisp prediction class
        prediction = model_pipeline.predict(input_df)
        prediction_code = int(prediction[0])
        prediction_label = LABEL_MAP.get(
            prediction_code, f"Unknown ({prediction_code})")

        # 4. Get the raw prediction probability arrays
        probabilities = model_pipeline.predict_proba(input_df)[0]

        # 5. Extract classes dynamically from the pipeline to build a confidence map
        # This pairs each label with its exact probability score percentage
        pipeline_classes = model_pipeline.classes_
        confidence_map = {}
        for index, class_code in enumerate(pipeline_classes):
            label_text = LABEL_MAP.get(int(class_code), f"Class_{class_code}")
            confidence_map[label_text] = round(
                float(probabilities[index]) * 100, 2)

        return {
            "prediction_code": prediction_code,
            "prediction": prediction_label,
            "confidence_percentages": confidence_map
        }

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Pipeline execution failure: {str(e)}")
