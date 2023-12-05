from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load your pre-trained model (replace 'your_model.pkl' with your actual model)
# Example:
import joblib
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')
    # return "Hello World!"

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get soil parameters from the form
            nitrogen = float(request.form['nitrogen'])
            phosphorus = float(request.form['phosphorus'])
            potassium = float(request.form['potassium'])
            ph = float(request.form['ph'])
            humidity = float(request.form['humidity'])
            temperature = float(request.form['temperature'])
            rainfall = float(request.form['rainfall'])
            
            # Use your model to predict the crop based on soil parameters
            # prediction = model.predict([[nitrogen, phosphorus, potassium, ph, humidity, temperature, rainfall]])
            # predicted_crop = perform_prediction(prediction)  # Perform necessary processing

            # Assuming 'data' contains your prediction values without feature names
            feature_names = ['Nitrogen', 'Phosphorus', 'Potassium', 'pH', 'Humidity', 'Temperature', 'Rainfall']

            # Create a DataFrame with feature names
            prediction_data = pd.DataFrame(data=[[nitrogen,phosphorus,potassium,ph,humidity,temperature,rainfall]], columns=feature_names)

            # Use this DataFrame for prediction
            prediction = model.predict(prediction_data)

            dict = {'Rice': 1, 'Wheat': 2, 'Maize': 3, 'Soybean': 4, 'Cotton': 5, 'Potato': 6, 'Tomato': 7, 'Onion': 8, 'Grapes': 9, 'Apple': 10, 'Banana': 11, 'Mango': 12, 'Citrus': 13, 'Coffee': 14, 'Tea': 15, 'Cocoa': 16, 'Sugarcane': 17, 'Sunflower': 18, 'Barley': 19, 'Oats': 20, 'Rye': 21, 'Sorghum': 22, 'Millet': 23, 'Chickpea': 24, 'Lentil': 25, 'Pea': 26}
            crop_dict = {value: key for key, value in dict.items()}
            # print(crop_dict[prediction[0]])

            
            predicted_crop = crop_dict[prediction[0]]  # Replace this with actual predicted crop
            
            return render_template('index.html', prediction=predicted_crop)
        except Exception as e:
            print(f"Error: {e}")
            return render_template('index.html', prediction="Error occurred. Please check input.")

if __name__ == '__main__':
    app.run(debug=True)
