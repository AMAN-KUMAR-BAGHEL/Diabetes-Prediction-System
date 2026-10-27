# Diabetes Prediction System

A machine learning web application that predicts whether a person is likely to be diabetic from eight basic health measurements. It uses a Support Vector Machine (SVM) classifier trained on the Pima Indians Diabetes dataset and is served through an interactive Streamlit interface.

> Part of the **Health Guard: Multiple Disease Prediction System** project by Aman Kumar Baghel. This README covers only the diabetes module.

## Dataset

- **Name:** Pima Indians Diabetes Database (National Institute of Diabetes and Digestive and Kidney Diseases)
- **Link:** <https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database>
- **Size:** 768 records, 8 input features, 1 target (`Outcome`)
- **Class balance:** 500 non-diabetic (0), 268 diabetic (1)

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure (mm Hg) |
| SkinThickness | Triceps skin-fold thickness (mm) |
| Insulin | 2-hour serum insulin (mu U/ml) |
| BMI | Body mass index |
| DiabetesPedigreeFunction | Diabetes pedigree (family history) score |
| Age | Age in years |
| Outcome | Target: 1 = diabetic, 0 = not diabetic |

## Project Description

The goal is to give users a quick, preliminary assessment of their diabetes risk so they can seek timely medical advice. The workflow is:

1. Load `diabetes.csv` with Pandas and explore it (shape, statistics, class counts).
2. Separate features (`x`) from the target (`Outcome`).
3. Split the data 80/20 into training and test sets (`stratify=y`, `random_state=2`).
4. Train an SVM classifier (`kernel='linear'`, `class_weight='balanced'`).
5. Evaluate with accuracy on both sets.
6. Save the trained model as `diabetes_model.sav` with `pickle`.
7. Load the model in a Streamlit app, collect inputs through sliders and show the result.

**Model performance**

| Dataset | Accuracy |
|---|---|
| Training | 77.85% |
| Test | 72.08% |

## Technologies Used

- **Language:** Python
- **Data processing:** NumPy, Pandas
- **Machine learning:** scikit-learn (Support Vector Machine)
- **Web interface:** Streamlit, streamlit-option-menu
- **Model persistence:** Pickle
- **Development environment:** Jupyter Notebook

## Project Structure

```
.
├── app.py                                           # Streamlit web application
├── Aman_Kumar_Baghel_Diabetes_Prediction_System.ipynb  # Model training notebook
├── Aman_Kumar_Baghel_ProjectReport.docx             # Project report
├── Datasets/
│   └── diabetes.csv                                 # Dataset
├── Models/
│   └── diabetes_model.sav                           # Trained SVM model
├── requirements.txt
└── README.md
```

## Setup and Run Instructions

**1. Clone or download the project and open a terminal in its folder.**

**2. (Recommended) Create and activate a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the web app**

```bash
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`. Open the **Diabetes Prediction** tab, set the sliders and click **Diabetes Test Result**.

> **Note:** `app.py` is the shared Health Guard app and also loads the heart disease, Parkinson's, lung cancer and thyroid models from `Models/`. To run only the diabetes module, keep just the diabetes model line (`Models/diabetes_model.sav`) and the Diabetes tab, and remove the other model loads and tabs.

**5. (Optional) Retrain the model**

Open `Aman_Kumar_Baghel_Diabetes_Prediction_System.ipynb` in Jupyter Notebook and run all cells. Make sure `Datasets/diabetes.csv` exists. The notebook saves a new `diabetes_model.sav`; move it into `Models/` to use it in the app.

## Key Information

- **Algorithm:** Linear-kernel SVM with balanced class weights to handle the 500/268 class imbalance.
- **Input order:** Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age. The model expects exactly this order.
- **Output:** "The person is diabetic" (1) or "The person is not diabetic" (0).
- **Version match:** The model was pickled with scikit-learn 1.5.1, so `requirements.txt` pins that version. Other versions may show an `InconsistentVersionWarning` or behave incorrectly.
- **Data quality:** The dataset uses `0` for missing values in Glucose, BloodPressure, SkinThickness, Insulin and BMI. No imputation is applied.
- **Known limitation:** The Glucose slider in the app currently ranges from 0 to 120, while the dataset goes up to 199. Raise the slider maximum in `app.py` to cover high-glucose cases.
- **Disclaimer:** This tool is for educational purposes only. It is not a medical diagnosis. Consult a qualified healthcare professional for any health concern.

## Future Scope

- Try ensemble and deep learning models for higher accuracy.
- Add feature scaling and missing-value handling.
- Add more health parameters and region-specific data.
- Integrate wearable and real-time health data.

## Author

**Aman Kumar Baghel**
