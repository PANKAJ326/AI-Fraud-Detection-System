🛡️ AI Fraud Detection System

An end-to-end, industry-aligned machine learning solution designed to detect fraudulent credit card transactions. This application features a real-time web interface built with Streamlit, an automated Random Forest classification pipeline, and secure SQLite database tracking for prediction history.

---

✨ Features

- Machine Learning based fraud prediction
- Real-time transaction analysis
- CSV file transaction upload
- Fraud and normal transaction classification
- Interactive analytics dashboard
- Data visualization using charts
- Prediction history storage
- User login system
- Download prediction results

---

🛠️ Tech Stack

- Python
- Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Streamlit
- Plotly
- SQLite

---

📂 Project Structure

```text
├── app.py                      # Main application entry point & layout
├── database.py                 # SQLite database schema and helper functions
├── requirements.txt            # Python dependencies
├── dataset/
│   └── creditcard_sample.csv   # Transaction training dataset
├── models/
│   └── fraud_model.pkl         # Serialized Random Forest model artifact
├── modules/
│   ├── assets/
│   │   └── logo.png            # Dashboard sidebar logo
│   ├── home.py                 # Home page content
│   ├── fraud_detection.py      # Batch data upload and ML prediction logic
│   ├── analytics.py            # Metrics and visualization panels
│   ├── history.py              # Past batch lookup interface
│   ├── login.py                # User login screen interface
│   └── about.py                # Project metadata and specifications
└── train_model.py              # Model training, evaluation, and serialization script
```

📊 Database Schema

The prediction history uses an automated SQLite backend configured as follows:

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `id` | `INTEGER` | Primary key auto-increment |
| `total_transactions` | `INTEGER` | Total rows processed per upload |
| `normal_transactions`| `INTEGER` | Total flag-free transactions |
| `fraud_transactions` | `INTEGER` | Total identified fraudulent flags |
| `fraud_percentage`   | `REAL` | Proportion of malicious inputs |
| `prediction_time`    | `TIMESTAMP`| Automatic current generation timestamp |

---

📝 Author
Pankaj Soni

