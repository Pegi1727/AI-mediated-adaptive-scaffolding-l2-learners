"""Shared conventions: paths are resolved relative to this file/repository; all analyses are two-sided, paired where appropriate, and preserve raw inputs."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
def main():
    a=pd.read_csv(OUT/'achievement_prepared.csv'); q=pd.read_csv(OUT/'questionnaire_prepared.csv')
    cols=['Pre','Post','Gain']; s=a[cols].agg(['count','mean','std','median','min','max']).T; s.to_csv(OUT/'achievement_descriptives.csv')
    items=[f'Q{i}' for i in range(1,13)]; ip=pd.DataFrame({'item':items,'n':q[items].sum().astype(int),'percent':q[items].mean()*100}); ip.to_csv(OUT/'questionnaire_item_descriptives.csv',index=False)
    scales=['Sub1','Sub2','Sub3','Total']; q[scales].agg(['count','mean','std','median','min','max']).T.to_csv(OUT/'questionnaire_scale_descriptives.csv'); print(s.round(3).to_string())
if __name__=='__main__': main()
