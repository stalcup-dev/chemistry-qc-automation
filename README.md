QC Results Automation with Westgard Rule Analysis
Clinical Chemistry Process Automation Demo
________________________________________
Project Overview
Automates aggregation and QC analysis of daily clinical chemistry results using Westgard rules. Reduces error-prone manual work, instantly flags failed QC parameters—critical for lab quality and compliance.
________________________________________
Quick Start
1.	Download code and sample data.
2.	Install Python 3 and pandas (pip install pandas).
3.	Put daily QC .csv files in the Daily_QC_Results/ folder.
4.	Run: python qc_weekly_summary.py
5.	Review outputs:
o	weekly_qc_summary.csv
o	weekly_qc_report.txt
________________________________________
Folder Structure
CopyEdit
project_folder/
├── qc_weekly_summary.py
├── Daily_QC_Results/
│   ├── qc_2024-05-20.csv
│   ├── qc_2024-05-21.csv
│   └── qc_2024-05-22.csv
└── README.md
________________________________________
Westgard Rules Implemented
•	1-2s: Result >2SD from mean (warning)
•	1-3s: Result >3SD from mean (fail)
•	2-2s: Two consecutive >2SD, same side (fail)
•	R-4s: One >+2SD, next <-2SD (fail)
•	4-1s: Four >1SD, same side (warning)
•	10x: Ten consecutive one side of mean (warning)
________________________________________
Why This Matters
•	Lab compliance: Instantly spots QC failures for audit and patient safety.
•	Efficiency: Zero manual collation, instant flagging.
•	Portfolio Value: Proves technical AND domain skills.
________________________________________
Example Input & Output
•	Input:
sql
CopyEdit
Date,TestName,Result,Mean,SD,ReferenceLow,ReferenceHigh,WestgardRuleViolated,Pass,Comments
2024-05-20,Glucose,98,100,5,70,110,None,Pass,Within 2SD
•	Output:
o	weekly_qc_summary.csv
o	weekly_qc_report.txt (flags all failures/warnings for the week)
 
________________________________________
Tech Stack
•	Python 3
•	pandas
________________________________________
Credits
Designed and implemented by Allen Stalcup as part of a clinical data/process automation portfolio.
Contact: [allen.stalc@gmail.com]

