# 🚀 Crypto Liquidity Predictor

This project is a machine learning web application that predicts the **liquidity of cryptocurrencies** using historical market data.

It is built using:
- Python 🐍
- Flask 🔥
- XGBoost 📈
- Render 🌐 (for deployment)

---

## 📊 Features Used for Prediction

- `price`
- `1h`, `24h`, `7d` (% changes)
- `24h_volume`, `market_cap`
- `price_change_ratio`, `volume_to_price`
- `is_stable_coin` (binary)

---

## 🧠 Model Used

- **XGBoost Regressor**
- Hyperparameter tuned with GridSearchCV
- Best model saved using `joblib`

---

## 🖥️ Run Locally

1. Clone this repo or download ZIP
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run Flask app:
```bash
python app.py
```
4. Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌍 Deployment on Render

This app is auto-deployable on [Render](https://render.com).  
Make sure your repo contains:
- `app.py`
- `render.yaml`
- `requirements.txt`
- `templates/index.html`
- `best_model_xgboost.pkl`

---

## 📂 File Structure

```
crypto-liquidity-app/
├── app.py
├── requirements.txt
├── render.yaml
├── best_model_xgboost.pkl
├── templates/
│   └── index.html
└── README.md
```

---

## 👤 Author
**Adeel**  
_Data Science Enthusiast | Crypto Explorer | Flask Developer_

