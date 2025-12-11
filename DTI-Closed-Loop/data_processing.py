from tdc.multi_pred import DTI
from DeepPurpose import utils as dp_utils
from utils import process_and_clean_df

def load_and_process_data(drug_encoding, target_encoding):
    print("--- Loading BindingDB Data ---")
    data = DTI(name='BindingDB_Kd')
    split = data.get_split(method='cold_split', column_name='Drug')
    
    train, val, test = split['train'], split['valid'], split['test']
 
    train = process_and_clean_df(train, "Train")
    val = process_and_clean_df(val, "Val")
    test = process_and_clean_df(test, "Test")
    
    print("--- Encoding Data (This may take a while) ---")
    train_data = dp_utils.data_process(X_drug=train['Drug'].values, X_target=train['Target'].values, y=train['Y'].values, 
                                    drug_encoding=drug_encoding, target_encoding=target_encoding, 
                                    split_method='no_split')

    val_data = dp_utils.data_process(X_drug=val['Drug'].values, X_target=val['Target'].values, y=val['Y'].values, 
                                    drug_encoding=drug_encoding, target_encoding=target_encoding, 
                                    split_method='no_split')

    test_data = dp_utils.data_process(X_drug=test['Drug'].values, X_target=test['Target'].values, y=test['Y'].values, 
                                    drug_encoding=drug_encoding, target_encoding=target_encoding, 
                                    split_method='no_split')
                                    
    return train_data, val_data, test_data, test