Energy Consumption Prediction
This project is a web-based application designed to predict energy consumption based on input data. It provides users with an easy-to-understand interface to input relevant data, view the prediction result, and initiate further predictions.

Features
Prediction Calculation: Predicts energy consumption in kilowatt-hours (kWh).
Responsive Design: The interface is designed to be user-friendly and responsive across different screen sizes.
Interactive Result Page: Displays the predicted energy consumption and allows the user to make new predictions.
Technologies Used
Frontend:
HTML5
CSS3
Backend:
Flask (for Python-based prediction model, SARIMAX Model)

1) Clone the repository:
  git clone https://github.com/swapnilsh2004/energy-consumption-prediction.git
2) Navigate to the project folder:
   cd energy-consumption-prediction
3) Run the application: If using Flask, run the following command to start the server:
   python app.py

How It Works
Input: The user inputs data (e.g., energy consumption factors, location, appliance usage).
Processing: The backend model processes the input data to predict energy consumption.
Output: The prediction result is displayed on the result page.
