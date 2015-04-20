##slow version

##pollutantmean = function(directory, pollutant, id = 1:332){
##	files = list.files(directory,full.name=TRUE)
##    dat = data.frame()
##    
##    for(i in id)
##		dat = rbind(dat, read.csv(files[i]))
##    
##    mean(dat[[pollutant]],na.rm = TRUE)
##}

#efficient version
pollutantmean = function(directory, pollutant, id = 1:332){
    files = list.files(directory,full.name=TRUE)
    tmp = vector(mode = "list",length = length(id))
    
    tmp = lapply(files[id], read.csv)
    
    dat = do.call(rbind, tmp)
    
    mean(dat[[pollutant]],na.rm = TRUE)
}

## 'directory' is a character vector of length 1 indicating
## the location of the CSV files



## 'pollutant' is a character vector of length 1 indicating
## the name of the pollutant for which we will calculate the
## mean; either "sulfate" or "nitrate".

## 'id' is an integer vector indicating the monitor ID numbers
## to be used
  
## Return the mean of the pollutant across all monitors list
## in the 'id' vector (ignoring NA values)
