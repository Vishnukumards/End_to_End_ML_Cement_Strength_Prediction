import os
from flask import Flask, request, render_template, send_from_directory
import pandas as pd
from werkzeug.utils import secure_filename
import uuid # For creating unique filenames

from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.exception import CustomException
from src.logger import logging

# Define upload and generated file folders
UPLOAD_FOLDER = 'uploads'
GENERATED_FOLDER = 'generated'

application = Flask(__name__)
app = application
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['GENERATED_FOLDER'] = GENERATED_FOLDER

# Ensure the upload and generated directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GENERATED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    """Handles single, real-time prediction from the form."""
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # Same single prediction logic as before
        data = CustomData(
            cement=float(request.form.get('cement')),
            blast_furnace_slag=float(request.form.get('blast_furnace_slag')),
            fly_ash=float(request.form.get('fly_ash')),
            water=float(request.form.get('water')),
            superplasticizer=float(request.form.get('superplasticizer')),
            coarse_aggregate=float(request.form.get('coarse_aggregate')),
            fine_aggregate=float(request.form.get('fine_aggregate')),
            age=int(request.form.get('age'))
        )
        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('index.html', results=f"{results[0]:.2f}")

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    """Handles batch prediction from an uploaded CSV file."""
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('index.html', error='No selected file')
    
    if file and file.filename.endswith('.csv'):
        try:
            # Create a unique filename to avoid conflicts
            unique_id = uuid.uuid4().hex
            original_filename = secure_filename(file.filename)
            input_filename = f"{unique_id}_{original_filename}"
            input_filepath = os.path.join(app.config['UPLOAD_FOLDER'], input_filename)
            file.save(input_filepath)

            logging.info(f"File uploaded successfully to {input_filepath}")
            
            # --- Batch Prediction Logic ---
            # 1. Load the uploaded data
            input_df = pd.read_csv(input_filepath)
            
            # 2. Run the prediction pipeline
            predict_pipeline = PredictPipeline()
            predictions = predict_pipeline.predict(input_df)
            
            # 3. Add predictions to the dataframe
            input_df['Strength_Prediction'] = predictions
            
            # 4. Generate the output file
            output_filename = f"predicted_{input_filename}"
            output_filepath = os.path.join(app.config['GENERATED_FOLDER'], output_filename)
            input_df.to_csv(output_filepath, index=False)
            
            logging.info(f"Batch prediction complete. Output saved to {output_filepath}")
            
            # 5. Prepare data to render on the page
            # Get the first 5 rows to display as a preview
            table_html = input_df.head().to_html(classes='table table-striped', index=False)
            
            return render_template('index.html', 
                                   table=table_html, 
                                   filename=output_filename,
                                   batch_success='Batch prediction complete!')

        except Exception as e:
            raise CustomException(e, sys)
    
    else:
        return render_template('index.html', error='Invalid file type. Please upload a CSV file.')

@app.route('/download/<filename>')
def download_file(filename):
    """Provides the download functionality for the predicted file."""
    return send_from_directory(app.config['GENERATED_FOLDER'], filename, as_attachment=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    
# from flask import Flask, request, render_template
# import numpy as np
# import pandas as pd
# from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# application = Flask(__name__)
# app = application

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predictdata', methods=['GET', 'POST'])
# def predict_datapoint():
#     if request.method == 'GET':
#         return render_template('index.html')
#     else:
#         data = CustomData(
#             cement=float(request.form.get('cement')),
#             blast_furnace_slag=float(request.form.get('blast_furnace_slag')),
#             fly_ash=float(request.form.get('fly_ash')),
#             water=float(request.form.get('water')),
#             superplasticizer=float(request.form.get('superplasticizer')),
#             coarse_aggregate=float(request.form.get('coarse_aggregate')),
#             fine_aggregate=float(request.form.get('fine_aggregate')),
#             age=int(request.form.get('age'))
#         )
#         pred_df = data.get_data_as_data_frame()
#         print(pred_df)

#         predict_pipeline = PredictPipeline()
#         results = predict_pipeline.predict(pred_df)
#         return render_template('index.html', results=f"{results[0]:.2f}")

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)
#     #app.run(host="0.0.0.0", debug=True)