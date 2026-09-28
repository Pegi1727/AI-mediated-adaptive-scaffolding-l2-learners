"""Shared conventions: paths are resolved relative to this file/repository; all analyses are two-sided, paired where appropriate, and preserve raw inputs."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'outputs'; FIG=ROOT/'figures'; OUT.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
def main():
    a=pd.read_csv(OUT/'achievement_prepared.csv'); q=pd.read_csv(OUT/'questionnaire_prepared.csv')
    fig,ax=plt.subplots(figsize=(6,4)); ax.boxplot([a.Pre,a.Post],labels=['Pre','Post']); ax.set_ylabel('Achievement score'); ax.set_title('Paired achievement scores'); fig.tight_layout(); fig.savefig(FIG/'achievement_pre_post.png',dpi=180); plt.close(fig)
    items=[f'Q{i}' for i in range(1,13)]; fig,ax=plt.subplots(figsize=(8,4)); ax.bar(items,q[items].mean()*100); ax.set_ylim(0,100); ax.set_ylabel('Affirmative (%)'); ax.set_title('Questionnaire item profile'); fig.tight_layout(); fig.savefig(FIG/'questionnaire_items.png',dpi=180); plt.close(fig)
    summary=pd.DataFrame({'metric':['N','Pre mean','Post mean','Gain mean','Gain SD'],'value':[len(a),a.Pre.mean(),a.Post.mean(),a.Gain.mean(),a.Gain.std(ddof=1)]}); summary.to_csv(OUT/'report_summary.csv',index=False); print(summary.to_string(index=False))
if __name__=='__main__': main()
