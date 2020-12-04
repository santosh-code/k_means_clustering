library(readr)
airlines<-read.csv(file.choose())
my_data<-airlines[,-1]

scaled_data<-scale(my_data)

twss<-NULL

for (i in 2:6){
  twss<-c(twss,kmeans(scaled_data,centers = i)$tot.withinss)
}
twss


plot(2:6,twss,type = "b",xlab = "number of cluster",ylab = "with sum of squares")
########

fit<-kmeans(scaled_data,3)
str(fit)

fit<-kmeans(scaled_data,4)
str(fit)

fit<-kmeans(scaled_data,5)
str(fit)

fit<-kmeans(scaled_data,6)
str(fit)

final<-data.frame(fit$cluster,crime_data)

#######hireracial clustering
d <- dist(my_data, method = "euclidean")
######distance method
fit <- hclust(d, method="complete")
plot(fit)
#######
fit <- hclust(d, method="ward.D2")
fit <- as.dendrogram(fit)
cd = color_branches(fit,k=3) #Coloured dendrogram branches
plot(cd)

#######

plot(fit) # display dendrogram
plot(fit, hang=-1)
groups <- cutree(fit, k=6) # cut tree into 3 clusters


rect.hclust(fit, k=2, border="red")

