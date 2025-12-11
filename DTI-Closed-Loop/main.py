import utils
import data_processing
import model_training
import optimization
import matplotlib.pyplot as plt

def main():
    utils.fix_max_atom()
    
    DRUG_ENCODING = 'MPNN'
    TARGET_ENCODING = 'CNN'
    
    train, val, test, test_df_raw = data_processing.load_and_process_data(DRUG_ENCODING, TARGET_ENCODING)
    
    model = model_training.train_model(train, val, test, DRUG_ENCODING, TARGET_ENCODING)
    
    target_protein_seq = test_df_raw['Target'].values[0]
    start_drug = "CC(=O)OC1=CC=CC=C1C(=O)O" # Aspirin as starting point
    
    history = optimization.run_closed_loop(model, 
                                           target_protein_seq, 
                                           start_drug, 
                                           iterations=20, 
                                           drug_enc=DRUG_ENCODING, 
                                           target_enc=TARGET_ENCODING)
    
    plt.figure(figsize=(10, 6))
    plt.plot(history, marker='o', color='green')
    plt.title('Optimization Trajectory')
    plt.ylabel('Binding Affinity (pKd)')
    plt.xlabel('Steps')
    plt.grid(True)
    plt.savefig('optimization_result.png')
    print("Graph saved as optimization_result.png")

if __name__ == "__main__":
    main()