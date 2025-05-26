import pandas as pd
import os

# Path to your QC CSV folder
qc_folder = "Daily_QC_Results"  # Use your local path

# List all files in the folder
files = [f for f in os.listdir(qc_folder) if f.endswith('.csv')]

# Read and combine all files
df_list = []
for file in files:
    df = pd.read_csv(os.path.join(qc_folder, file))
    df_list.append(df)
qc_all = pd.concat(df_list, ignore_index=True)

# Sort by Date and TestName for easier trend spotting
qc_all = qc_all.sort_values(by=["TestName", "Date"])

# Identify all fails and warnings
failures = qc_all[qc_all['Pass'] == 'Fail']
warnings = qc_all[qc_all['Pass'] == 'Warning']

# Output 1: Combined CSV for the week
qc_all.to_csv("weekly_qc_summary.csv", index=False)

# Output 2: Human-readable report
with open("weekly_qc_report.txt", "w") as f:
    f.write("WEEKLY QC SUMMARY: WESTGARD VIOLATIONS\n\n")
    f.write("=== FAILURES (Immediate Investigation Needed) ===\n")
    if not failures.empty:
        for idx, row in failures.iterrows():
            f.write(f"{row['Date']} | {row['TestName']} | {row['Result']} | Rule: {row['WestgardRuleViolated']} | {row['Comments']}\n")
    else:
        f.write("None! All critical Westgard checks passed.\n")
    
    f.write("\n=== WARNINGS (Monitor for Trends) ===\n")
    if not warnings.empty:
        for idx, row in warnings.iterrows():
            f.write(f"{row['Date']} | {row['TestName']} | {row['Result']} | Rule: {row['WestgardRuleViolated']} | {row['Comments']}\n")
    else:
        f.write("None! No warnings this week.\n")