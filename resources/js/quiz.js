 /****************************************************************
    
    Javascript for quiz page
    no use of jquery as returning values is easier with javascript
    Colby Scarbrough
    group 6
    
******************************************************************/
/* define variables for document */

var doc, submit, answers, questions;
doc = document
submit = doc.getElementById("submit-btn")
answers = [];
questions = 8;

console.log("script file");
console.log(doc.location);
console.log(submit)

/* make list for all answers input */

function returnResults() {
    //add answers to list
    var radios
    for(i = 0; i < questions; i++) {
        radios = doc.getElementsByName("q" + i)
        for (j = 0; j < radios.length; j++) {
            if (radios[j].checked) {
                answers.push(radios[j].value)
            }
        }
    }
    console.log(answers)
    //send list to maisha python program
    
    
    //add a results section to the test page
    doc.getElementById("test-form").style.display = "none";
    doc.getElementById("test-title").style.display = "none";
    doc.getElementById("results").style.display = "block";
    
}

/* submit button clicked do the following */
submit.addEventListener("click", returnResults);