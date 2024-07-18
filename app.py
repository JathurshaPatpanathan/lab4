from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model and scaler
with open('fish_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('fish_scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Ensure all required features are present
        features = [
            float(data['Length1']),
            float(data['Length2']),
            float(data['Length3']),
            float(data['Height']),
            float(data['Width']),
            # Defaults to 0 if not provided
            float(data.get('Species_Parkki', 0)),
            float(data.get('Species_Perch', 0)),
            float(data.get('Species_Pike', 0)),
            float(data.get('Species_Roach', 0)),
            float(data.get('Species_Smelt', 0)),
            float(data.get('Species_Whitefish', 0))
        ]

        # Scale the features
        scaled_features = scaler.transform([features])

        # Make prediction
        prediction = model.predict(scaled_features)

        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
