# Reproducible analysis script. Run from any working directory; paths resolve from the repository.
options(stringsAsFactors = FALSE)
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (basename(root) == "R") root <- dirname(root)
data_dir <- file.path(root, "data"); out_dir <- file.path(root, "outputs"); fig_dir <- file.path(root, "figures")
dir.create(out_dir, showWarnings=FALSE); dir.create(fig_dir, showWarnings=FALSE)
a <- read.csv(file.path(out_dir,"achievement_prepared_R.csv")); z <- lapply(c("Pre","Post","Gain"), function(v){x <- shapiro.test(a[[v]]); data.frame(variable=v,W=unname(x$statistic),p_value=x$p.value,n=length(a[[v]]))}); write.csv(do.call(rbind,z),file.path(out_dir,"assumption_tests_R.csv"),row.names=FALSE)
