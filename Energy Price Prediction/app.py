from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained SARIMAX model
with open('sarimax_energy_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    square_foot = float(request.form['square_foot'])
    occupancy = int(request.form['occupancy'])
    hvac_usage = 1 if request.form['hvac_usage'] == 'On' else 0
    lighting_usage = 1 if request.form['lighting_usage'] == 'On' else 0
    renewable_energy = float(request.form['renewable_energy'])
    # day_of_week = request.form['day_of_week']
    holiday = 1 if request.form['holiday'] == 'Yes' else 0

    # Prepare the input for the model
    data = pd.DataFrame({
        'Temperature': [temperature],
        'Humidity': [humidity],
        'SquareFoot': [square_foot],
        'Occupancy': [occupancy],
        'HVACUsage': [hvac_usage],
        'LightingUsage': [lighting_usage],
        'RenewableEnergy': [renewable_energy],
        # 'DayOfWeek_Saturday': [1 if day_of_week == 'Saturday' else 0],  # Example for one-hot encoding
        'Holiday': [holiday]
    })

    # Predict using the SARIMAX model
    prediction = model.forecast(steps=1, exog=data)[0]

    return render_template('result.html', prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)
