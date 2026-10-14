# Credit Card Fraud Detection

## Project Overview
This project uses a Random Forest classifier to estimate the probability that a credit card transaction is fraudulent. A Streamlit web application allows users to enter transaction features and view the model's prediction.

## Technologies
- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn

## Model Information
- **Algorithm:** Random Forest Classifier
- **Input features:** 30
- **Fraud decision threshold:** 0.20 (20%)

## Recorded Test Results
The model's recorded evaluation at the 0.20 threshold:

| Metric | Result |
|---|---:|
| Precision | 92.5% |
| Recall | 77.9% |
| F1-score | 84.6% |
| Average precision | 80.3% |
| Fraud cases detected | 74 out of 95 |
| Legitimate transactions incorrectly flagged | 6 |

These are previously recorded test results, not live measurements. The test set was also used to assess an earlier baseline model, so it should not be described as a completely untouched final test set.

## Run Locally

1. Install Python.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Launch the app:

   ```bash
   python -m streamlit run app.py
   ```

## Limitations
- The application is a demonstration, not a production banking system.
- The V1–V28 features are transformed numerical values and are not intuitive raw transaction details.
- Manually entered values may not represent real transactions.
- A fraud prediction is a risk estimate, not proof of fraud.
- Model performance can change when applied to different data.

## Disclaimer
This project is for educational and portfolio purposes only.