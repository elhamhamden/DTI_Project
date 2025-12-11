from DeepPurpose import utils as dp_utils
from DeepPurpose import DTI as models

def train_model(train_data, val_data, test_data, drug_encoding, target_encoding):
    print("--- Configuring Model ---")
    config = dp_utils.generate_config(drug_encoding=drug_encoding, 
                                      target_encoding=target_encoding, 
                                      cls_hidden_dims=[1024, 1024, 512], 
                                      train_epoch=20, 
                                      LR=0.001, 
                                      batch_size=256,
                                      mpnn_hidden_size=128,
                                      mpnn_depth=3,
                                      cnn_target_filters=[32, 64, 96],
                                      cnn_target_kernels=[4, 8, 12])
    
    model = models.model_initialize(**config)
    
    print("--- Starting Training ---")
    model.train(train_data, val_data, test_data)
    
    model.save_model('./saved_model')
    return model