function caller(name, subject, message, email) {
	document.getElementById('inputForm').addEventListener('submit', prevDef())
	if (!name || !subject || !message || !email) {
		document.getElementById('errorMsg').hidden = false;
	} else {
		alert("Hi " + name +  ", your message has been sent")
	}
}

function prevDef() {
	event.preventDefault();
}