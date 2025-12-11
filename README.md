# 🧬 Closed-Loop Drug-Target Interaction (DTI) Optimization

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![DeepPurpose](https://img.shields.io/badge/Bioinformatics-DeepPurpose-green)
![RDKit](https://img.shields.io/badge/Cheminformatics-RDKit-yellow)

## 📌 Overview
This project implements a **Closed-Loop AI System** for optimizing drug molecule affinity against specific protein targets. It combines a Deep Learning predictor (Oracle) with an iterative modification algorithm to evolve drug candidates for higher binding affinity (**pKd**).

The system leverages the **BindingDB** dataset and uses **Message Passing Neural Networks (MPNN)** for drug encoding and **Convolutional Neural Networks (CNN)** for target protein encoding.

## 🚀 Key Features
- **State-of-the-Art Encodings:** Uses MPNN for molecular graphs (Drugs) and CNN for amino acid sequences (Targets).
- **Cold Split Validation:** Ensures robust testing by evaluating on unseen drugs.
- **Closed-Loop Optimization:** Iteratively mutates drug structures and evaluates them using the trained AI Oracle.
- **Data Cleaning:** Automated handling of large molecules and outliers using `PyTDC` and `RDKit`.
- **Visualization:** Tracks and plots the optimization trajectory of binding affinity over time.

## 📂 Project Structure
```text
DTI-Closed-Loop/
│
├── data_processing.py    # Data loading, cleaning, and encoding (BindingDB)
├── model_training.py     # DeepPurpose model configuration and training
├── optimization.py       # The closed-loop controller and mutation logic
├── utils.py              # Helper functions (e.g., DeepPurpose hacks)
├── main.py               # Main entry point to run the pipeline
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
