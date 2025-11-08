import pandas as pd

# === CONFIG ===
csv_file = "data.csv"       # your input CSV filename
output_file = "output.txt"  # your desired output file
template = '{{ num: {num} , link: " {url} "}},'

# === READ CSV ===
df = pd.read_csv(csv_file)

# === GENERATE OUTPUT ===
lines = [template.format(num=row['num'], url=row['url']) for _, row in df.iterrows()]

# === WRITE TO TXT ===
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"✅ Successfully created {output_file} with {len(lines)} entries.")
