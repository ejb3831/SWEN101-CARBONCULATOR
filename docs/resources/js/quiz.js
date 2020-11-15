 /****************************************************************
    
    Javascript for quiz page
    no use of jquery as returning values is easier with javascript
    Colby Scarbrough
    Maisha Iqbal
    group 6
    
******************************************************************/
/* define variables for document */

var doc, submit, answers, questions;
doc = document
submit = doc.getElementById("submit-btn")
answers = [];
questions = 9;

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
    console.log(answers);
    //send list to maisha python program
    function quiz(answers) {
        var results = [];
        var points = 0;
        
        points += (16 - answers[0] * 2);
        
        points += (13 - answers[1] * 2);
        
        points += (12 - answers[2] * 2);
        
        if (answers[2] < 2) {
            results.push("You can help by eating less meat.  https://www.greenpeace.org/usa/sustainable-agriculture/eco-farming/eat-more-plants/")
        }
        
        points += (answers[3] - 1);
        if (answers[3] > 2) {
            results.push("'You can help by using less water. https://www.epa.gov/watersense/how-we-use-water")
        }
        
        points += (answers[4] - 1);
        if (answers[4] > 2) {
            results.push("You can help by using less water.  https://www.epa.gov/watersense/how-we-use-water")
        }
        
        points += (12 - answers[5] * 2);
        
        if (answers[6] == 1) {
            points += 5
        } else {
            points += (answers[6] * 10)
        }
        
        if (answers[6] > 2) {
            results.push("You can help by producing less waste.  https://www.earthday.org/how-our-trash-impacts-the-environment/")
        }
        
        points += (24 - (answers[7] - 1) * 4)
        if(answers[7] < 4) {
            results.push("You can help by recycling more https://www.epa.gov/recycle/recycling-basics")
        }
        
        if (answers[8] != 5) {
            points += (14 - answers[8] * 2);
        }
        if (answers[8] <= 2) {
            results.push("You can help by taking public transportation and carpooling. https://www.greenamerica.org/green-living/carpool-climate-and-community")
        }
        
        return results
        
        
    }
    
    var suggestions = quiz(answers);
    console.log(suggestions)
    //add a results section to the test page 
        
    for (i = 0; i < suggestions.length - 1; i++) {
        var p = doc.createElement("p");
        p.innerText = suggestions[i];
        doc.getElementById("results-text").appendChild(p);
    }
    
    doc.getElementById("test-form").style.display = "none";
    doc.getElementById("test-title").style.display = "none";
    doc.getElementById("results").style.display = "block";

    
}

/* submit button clicked do the following */
submit.addEventListener("click", returnResults);

