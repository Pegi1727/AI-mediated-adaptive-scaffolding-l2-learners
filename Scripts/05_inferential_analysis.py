"""Shared conventions: paths are resolved relative to this file/repository; all analyses are two-sided, paired where appropriate, and preserve raw inputs."""
from pathlib import Path
import pandas as pd, numpy as np
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
def main():
    a=pd.read_csv(OUT/'achievement_prepared.csv'); d=a.Gain.dropna(); n=len(d); t,p=stats.ttest_rel(a.Post,a.Pre); dz=d.mean()/d.std(ddof=1); ci=stats.t.ppf(.975,n-1)*d.std(ddof=1)/np.sqrt(n); w,pw=stats.wilcoxon(a.Post,a.Pre,alternative='two-sided',method='auto')
    result=pd.DataFrame([{'analysis':'paired_t_test','estimate_gain':d.mean(),'statistic':t,'df':n-1,'p_value':p,'effect_dz':dz,'ci95_low':d.mean()-ci,'ci95_high':d.mean()+ci},{'analysis':'wilcoxon_signed_rank','estimate_gain':d.median(),'statistic':w,'df':None,'p_value':pw,'effect_dz':None,'ci95_low':None,'ci95_high':None}]); result.to_csv(OUT/'inferential_results.csv',index=False); print(result.to_string(index=False))
if __name__=='__main__': main()
