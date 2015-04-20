rankhospital <- function(state, outcome, num = "best") {
    ## Read outcome data
    outcomeData = read.csv("outcome-of-care-measures.csv", colClasses = 'character', na.strings = "Not Available")
    
    ## Check that state and outcome are valid
    
    ##subset to state
    state = subset(outcomeData,outcomeData[,7] == state)
    
    if(nrow(state) == 0){
        stop("invalid state")
    }
    
    ##11 heart attack,17 fail,23 pneumonia
    if(tolower(outcome == "pneumonia"))
        disease = 23
    else if (tolower(outcome) == "heart failure")
        disease = 17
    else if(tolower(outcome) == "heart attack")
        disease = 11
    else
        stop("invalid outcome")
    
    ## Return hospital name in that state with the given rank
    ## 30-day death rate
    
    sorted = order(as.numeric(state[,disease], na.last= TRUE))
    answer = rbind(state)[sorted,]
    answer = subset(answer,answer[,disease] != "NA")
    
    if(num == "best"){
        return(answer[1,2])
    }  
    else if(num == "worst"){
        return(answer[nrow(answer),2])
    }  
    else if(num >nrow(answer)){
        return(NA)
    }
    else{
        return(answer[num,2])
    }

}
