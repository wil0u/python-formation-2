setwd('C:\\Users\\dgr\\Documents\\Formations\\R\\R_ML\\data')
library(tidyverse)

# install.packages("ripa")
# install.packages("jpeg")
# library(ripa)
# library(jpeg)
# tux <-readJPEG("tux.jpg")
# dim(tux)
# length(tux)
# 
# head(tux)
# str(tux)
#img <- readJPEG(system.file("img", "Rlogo.jpg", package="jpeg"))


# 
# tux <- imagematrix(tux,type='grey')
# tux[1:8,1:20]
# dim(tux)
# plot(tux)



library(imager)

# https://dahtah.github.io/imager/imager.html
im <- load.image("tux.jpg")
#Images are represented as 4D numeric arrays
# The four dimensions are labelled x,y,z,c.
# The first two are the usual spatial dimensions, 
# the third one will usually correspond to depth or time,
# and the fourth one is colour.
# If you only have grayscale images then the two extra dimensions are obviously pointless, 
# but they won't bother you much. 
# Your objects will still be officially 4 dimensional, with two trailing flat dimensions.
# Pixels are stored in the following manner: we scan the image beginning at the upper-left corner, along the x axis.
#Once we hit the end of the scanline, we move to the next line.
dim(im)
length(im)
x11()
plot(im)

head(im)
str(im)
# 
plot(im[300:320,1200:1220,1,1])


# on applique un filtre qui detecte les traits
im.xedges <- deriche(im,2,order=2,axis="x") #Edge detector le long de x-axis
plot(im.xedges)

im.yedges <- deriche(im,2,order=2,axis="y") #Edge detector le long de y-axis
plot(im.yedges)
#Chain operations avec  pipe operator ( magrittr)
deriche(im,2,order=2,axis="x") %>% deriche(2,order=2,axis="y") %>% plot

# EN N&B, retourne une image sur un seul canal de couleur
tux_nb<-grayscale(im)
plot(tux_nb)
dim(tux_nb)


# fonction qui prend en entrée la matrice des pixels
# et le nombre de dimension de compression


reduce <- function(A,dim) { 
  #Calcul SVD 
  sing <- svd(A) 
  #approxime chaque matrice d?composee avec les dimensions souhait?es 
  u<-as.matrix(sing$u[, 1:dim]) 
  v<-as.matrix(sing$v[, 1:dim]) 
  d<-as.matrix(diag(sing$d)[1:dim, 1:dim])
  #Create the new approximated matrix sur les n prem dimensions
  return(as.cimg(u%*%d%*%t(v)))
}
  
 # combien notre matrice a de val singulieres
  tux_d <- svd(tux_nb) 
  length(tux_d$d) 
  #[1] 1038 => val sing 
  
  # approxime la matrice sur 1 dim
  img_reduite<-reduce(tux_nb,1)
  plot(img_reduite)
  dim(img_reduite)
  dim()
  # avec 5 % (50 singular values)
  plot(reduce(tux_nb,10))
  
  #avec 5% des data on est capable de representer une bonne approximation
  