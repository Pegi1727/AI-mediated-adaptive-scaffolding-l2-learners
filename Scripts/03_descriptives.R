# Reproducible analysis script. Run from any working directory; paths resolve from the repository.
options(stringsAsFactors = FALSE)
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (basename(root) == "R") root <- dirname(root)
data_dir <- file.path(root, "data"); out_dir <- file.path(root, "outputs"); fig_dir <- file.path(root, "figures")
dir.create(out_dir, showWarnings=FALSE); dir.create(fig_dir, showWarnings=FALSE)
a <- read.csv(file.path(out_dir,"achievement_prepared_R.csv")); q <- read.csv(file.path(out_dir,"questionnaire_prepared_R.csv")); cols <- c("Pre","Post","Gain"); desc <- data.frame(variable=cols, n=sapply(a[cols],length), mean=sapply(a[cols],mean), sd=sapply(a[cols],sd), median=sapply(a[cols],median)); write.csv(desc,file.path(out_dir,"achievement_descriptives_R.csv"),row.names=FALSE); items <- paste0("Q",1:12); write.csv(data.frame(item=items,n=colSums(q[items]),percent=100*colMeans(q[items])),file.path(out_dir,"questionnaire_items_R.csv"),row.names=FALSE)
