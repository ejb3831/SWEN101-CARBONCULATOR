/***********************************************

This is custom javascript for front end of quiz

Colby Scarbrough
Maisha Iqbal


**********************************************/

var answers = [0];
var currentAnswer;

console.log("script file");

//jquery loaded excecute following
$(document).ready(function(){
    console.log("jquery file");
    var questionNumber = 1;
    //hide questions
    $('.question-form').hide();
    
    //first one is displayed
    //grab form id
    $('#q1').show();
 
    $('#q1 #submit').click(function() {
        $('question-form').hide();
        $('#q2').fadeIn(300);
        return false;
        
    });
    questionNumber ++
    console.log(questionNumber)
    $('#q2 #submit').click(function() {
        $('question-form').hide();
        $('#q3').fadeIn(300);
        return false;
        
    });
    questionNumber ++
    $('#q3 #submit').click(function() {
        $('question-form').hide();
        $('#q4').fadeIn(300);
        return false;
        
    });
    questionNumber ++
    $('#q4 #submit').click(function() {
        $('question-form').hide();
        $('#q5').fadeIn(300);
        return false;
        
    });
    questionNumber ++
    $('#q5 #submit').click(function() {
        $('question-form').hide();
        $('#q5').fadeIn(300);
        return false;
        
    });
    
});