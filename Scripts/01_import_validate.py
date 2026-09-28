"""Shared conventions: paths are resolved relative to this file/repository; all analyses are two-sided, paired where appropriate, and preserve raw inputs."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'data'; OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
def check_binary(df, cols):
    bad={c:sorted(set(df[c].dropna())-{0,1}) for c in cols}; return {k:v for k,v in bad.items() if v}
def main():
    ach=pd.read_csv(DATA/'pre_post_scores_full_50students.csv'); q=pd.read_csv(DATA/'questionnaire_post_intervention_corrected.csv')
    assert len(ach)==50 and ach[['Pre','Post']].notna().all().all(), 'Achievement must contain 50 complete pairs'
    assert ach.Student.is_unique and q.ID.is_unique, 'IDs must be unique'
    qcols=[f'Q{i}' for i in range(1,13)]; bad=check_binary(q,qcols); assert not bad, f'Non-binary questionnaire values: {bad}'
    assert (q.Sub1==q[qcols[:4]].sum(axis=1)).all() and (q.Sub2==q[qcols[4:8]].sum(axis=1)).all() and (q.Sub3==q[qcols[8:]].sum(axis=1)).all()
    report=pd.DataFrame({'check':['achievement_n','questionnaire_n','unique_achievement_ids','unique_questionnaire_ids','binary_items','derived_scales'],'value':[len(ach),len(q),ach.Student.nunique(),q.ID.nunique(),True,True]})
    report.to_csv(OUT/'validation_report.csv',index=False); print(report.to_string(index=False))
if __name__=='__main__': main()
