"""Shared conventions: paths are resolved relative to this file/repository; all analyses are two-sided, paired where appropriate, and preserve raw inputs."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'data'; OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
def main():
    a=pd.read_csv(DATA/'pre_post_scores_full_50students.csv'); a['Gain']=a['Post']-a['Pre']; a.to_csv(OUT/'achievement_prepared.csv',index=False)
    q=pd.read_csv(DATA/'questionnaire_post_intervention_corrected.csv'); items=[f'Q{i}' for i in range(1,13)]
    q['Sub1']=q[items[:4]].sum(axis=1); q['Sub2']=q[items[4:8]].sum(axis=1); q['Sub3']=q[items[8:]].sum(axis=1); q['Total']=q[items].sum(axis=1); q.to_csv(OUT/'questionnaire_prepared.csv',index=False)
    print(f'Wrote {len(a)} achievement pairs and {len(q)} questionnaire records')
if __name__=='__main__': main()
