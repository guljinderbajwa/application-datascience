from pathlib import Path
import json
file_path = Path(".").resolve().parent.parent /"labeled_sentences.json"
print(file_path)
with open(file_path, "r", encoding="utf-8") as file:
    # 👇 This line MUST be indented
    data = json.load(file)

for record in data[:10]:
    record_id = record.get("id", None)
    text = record.get("text", "")
    print(record_id)