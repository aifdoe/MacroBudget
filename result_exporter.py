import json


def export_result_to_json(result, file_path):
    with open(file_path, mode="w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
        file.write("\n")