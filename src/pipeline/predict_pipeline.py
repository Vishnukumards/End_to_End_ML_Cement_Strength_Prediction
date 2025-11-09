import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 cement: float,
                 blast_furnace_slag: float,
                 fly_ash: float,
                 water: float,
                 superplasticizer: float,
                 coarse_aggregate: float,
                 fine_aggregate: float,
                 age: int):
        
        self.cement = cement
        self.blast_furnace_slag = blast_furnace_slag
        self.fly_ash = fly_ash
        self.water = water
        self.superplasticizer = superplasticizer
        self.coarse_aggregate = coarse_aggregate
        self.fine_aggregate = fine_aggregate
        self.age = age

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Cement (component 1)(kg in a m^3 mixture)": [self.cement],
                "Blast Furnace Slag (component 2)(kg in a m^3 mixture)": [self.blast_furnace_slag],
                "Fly Ash (component 3)(kg in a m^3 mixture)": [self.fly_ash],
                "Water  (component 4)(kg in a m^3 mixture)": [self.water],
                "Superplasticizer (component 5)(kg in a m^3 mixture)": [self.superplasticizer],
                "Coarse Aggregate  (component 6)(kg in a m^3 mixture)": [self.coarse_aggregate],
                "Fine Aggregate (component 7)(kg in a m^3 mixture)": [self.fine_aggregate],
                "Age (day)": [self.age]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)