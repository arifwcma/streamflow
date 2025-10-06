import os
import pandas as pd

base = r"C:\Users\m.rahman\PythonProject\streamflow"
flow_path = os.path.join(base, "raw_data", "415247.streamflow.Raw_Data.csv")
level_path = os.path.join(base, "raw_data", "415247.streamwaterlevel.Raw_Data.csv")
out_dir = os.path.join(base, "data")
os.makedirs(out_dir, exist_ok=True)

flow = pd.read_csv(flow_path)
level = pd.read_csv(level_path)

merged = pd.merge(flow, level, on="Date Time", suffixes=("_flow", "_level"))
merged = merged[["Date Time", "VALUE_flow", "VALUE_level"]]
merged.columns = ["recorded_time", "flow", "level"]

merged.to_csv(os.path.join(out_dir, "merged.csv"), index=False)
