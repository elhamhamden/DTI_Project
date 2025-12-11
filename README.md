# 🧬 Closed-Loop Drug-Target Interaction (DTI) Optimization

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![DeepPurpose](https://img.shields.io/badge/Bioinformatics-DeepPurpose-green)
![RDKit](https://img.shields.io/badge/Cheminformatics-RDKit-yellow)

## 📌 Overview

This project implements an AI-driven **Closed-Loop System** for optimizing drug molecule affinity against specific protein targets. It combines a Deep Learning predictor (The Oracle) with an iterative modification algorithm (The Controller) to evolve drug candidates for higher binding affinity (**pKd**).

The system leverages the **BindingDB** dataset and utilizes state-of-the-art encoders: **Message Passing Neural Networks (MPNN)** for drug molecules and **Convolutional Neural Networks (CNN)** for target protein sequences.

## 🚀 Key Features

* **Advanced Encodings:** Uses Graph Neural Networks (MPNN) for molecular graphs and CNN for amino acid sequences.
* **Robust Evaluation:** Implements **Cold Split** validation to test the model on unseen drugs, ensuring realistic performance metrics.
* **Closed-Loop Optimization:** An iterative feedback loop that mutates drug structures and evaluates them using the trained AI Oracle to find better candidates.
* **Automated Processing:** Handles data cleaning, large molecule filtering, and Kd to pKd conversion automatically.

## 📂 Project Structure

```text
DTI-Closed-Loop/
│
├── data_processing.py    # Handles data loading, cleaning, and splitting from BindingDB
├── model_training.py     # Configures and trains the DeepPurpose model (MPNN + CNN)
├── optimization.py       # Contains the Oracle (Predictor) and Controller (Mutator) logic
├── utils.py              # Utility functions and library fixes (e.g., MAX_ATOM fix)
├── main.py               # The entry point to run the entire pipeline
├── requirements.txt      # List of required Python libraries
└── README.md             # Project documentation
```

## 🛠️ Installation

**Clone the repository:**

```bash
git clone https://github.com/elhamhamden/DTI_Project.git
cd DTI_Project
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

> **Note:** This project includes a custom fix in `utils.py` that automatically adjusts the `MAX_ATOM` parameter in the DeepPurpose library to handle complex molecules without crashing.

---

## 💻 Usage

To run the full pipeline (Data Processing → Training → Optimization), simply execute:

```bash
python main.py
```

### **What happens when you run this?**

* The script downloads and processes the BindingDB dataset.
* It trains the DTI predictor model for **20 epochs**.
* The model is saved locally.
* The system picks a starting drug (e.g., *Aspirin*) and a target protein.
* It runs the Closed-Loop Optimization for **20 iterations** to generate a drug with higher affinity.
* A trajectory plot is saved as **`optimization_result.png`**.

---

## 🧠 Methodology

### **1. The Predictor (AI Oracle)**

* **Framework:** DeepPurpose
* **Inputs:** Drug SMILES string + Target Amino Acid Sequence
* **Output:** Predicted **pKd** (Binding Affinity)

### **2. The Controller (Optimizer)**

* Takes a starting molecule and applies chemical modifications (adding atoms like **C, N, O**).
* Candidates are validated using **RDKit** for chemical stability.
* If the predicted pKd improves, the new molecule becomes the baseline for the next iteration.

---

## 📊 Results

The system successfully evolves a starting molecule into a modified version with **higher predicted binding affinity**.

> ![Optimization Result](optimization_result.png)

---

## 🔮 Future Work

* [ ] Replace random mutation with **GANs** for de novo drug design.
* [ ] Implement **Reinforcement Learning (RL)** to guide the optimization policy.
* [ ] Integrate **QED** (drug-likeness) and **SA** (synthetic accessibility) as constraints.
