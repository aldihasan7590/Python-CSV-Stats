"""
Quick CSV stats per numeric column.
Usage:
  python py_csv_stats.py data.csv
Outputs count, min, max, mean for each numeric column.
"""
import csv, sys, math

def is_float(x:str)->bool:
    try:
        float(x); return True
    except: return False

def summarize(path):
    with open(path, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("No rows."); return
    cols = rows[0].keys()
    for c in cols:
        vals = [float(r[c]) for r in rows if r.get(c) not in (None,"") and is_float(r[c])]
        if not vals:
            print(f"[{c}] non-numeric or empty")
            continue
        n = len(vals)
        mn, mx = min(vals), max(vals)
        mean = sum(vals)/n
        # stddev (population)
        var = sum((v-mean)**2 for v in vals)/n
        sd = math.sqrt(var)
        print(f"[{c}] n={n} min={mn:.4g} max={mx:.4g} mean={mean:.4g} sd={sd:.4g}")

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Usage: python py_csv_stats.py file.csv"); raise SystemExit(1)
    summarize(sys.argv[1])
