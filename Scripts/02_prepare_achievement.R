# Reproducible analysis script. Run from any working directory; paths resolve from the repository.
options(stringsAsFactors = FALSE)
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (basename(root) == "R") root <- dirname(root)
data_dir <- file.path(root, "data"); out_dir <- file.path(root, "outputs"); fig_dir <- file.path(root, "figures")
dir.create(out_dir, showWarnings=FALSE); dir.create(fig_dir, showWarnings=FALSE)
a <- read.csv(file.path(data_dir,"pre_post_scores_full_50students.csv")); a$Gain <- a$Post-a$Pre; write.csv(a,file.path(out_dir,"achievement_prepared_R.csv"),row.names=FALSE)
q <- read.csv(file.path(data_dir,"questionnaire_post_intervention_corrected.csv")); items <- paste0("Q",1:12); q$Sub1 <- rowSums(q[items[1:4]]); q$Sub2 <- rowSums(q[items[5:8]]); q$Sub3 <- rowSums(q[items[9:12]]); q$Total <- rowSums(q[items]); write.csv(q,file.path(out_dir,"questionnaire_prepared_R.csv"),row.names=FALSE)
