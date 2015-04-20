complete <- function(directory, id = 1:332) {    
    files = list.files(directory,full.name=TRUE)
    tmp = vector(mode = "list",length = length(id))
    
    ans = data.frame(matrix(data = c(integer(), integer()), nrow=length(id), ncol = 2))
    names(ans) = c("ID", "nobs")
        
    for(i in 1:length(id)){
        dat = read.csv(files[id[i]])
        ans[i,] = data.frame(id[i],sum(complete.cases(dat))) 
    }
    
    return(ans)
}