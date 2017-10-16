function caller(name, subject, message) {
	document.getElementById('inputForm').addEventListener('submit', prevDef())
	if (!name || !subject || !message) {
		document.getElementById('errorMsg').hidden = false;
	} else {
		alert("Hi " + name +  ", your message has been sent")
	}
}

function prevDef() {
	event.preventDefault();
}