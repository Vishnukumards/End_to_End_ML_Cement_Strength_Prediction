
# 🏗️ Cement Compressive Strength Prediction

This is an end-to-end Machine Learning Operations (MLOps) project designed to predict the compressive strength of concrete based on its constituent components.  
The project includes a complete training pipeline, real-time prediction API, and batch prediction service — all accessible via a user-friendly Flask web interface.

---

## 🎯 Problem Statement

The goal is to build a robust machine learning model that accurately predicts the **compressive strength of concrete**.  
This prediction is based on 8 quantitative input variables representing the components of the mixture and its age.  
By doing so, construction companies can **optimize material usage, reduce costs,** and **ensure quality** without relying solely on physical testing.

---

## ✨ Features

**1. Real-Time Prediction (Single Input)**  
Users can input values for a single concrete mixture through a web form and get an instant prediction.

**2. Batch Prediction (CSV Upload)**  
Upload a CSV file containing multiple concrete mixtures. The app predicts strengths for all and returns a downloadable CSV file with an added prediction column.

---
## 📸 Screenshots

You can check out all screenshots of the project here:  
🔗 [Screenshots Folder on GitHub](https://github.com/Vishnukumards/End_to_End_ML_Cement_Strength_Prediction/Screenshots/Screenshot%2025-11-09%184218.pnghttps://github.com/Vishnukumards/End_to_End_ML_Cement_Strength_Prediction/Screenshots/Screenshot%2025-11-09%184218.png)

Example views:
- Web Interface (Real-Time & Batch Prediction)
- Prediction Output Table
- Model Training Logs

--

## 🎥 Project Overview Video

Watch the complete project walkthrough here:  
🎬 [Project Overview Video](https://github.com/Vishnukumards/End_to_End_ML_Cement_Strength_Prediction/blob/main/Demo_Project/Screen%20Recording%202025-11-09%20184420.mp4)

*(Replace `<your-video-link>` with your actual GitHub or YouTube video URL.)*

---

## 📂 Project Structure

```

PROJECT_CEMENT_STRENGTH/
├── artifacts/                 # Trained model (model.pkl) & preprocessor (preprocessor.pkl)
├── generated/                 # Output CSVs from batch predictions
├── logs/                      # Log files for debugging and monitoring
├── notebooks/                 # Jupyter notebooks for EDA
├── src/                       # Source code package
│   ├── **init**.py
│   ├── components/            # ML workflow components
│   │   ├── **init**.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/              # Training & prediction pipelines
│   │   ├── **init**.py
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── exception.py           # Custom exception handling
│   ├── logger.py              # Logging setup
│   └── utils.py               # Helper functions (save/load, etc.)
├── templates/                 # Flask HTML templates
│   └── index.html
├── uploads/                   # Temporary file uploads
├── venv/                      # Virtual environment
├── application.py             # Flask app entry point
├── predict.py                 # CLI batch prediction script
├── requirements.txt           # Dependencies
└── setup.py                   # Installable package setup

````

---

## ⚙️ Technology Stack

- **Backend**: Flask  
- **ML & Data Science**: Scikit-learn, Pandas, NumPy  
- **Environment & Tooling**: Python 3.8+, Virtualenv (`venv`), Git  

---

## 🚀 Setup & Installation

### Prerequisites
- Python 3.8 or higher  
- Git installed  

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd PROJECT_CEMENT_STRENGTH
````

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # for Windows
# OR
source venv/bin/activate # for Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Source Package

```bash
pip install -e .
```

---

## 🛠️ How to Run the Project

### **Phase 1: Train the Pipeline**

This runs the full ML workflow — data ingestion, transformation, model training, and artifact saving.

```bash
python src/pipeline/train_pipeline.py
```

### **Phase 2: Launch the Web App**

```bash
python application.py
```

Now open your browser at:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🧪 How to Use the Application

### **1. Real-Time Prediction**

* Go to `http://127.0.0.1:5000`
* Enter values for all 8 input fields under **“Real-Time Prediction”**
* Click **“Predict Single Value”**
* The predicted compressive strength will appear below the form.

### **2. Batch Prediction (CSV Upload)**

* Go to `http://127.0.0.1:5000`
* Under **“Batch Prediction”**, upload a CSV containing 8 input columns (no strength column)
* Click **“Predict on Dataset”**
* A preview of the first 5 predicted rows appears
* Click **“Download Full Predicted Dataset”** to get the complete CSV with predictions.

---

## 🧠 Model Details

* **Algorithm**: `RandomForestRegressor` (Scikit-learn)
* **Performance**: Achieves an **R² score ≈ 0.93** on test data, indicating high predictive accuracy.

---

## 📜 License

This project is for educational and demonstration purposes.
Feel free to adapt or extend it for your own MLOps learning and experimentation.

---

**Author:** Vishnu Kumar D S

**GitHub:** [Link](https://github.com/Vishnukumards)

```

