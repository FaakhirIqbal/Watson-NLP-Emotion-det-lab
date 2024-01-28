// Function to run sentiment analysis on the input text
function runSentimentAnalysis() {
    // Retrieve the text entered by the user
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    // Create a new XMLHttpRequest object
    const xhttp = new XMLHttpRequest();

    // Define what happens on state change of the request
    xhttp.onreadystatechange = function() {
        // Check if the request is complete and was successful
        if (this.readyState === 4 && this.status === 200) {
            // Update the system response on the web page
            document.getElementById("system_response").innerHTML = this.responseText;
        }
    };

    // Initialize a GET request with the input text as a query parameter
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);

    // Send the request to the server
    xhttp.send();
}
