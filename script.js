document.addEventListener('DOMContentLoaded', function () {
	getPrompt(activities);
});

var newPrompt =""

function getPrompt(activities) {
    console.log("Function Working");
    newPrompt = activities[Math.floor(Math.random() * activities.length)];
    console.log(newPrompt);
    printPrompt()
}

function printPrompt() {
    let dailyPrompt = document.getElementById('activity');
    dailyPrompt.innerHTML = newPrompt;
}
