library(readr)
insurance<-read.csv(file.choose())
my_data<-insurance

scaled_data<-scale(my_data)

twss<-NULL

for (i in 2:10){
  twss<-c(twss,kmeans(scaled_data,centers = i)$tot.withinss)
}
twss


plot(2:10,twss,type = "b",xlab = "number of cluster",ylab = "with sum of squares")
########

fit<-kmeans(scaled_data,3)
str(fit)

fit<-kmeans(scaled_data,4)
str(fit)

fit<-kmeans(scaled_data,5)
str(fit)

fit<-kmeans(scaled_data,6)
str(fit)

final<-data.frame(fit$cluster,insurance)
