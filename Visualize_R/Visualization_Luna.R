# setwd("/Users/lunafrauhammer/Desktop")

list <- readLines("results_edit.txt")


## Speichert die einzelnen Loesungen in eigenen Vektoren ##
for(i in 1:12){
  nam <- paste("l", i, sep = "")
  assign(nam, as.integer(unlist(strsplit(list[i], split = " "))))
}

## Koordinaten erstellen ## 
x <- c(2, 3, 4, 1.5, 2.5, 3.5, 4.5, 1, 2, 3, 4, 5, 1.5, 2.5, 3.5, 4.5, 2, 3, 4)
y <- c(5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1)

## Farben festlegen ## 
colors <- c("red", "blue", "green", "yellow", "grey", "orange", 
            "pink", "cadetblue1", "darkorchid1", "darkgreen", 
            "antiquewhite", "black", "coral3", "blue4", 
            "mediumpurple", "darkgoldenrod3", "deeppink", "cadetblue", 
            "darkred")
# die Zuordnung erfolgt durch den Index automatisch: 1 = rot, 2 = blau, ...


## Plot Erstellen ## 

# png("Aristotle.png", units="in", width = 10, height= 10 * 0.75, res=300)

par(mfrow = c(3, 4), mai = c(0.1, 0.1, 0.1, 0.1))

for(i in 1:12){ # erstellt fuer jede Loesung einen eigenen Plot
  l <- as.integer(unlist(strsplit(list[i], split = " ")))
  dat <- data.frame(x, y, z = l)
  dat <- dat[order(dat$z), ] # WICHTIG: Den Dataframe anhand der neuen Variable sortieren, 
  # so stellt man sicher, dass die Farben immer den gleichen Nummern zugeordnet werden, aber
  # unterschiedliche Koordinaten haben
  plot(dat$x, dat$y, pch = 19, cex = 6.2, ylim = c(0, 6), xlim = c(0, 6), col = colors, 
       ylab = "", xlab = "", yaxt = "n", xaxt = "n", bty = "n")
  text(dat$x, dat$y, labels=1:19, cex=1.9, col = "white")
}

# dev.off()