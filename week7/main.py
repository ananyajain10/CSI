import os
import pandas as pd
import re

# Folder paths
data_folder = 'data'
output_folder = 'output'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# 1. Load CUST_MSTR files
cust_files = [f for f in os.listdir(data_folder) if f.startswith("CUST_MSTR_")]

cust_dfs = []

for file in cust_files:
    match = re.search(r'CUST_MSTR_(\d{8})\.csv', file)
    if match:
        date_str = match.group(1)
        date_fmt = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
        
        df = pd.read_csv(os.path.join(data_folder, file))
        df['Date'] = date_fmt
        cust_dfs.append(df)

# Truncate + load
if cust_dfs:
    final_cust = pd.concat(cust_dfs, ignore_index=True)
    final_cust.to_csv(os.path.join(output_folder, "CUST_MSTR.csv"), index=False)
    print("✅ CUST_MSTR loaded.")

# 2. Load master_child_export files
master_files = [f for f in os.listdir(data_folder) if f.startswith("master_child_export-")]

master_dfs = []

for file in master_files:
    match = re.search(r'master_child_export-(\d{8})\.csv', file)
    if match:
        date_key = match.group(1)
        date_fmt = f"{date_key[:4]}-{date_key[4:6]}-{date_key[6:]}"
        
        df = pd.read_csv(os.path.join(data_folder, file))
        df['DateKey'] = date_key
        df['Date'] = date_fmt
        master_dfs.append(df)

if master_dfs:
    final_master = pd.concat(master_dfs, ignore_index=True)
    final_master.to_csv(os.path.join(output_folder, "master_child.csv"), index=False)
    print("✅ master_child loaded.")

# 3. Load H_ECOM_ORDER as-is
order_path = os.path.join(data_folder, "H_ECOM_ORDER.csv")

if os.path.exists(order_path):
    df_order = pd.read_csv(order_path)
    df_order.to_csv(os.path.join(output_folder, "H_ECOM_Orders.csv"), index=False)
    print("✅ H_ECOM_Orders loaded.")
