1. What is the function of the following technologies in your assignment:
HTML - used to create the text to be displayed on a page as well as formatting it.
CSS - used to modify the text displayed on a page with style attributes such as color of text. 
JavaScript - used to dynamically update the contents of the page/DOM instead of having a static page.
Python - used to run the backend of the website upon which Flask was also used.
Flask - a microframework that features templating to make it easier to display certain html docs on certain pages as well as make routing much more easier and intuitive. 
HTTP - the protocol that is used so that we can transfer hypertext such as HTML documents that are used as templates.
GET and POST requests - used POST requests to POST the contents of the form and make another request to MAILGUN so that I could send out an email with the contents of the form.

2. How does HTML, CSS, and JavaScript work together in the browser for this assignment?

HTML provides the raw text (hypertext) on a webpage, the CSS provides the styling of the text so that we can make it look nice/aesthetic, and JavaScript allows us to make our pages dynamic so that they can change based on user input or other external changes.

3. How does Python and Flask work together in the server for this assignment?

Flask is a very simple web framework that functions as a library we import when we run our python webserver. It handles everything from routing, to rendering templates, to handling requests from the app. For example flask handles the requests back to python so that we can handle them with python logic.

4. List all of the possible GET and POST requests that your server returns a response for and describes what happens for each GET and POST request.

GET requests - GET home page (index), GET about us page, GET contact us page, GET each blog page

POST requests - submitting the form

