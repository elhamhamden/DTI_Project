import os
import re
import importlib
import DeepPurpose
from DeepPurpose import utils as dp_utils

def fix_max_atom():
    file_path = os.path.join(os.path.dirname(DeepPurpose.__file__), 'utils.py')
    print(f"Found utils.py at: {file_path}")

    with open(file_path, 'r') as f:
        content = f.read()

    if 'MAX_ATOM = 2000' not in content:
        new_content = re.sub(r'MAX_ATOM\s*=\s*\d+', 'MAX_ATOM = 2000', content)
        with open(file_path, 'w') as f:
            f.write(new_content)
        
        importlib.reload(dp_utils)
        print("Success! MAX_ATOM is set to 2000")
    else:
        print("MAX_ATOM is already set to 2000")

def process_and_clean_df(df, name="df"):
    import numpy as np
    original_len = len(df)
    
    df = df[df['Y'] <= 10000]
    df['Y'] = -np.log10((df['Y'] * 1e-9) + 1e-10)
    
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.dropna(subset=['Drug', 'Target', 'Y'])
    
    df['Drug'] = df['Drug'].astype(str)
    df['Target'] = df['Target'].astype(str)

    df = df[df['Target'].str.len() <= 2500]
    df = df[df['Drug'].str.len() <= 100]
    
    print(f"[{name}] Processed: Started with {original_len} -> Ended with {len(df)}")
    return df