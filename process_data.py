import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('data/export.xml')
root = tree.getroot()

data = []

for record in root.findall('Record'):
    entry = {
        'type': record.get('type'),
        'value': record.get('value'),
        'startDate': record.get('startDate'),
        'endDate': record.get('endDate')
    }
    data.append(entry)

df = pd.DataFrame(data)

df.to_csv('output.csv', index=False)

print("Done")
