import random
from rdkit import Chem
from DeepPurpose import utils as dp_utils

def oracle_sensor(drug_smiles, target_protein_seq, model, drug_encoding, target_encoding):
    try:
        X_drug = [drug_smiles]
        X_target = [target_protein_seq]
        y = [0] 
        
        processed_data = dp_utils.data_process(X_drug, X_target, y, 
                                            drug_encoding, target_encoding, 
                                            split_method='no_split')
        
        pred = model.predict(processed_data)
        return pred[0]
    except Exception:
        return 0.0

def controller_mutate(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None: return smiles
        
        action = random.choice(['add_C', 'add_O', 'add_N'])
        new_smiles = smiles
        
        if action == 'add_C': new_smiles = smiles + "C"
        elif action == 'add_O': new_smiles = smiles.replace("C", "CO", 1)
        elif action == 'add_N': new_smiles = smiles + "N"
            
        if Chem.MolFromSmiles(new_smiles): return new_smiles
        return smiles
    except:
        return smiles

def run_closed_loop(model, target_seq, start_drug, iterations, drug_enc, target_enc):
    print("\n--- Starting Closed-Loop Optimization ---")
    
    best_drug = start_drug
    best_score = oracle_sensor(start_drug, target_seq, model, drug_enc, target_enc)
    
    print(f"Initial Drug: {start_drug}")
    print(f"Initial pKd: {best_score:.4f}")
    
    history = [best_score]

    for i in range(iterations):
        mutated_drug = controller_mutate(best_drug)
        
        if mutated_drug == best_drug: continue
        
        new_score = oracle_sensor(mutated_drug, target_seq, model, drug_enc, target_enc)
        
        if new_score > best_score:
            print(f"Iter {i+1}: Improved! {best_score:.4f} -> {new_score:.4f} | Drug: {mutated_drug}")
            best_drug = mutated_drug
            best_score = new_score
        
        history.append(best_score)
        
    print(f"\nOptimization Finished. Best Drug: {best_drug} with pKd: {best_score:.4f}")
    return history