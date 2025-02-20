# Advanced Real Estate Prediction Tool
This project is a real estate price prediction tool built using Random Forest Regression and deployed as a web application using Streamlit. The model is trained on an extensive dataset with 287 features, processed with feature scaling, encoding, and outlier handling.

## Features

1. Machine Learning Model: Utilizes a fine-tuned Random Forest Regressor for accurate predictions.

2. Preprocessing Pipeline: Includes feature scaling, finding missing data, and outlier detection.

3. Web Application: Developed using Streamlit for an interactive and user-friendly interface.

4. User Inputs: Users can input house features via the web app to get instant price predictions.

5. Scalability: Designed for easy deployment and scalability.

## Installation

Clone the repository:  
git clone https://github.com/yourusername/real-estate-prediction.git
cd real-estate-prediction

Install dependencies:
pip install -r requirements.txt

Run the Streamlit app: streamlit run app.py

## Usage

1. Open the app in your browser and enter house features.
2. Click "Predict Price" to get the estimated price.

## File Structure

app.py: Streamlit web app for real-time predictions.

random_forest_model.pkl: Trained Random Forest model.

scaler.pkl: Preprocessing scaler for input data.

feature_columns.pkl: List of feature names for user input.

Advanced Real Estate Valuation with Ensemble Regression Models.ipynb: The source code for the project.

## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

## Author
Developed by Nilanjana Jamindar, Nithish Gowda KJ, Sanjana O R, Shama S K.
