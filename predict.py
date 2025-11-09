# predict.py

import sys
import os
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.pipeline.predict_pipeline import PredictPipeline
import argparse

def main(input_path, output_path):
    """
    Main function to run the batch prediction pipeline.
    """
    logging.info(f"Starting batch prediction for input file: {input_path}")
    
    try:
        # Load the input dataset
        input_df = pd.read_csv(input_path)
        logging.info(f"Successfully loaded input data with shape: {input_df.shape}")

        # Ensure the 'Age (day)' column is of integer type if it exists
        if 'Age (day)' in input_df.columns:
            input_df['Age (day)'] = input_df['Age (day)'].astype(int)

        # Initialize the prediction pipeline
        predict_pipeline = PredictPipeline()
        
        # Get predictions
        logging.info("Making predictions on the input data...")
        predictions = predict_pipeline.predict(input_df)
        
        # Add the predictions as a new column to the dataframe
        input_df['Strength_Prediction'] = predictions
        logging.info("Predictions generated and added to the dataframe.")
        
        # Save the output file
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        input_df.to_csv(output_path, index=False)
        logging.info(f"Predictions saved to output file: {output_path}")

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    # Set up argument parser for command-line execution
    parser = argparse.ArgumentParser(description="Batch Prediction Pipeline for Cement Strength.")
    parser.add_argument('--input', type=str, required=True, help='Path to the input CSV file for prediction.')
    parser.add_argument('--output', type=str, required=True, help='Path to save the output CSV file with predictions.')
    
    args = parser.parse_args()
    
    # Run the main function
    main(args.input, args.output)