function newUser(){
    var userName = prompt("Please enter a username");
    var passWord = prompt("Please enter a password. Must contain a number, symbol, capital letter and be at least 8 characters");
    var pass2 = prompt("please re-enter your password");
    capTest = Array.from({length:10},(v,k)=>k+1);
    numTest = Array.from({length:24},(v,k)=>k+1);
    symTest = Array.from({length:15},(v,k)=>k+52+1);
    test = {capTest, numTest, symTest};
    key = "bT5h&ZVUgQBzrxj9NCD#w@kZ#6+Xz-Cd^+Df#@vV2H75W9jp2CcDJzkvR!&aFZ%M?LlVV3-cxKX4b&5mP|=bzaTHJrKer?qH!fpTL-FMi?9luapw|VYCu#al947=sbS0EFR3-yh92dV3Z%pS^@xm@E81k9=Zc&YPx6s!?z8_%tZ+Qb3O!uA%n8+DUJ+e%Y+?+LQ^Y7_tDB^7gc&bRXW8d0oeKH4CIAVeQA|J9Zzue3cP=MZCjrl_V^7JtBTdE|1m";
    var fin = DBFunctions.readFile(key);
    if(passWord !=pass2 ){
        alert("Passwords do not match");
        return;
    }else if(!contSec(passWord, test)){
        alert("Password does not reach requirements");
        return;
    }else if(fin.includes(userName)){
        alert("Acount already exists");
        return;
    }else{   
        fin[userName]=passWord;  
        DBFunctions.writeFile(fin);
        return;
    }
    
}
function contSec(input, compareLst){
    for(x in compareLst){
        if(!input.some(cont(x))){
            return false;
        }
    }
    return(true);
}
function cont(input, c){
    if(input.includes(String.fromCharCode(c))){
        return true;
    }else{
        return false;
    }
}