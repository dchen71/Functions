rankall <- function(outcome, num = "best") {
    ## Read outcome data
    outcomeData = read.csv("outcome-of-care-measures.csv", colClasses = 'character', na.strings = "Not Available")
    
    ## Splits the states
    state = split(outcomeData,outcomeData$State)
        
    ##11 heart attack,17 fail,23 pneumonia
    if(tolower(outcome == "pneumonia"))
        disease = 23
    else if (tolower(outcome) == "heart failure")
        disease = 17
    else if(tolower(outcome) == "heart attack")
        disease = 11
    else
        stop("invalid outcome")
    
    ## For each state, find the hospital of the given rank
    ## Return a data frame with the hospital names and the
    ## (abbreviated) state name
    #state[[val]][,col]
    answer = data.frame(matrix(ncol = 2, nrow = 54))
##need alphabetically order it
    
    if(num == "best"){
        num = 1
        for(i in 1:54){
            rankList = rbind(state[[i]])[order(as.numeric(state[[i]][,disease]), state[[i]][,2], na.last=TRUE),]
            rankList = subset(rankList,rankList[,disease] != "NA")
            answer[i,] = c(rankList[num,2],rankList[1,7])
        }
    }  
    else if(num == "worst"){
        
        for(i in 1:54){
            rankList = rbind(state[[i]])[order(as.numeric(state[[i]][,disease]), state[[i]][,2], na.last=TRUE),]
            rankList = subset(rankList,rankList[,disease] != "NA")        
            num = nrow(state[[i]])
            answer[i,] = c(rankList[num,2],rankList[1,7])
        }
        
    }
    else{
        for(i in 1:54){
            rankList = rbind(state[[i]])[order(as.numeric(state[[i]][,disease]), state[[i]][,2], na.last=TRUE),]
            rankList = subset(rankList,rankList[,disease] != "NA")
            answer[i,] = c(rankList[num,2],rankList[1,7])
        }
    }
    
    names(answer) = c("hospital", 'state')
    
    return(answer)
}
