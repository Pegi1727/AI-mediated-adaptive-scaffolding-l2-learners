# Reproducible analysis script. Run from any working directory; paths resolve from the repository.
options(stringsAsFactors = FALSE)
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (basename(root) == "R") root <- dirname(root)
data_dir <- file.path(root, "data"); out_dir <- file.path(root, "outputs"); fig_dir <- file.path(root, "figures")
dir.create(out_dir, showWarnings=FALSE); dir.create(fig_dir, showWarnings=FALSE)
a <- read.csv(file.path(out_dir,"achievement_prepared_R.csv")); png(file.path(fig_dir,"achievement_pre_post_R.png"),700,500); boxplot(a$Pre,a$Post,names=c("Pre","Post"),ylab="Achievement score",main="Paired achievement scores"); dev.off(); items <- paste0("Q",1:12); png(file.path(fig_dir,"questionnaire_items_R.png"),800,500); barplot(100*colMeans(read.csv(file.path(out_dir,"questionnaire_prepared_R.csv"))[items]),names.arg=items,ylim=c(0,100),ylab="Affirmative (%)"); dev.off(); write.csv(data.frame(metric=c("N","Pre mean","Post mean","Gain mean","Gain SD"),value=c(nrow(a),mean(a$Pre),mean(a$Post),mean(a$Gain),sd(a$Gain))),file.path(out_dir,"report_summary_R.csv"),row.names=FALSE)
