from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("best_model_xgboost.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict-ui', methods=['POST'])
def predict_ui():
    try:
        features = np.array([
            float(request.form['price']),
            float(request.form['1h']),
            float(request.form['24h']),
            float(request.form['7d']),
            float(request.form['24h_volume']),
            float(request.form['market_cap']),
            float(request.form['price_change_ratio']),
            float(request.form['volume_to_price']),
            int(request.form['is_stable_coin'])
        ]).reshape(1, -1)

        prediction = model.predict(features)[0]
        prediction = round(prediction, 5)

        return render_template("index.html", prediction=prediction)
    except Exception as e:
        return render_template("index.html", prediction=f"Error: {str(e)}")
if __name__ == '__main__':
    app.run(debug=True)
