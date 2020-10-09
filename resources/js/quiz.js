 /****************************************
    
    Javascript for quiz page
    Colby Scarbrough
    group 6
    
****************************************/
/* define variables for document */

var doc, submit, answers;
doc = document
submit = doc.getElementById("submit-btn")
answers = [];

console.log("script file");
console.log(doc.location);
console.log(submit)

/* make lists for all answers input */

function returnResults() {
    //wait for maisha give what she wants for answers
}


submit.addEventListener("click", returnResults);