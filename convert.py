import json
import csv


input_file = "f_secure_key_export.fsk"
output_file = "lastpass_import.csv"

header = ["url", "username", "password", "extra", "name", "grouping", "fav"]
sep = ","

with open(input_file, "r") as fp:
    dct = json.load(fp)

with open(output_file, "w") as fp:
    fp.write(sep.join(header) + "\n")

    for data in dct["data"].values():
        line = []
        line.append(data["url"])
        line.append(data["username"])
        line.append(data["password"])
        line.append(data["notes"])
        line.append(data["service"])
        line.append("")  # Grouping empty
        line.append("0")  # 1 == favourite, 0 == no favourite
        fp.write(sep.join(line) + "\n")
