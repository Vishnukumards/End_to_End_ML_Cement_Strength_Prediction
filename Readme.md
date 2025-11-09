# Cement Compressive Strength Prediction

This is an end-to-end Machine Learning Operations (MLOps) project designed to predict the compressive strength of concrete based on its constituent components. The project is built with a modular structure, featuring a complete training pipeline, a real-time prediction API, and a batch prediction service, all accessible through a user-friendly web interface built with Flask.

## 🎯 Problem Statement

The goal of this project is to build a robust machine learning model that accurately predicts the compressive strength of concrete. This prediction is based on 8 quantitative input variables representing the components of the concrete mixture and its age. By predicting the strength, construction companies can optimize material usage, reduce costs, and ensure the quality and durability of concrete structures without relying solely on time-consuming physical tests.

---

## ✨ Features

This application provides two primary modes of prediction:

1.  **Real-Time Prediction (Single Input)**: A web form allows users to input the values for each component of a single concrete mixture and receive an instant strength prediction.

2.  **Batch Prediction (CSV Upload)**: Users can upload a CSV file containing multiple rows of cement mixture data. The application processes the entire file and provides a downloadable CSV with an added column for the predicted strength of each mixture.

---

## 📂 Project Structure

The project is organized using a professional MLOps structure to ensure scalability and maintainability:
PROJECT_CEMENT_STRENGTH/
├── artifacts/ # Stores the trained model (model.pkl) and preprocessor (preprocessor.pkl)
├── generated/ # Stores the output CSVs from batch predictions
├── logs/ # Stores log files for monitoring and debugging
├── notebooks/ # Contains Jupyter notebooks for exploratory data analysis
├── src/ # The main source code package
│ ├── init.py
│ ├── components/ # Modules for different ML stages
│ │ ├── init.py
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ ├── pipeline/ # Orchestration scripts for training and prediction
│ │ ├── init.py
│ │ ├── predict_pipeline.py
│ │ └── train_pipeline.py
│ ├── exception.py # Custom exception handling
│ ├── logger.py # Logging configuration
│ └── utils.py # Utility functions (e.g., for saving/loading objects)
├── templates/ # HTML templates for the Flask web application
│ └── index.html
├── uploads/ # Temporarily stores uploaded files
├── venv/ # Virtual environment files
├── application.py # The main Flask application entry point
├── predict.py # Script for command-line batch prediction
├── requirements.txt # Project dependencies
└── setup.py # Makes the src directory an installable package

---

## ⚙️ Technology Stack

-   **Backend**: Flask
-   **Machine Learning & Data Science**: Scikit-learn, Pandas, NumPy
-   **Environment & Tooling**: Python 3.8+, Virtual Environment (`venv`), Git

---

## 🚀 Setup and Installation

Follow these steps to set up and run the project on your local machine.

**Prerequisites**:
-   Python 3.8 or higher
-   Git for version control

**1. Clone the Repository**
```bash
git clone <your-repository-url>
cd PROJECT_CEMENT_STRENGTH

**2. Create and Activate a Virtual Environment**
python -m venv venv
venv\Scripts\activate

**3. Install Dependencies**
pip install -r requirements.txt

**4. Install the Source Package**
pip install -e .

🛠️ How to Run the Project
The project is divided into two main phases: training the pipeline and launching the web application.
Phase 1: Training the Pipeline
This script will run the complete machine learning pipeline: ingest the data, perform transformations, train the RandomForestRegressor model, and save the necessary model and preprocessor files (.pkl) into the artifacts folder.
python src/pipeline/train_pipeline.py

Phase 2: Launching the Web Application
python application.py

Once the server is running, open your web browser and navigate to:
http://127.0.0.1:5000


🧪 How to Use the Application
Once the web application is running, you can use its two main features:
For Real-Time Prediction (Single Input):
Navigate to http://127.0.0.1:5000.
Use the form on the left side of the page, titled "Real-Time Prediction".
Fill in the values for all 8 input fields.
Click the "Predict Single Value" button.
The predicted compressive strength will appear below the form.
For Batch Prediction (CSV Upload):
Navigate to http://127.0.0.1:5000.
Use the form on the right side of the page, titled "Batch Prediction".
Prepare a CSV file that contains the 8 input columns but does not contain the final strength column.
Click "Choose File", select your CSV, and click the "Predict on Dataset" button.
The page will reload, showing a preview of the first 5 rows of your data with a new Strength_Prediction column.
Click the "Download Full Predicted Dataset" button to download a new CSV file containing all your original data plus the predictions.

🧠 Model Details

Model: RandomForestRegressor from Scikit-learn.
Performance: The model achieves an R-squared (R²) score of approximately 0.93 on the test set, indicating high predictive accuracy.
