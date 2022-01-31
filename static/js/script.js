//Wait for the DOM to finish loading. //Get the button element and add event listeners.

document.addEventListener('DOMContentLoaded', function () {
	getPrompt(activities);
	addActivityButtonListener();
});

var newPrompt = ""

function getPrompt(activities) {
	newPrompt = activities[Math.floor(Math.random() * activities.length)];
	console.log(newPrompt);
	printPrompt()
}

function printPrompt() {
	let dailyPrompt = document.getElementById('activity');
	dailyPrompt.innerHTML = newPrompt;
}

function addActivityButtonListener() {
	let button = document.getElementById('btn--activity');
	button.addEventListener('click', function (event) {
		getPrompt(activities);
	})
}