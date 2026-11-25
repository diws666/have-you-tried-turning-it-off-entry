import os

LINE = "Sir, I have been on this call for forty minutes. The computer is fine. It is you I am worried about."  # verified: 100 chars

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(LINE)

print(len(LINE))
