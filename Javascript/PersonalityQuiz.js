/*Add your JavaScript here*/
heroScore = 0;
magicScore = 0;

var questionCount = 0;


var result = document.getElementById("result");

var restart = document.getElementById("restart");

var q1a1 = document.getElementById("q1a1");
var q1a2 = document.getElementById("q1a2");

var q2a1 = document.getElementById("q2a1");
var q2a2 = document.getElementById("q2a2");

var q3a1 = document.getElementById("q3a1");
var q3a2 = document.getElementById("q3a2");


//Button Clicks
restart.addEventListener("click", restartQuiz);


q1a1.addEventListener("click", magic);
q1a2.addEventListener("click", hero);

q2a1.addEventListener("click", magic);
q2a2.addEventListener("click", hero);

q3a1.addEventListener("click", magic);
q3a2.addEventListener("click", hero);

function magic() {
  magicScore +=1;
  questionCount += 1;

  console.log("Question Count = " + questionCount + " magicScore = " + magicScore);

  if(questionCount == 3) {
  console.log("Your quiz is done!");
  updateResult();
}

}

function hero() {
  heroScore += 1;
  questionCount += 1;

  console.log("Question Count = " + questionCount + " heroScore = " + heroScore);

  if(questionCount == 3) {
  console.log("Your quiz is done!");
  updateResult();  
}
} 

function updateResult() {
   if (heroScore >= 2) {
      console.log("You are a Heroic Adventurer!");
      result.innerHTML =  "You are a Heroic Adventurer";
    }
    else {
    console.log("You are a mystical adventurer!");
    result.innerHTML = "You are a mystical adventurer!";
}
}

function restartQuiz() {
      result.innerHTML = "Your result is..."

     heroScore = 0;
     magicScore = 0;
    questionCount = 0;
}
