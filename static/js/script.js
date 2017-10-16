function caller(name, subject, message) {
	document.getElementById('inputForm').addEventListener('submit', prevDef())

	if (!name || !subject || !message) {
		document.getElementById('errorMsg').hidden = false;
	}
}

function prevDef() {
	event.preventDefault();
}