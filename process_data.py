import json
import pandas as pd
import os

data = []

folder_path = "data/"

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(root, file)) as f:
                try:
                    j = json.load(f)
                    
                    if "points" in j:
                        for point in j["points"]:
                            entry = {}
                            
                            entry["time"] = point.get("startTimeNanos", "")
                            
                            if "value" in point:
                                for v in point["value"]:
                                    if "intVal" in v:
                                        entry["value"] = v["intVal"]
                                    elif "fpVal" in v:
                                        entry["value"] = v["fpVal"]
                            
                            data.append(entry)
                except:
                    pass

df = pd.DataFrame(data)

df.to_csv("output.csv", index=False)

print("Done")
