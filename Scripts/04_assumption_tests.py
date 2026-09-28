"""Shared conventions: paths are resolved relative to this file/repository; all analyses are two-sided, paired where appropriate, and preserve raw inputs."""
from pathlib import Path
import pandas as pd
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
def main():
    a=pd.read_csv(OUT/'achievement_prepared.csv'); rows=[]
    for c in ['Pre','Post','Gain']:
        x=a[c].dropna(); w,p=stats.shapiro(x); rows.append({'variable':c,'test':'Shapiro-Wilk','statistic':w,'p_value':p,'n':len(x)})
    # paired difference is the inferential target; no homogeneity test is required for paired t-test
    pd.DataFrame(rows).to_csv(OUT/'assumption_tests.csv',index=False); print(pd.DataFrame(rows).to_string(index=False))
if __name__=='__main__': main()
