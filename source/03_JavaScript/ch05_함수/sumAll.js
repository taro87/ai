function sumAll(){
    let sumA = 0;
    if(arguments.length==1){
    sumA = arguments[0];
    }else if(arguments.length >= 2){
        for(let data in arguments){
        sumA += arguments[data];
        }
    }else{
    return -999;
    };
    return sumA;    
}