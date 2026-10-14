import joblib
import streamlit as st
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


# Locate the folder containing this Python file
BASE_DIR = Path(__file__).parent

# Load the saved model
model_path = BASE_DIR / "fraud_detection_model.joblib"
model = joblib.load(model_path)


# Load the saved threshold configuration
config_path = BASE_DIR / "fraud_detection_config.joblib"
config = joblib.load(config_path)

threshold = config["threshold"]


# Configure the Streamlit page
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="🛡️",
    layout="wide"
)


# Configure the sidebar
st.sidebar.title("About This Project")

st.sidebar.write(
    "This application uses a trained Random Forest "
    "model to estimate the probability of credit card fraud."
)

st.sidebar.subheader("Decision Threshold")
st.sidebar.write(f"Fraud threshold: {threshold:.0%}")

st.sidebar.subheader("Important Notes")
st.sidebar.write(
    "A flagged transaction is not proof of fraud."
)

st.sidebar.write(
    "The V1–V28 features are transformed numerical values. "
    "Manual inputs are for demonstration purposes."
)


st.title("🛡️ Credit Card Fraud Detection")

st.write(
    "An interactive machine learning application that estimates "
    "the probability of credit card fraud using a trained "
    "Random Forest classifier."
)

st.caption(
    "Portfolio project | Machine Learning | Streamlit"
)

st.success("Model loaded successfully!")

st.write(f"Decision threshold: {threshold:.2f}")
st.write(f"Number of model input features: {model.n_features_in_}")

st.divider()

st.subheader("Model Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model", "Random Forest")

with col2:
    st.metric("Input Features", model.n_features_in_)

with col3:
    st.metric("Fraud Threshold", f"{threshold:.0%}")


st.divider()

st.subheader("Model Evaluation")

st.caption(
    "Test-set results at a fraud decision threshold of 20%. "
    "These metrics describe the model's earlier evaluation."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Precision", "92.5%")

with col2:
    st.metric("Recall", "77.9%")

with col3:
    st.metric("F1-Score", "84.6%")

with col4:
    st.metric("Average Precision", "80.3%")

st.write("**Fraud detection breakdown**")

col1, col2 = st.columns(2)

with col1:
    st.metric("Fraud Cases Detected", "74 / 95")

with col2:
    st.metric("Legitimate Transactions Flagged", "6")


st.divider()

st.subheader("Confusion Matrix")

# Recorded test-set confusion matrix
confusion_matrix = [
    [56645, 6],
    [21, 74]
]

fig, ax = plt.subplots(figsize=(6, 4))

sns.heatmap(
    confusion_matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Legitimate", "Fraud"],
    yticklabels=["Legitimate", "Fraud"],
    ax=ax
)

ax.set_xlabel("Predicted Class")
ax.set_ylabel("Actual Class")
ax.set_title("Random Forest Test Results")

st.pyplot(fig)
plt.close(fig)
st.header("Enter Transaction Details")
# Get transaction time from the user
transaction_time = st.number_input(
    "Transaction Time (seconds)",
    min_value=0.0,
    value=0.0
)

# Get transaction amount from the user
transaction_amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=1000.0
)

st.write("Transaction time:", transaction_time)
st.write("Transaction amount:", transaction_amount)

st.subheader("Additional Transaction Features")

# Create input fields for V1 through V28
features = {}

for i in range(1, 29):
    features[f"V{i}"] = st.number_input(
        f"V{i}",
        value=0.0,
        format="%.6f"
    )

import pandas as pd

# Create a dictionary containing all 30 input features
input_data = {
    "Time": [transaction_time],
    **{name: [features[name]] for name in features},
    "Amount": [transaction_amount]
}

# Convert the dictionary into a DataFrame
input_df = pd.DataFrame(input_data)

# Arrange the columns in the exact order used during training
input_df = input_df[X.columns] if "X" in globals() else input_df[
    ["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount"]
]

st.subheader("Transaction Input Preview")
st.dataframe(input_df)

st.write("Number of input features:", input_df.shape[1])


st.divider()

st.subheader("Fraud Detection")

if st.button("Predict Transaction", type="primary"):

    # Calculate the probability of fraud
    fraud_probability = model.predict_proba(input_df)[0][1]

    # Compare with the saved threshold
    if fraud_probability >= threshold:
        st.error(
            "Warning: This transaction is flagged as potentially fraudulent."
        )
    else:
        st.success("This transaction is not flagged as fraudulent.")

    # Display prediction results
    st.write(f"Fraud probability: {fraud_probability:.2%}")
    st.write(f"Decision threshold: {threshold:.0%}")

    # Display a visual indicator
    st.progress(float(fraud_probability))

    # Explain the prediction
    if fraud_probability >= threshold:
        st.write("The probability meets or exceeds the fraud threshold.")
    else:
        st.write("The probability is below the fraud threshold.")