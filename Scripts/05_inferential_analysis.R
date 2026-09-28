# Reproducible analysis script. Run from any working directory; paths resolve from the repository.
options(stringsAsFactors = FALSE)
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (basename(root) == "R") root <- dirname(root)
data_dir <- file.path(root, "data"); out_dir <- file.path(root, "outputs"); fig_dir <- file.path(root, "figures")
dir.create(out_dir, showWarnings=FALSE); dir.create(fig_dir, showWarnings=FALSE)
a <- read.csv(file.path(out_dir,"achievement_prepared_R.csv")); tt <- t.test(a$Post,a$Pre,paired=TRUE); d <- a$Gain; wx <- wilcox.test(a$Post,a$Pre,paired=TRUE,exact=FALSE); out <- data.frame(analysis=c("paired_t_test","wilcoxon_signed_rank"),statistic=c(unname(tt$statistic),unname(wx$statistic)),df=c(tt$parameter,NA),p_value=c(tt$p.value,wx$p.value),mean_gain=c(mean(d),median(d)),effect_dz=c(mean(d)/sd(d),NA)); write.csv(out,file.path(out_dir,"inferential_results_R.csv"),row.names=FALSE)
