/**
 * Returns Sentiment of a Given text.
 *
 * @param {string} input - text.
 * @return String describing sentiment.
 * @customfunction
 */
function GETSENTIMENT(text) {

  var url = "https://pc-sentiment-analyzer.herokuapp.com/get-sentiment"

  // Make a POST request with a JSON payload.
  var data = {
    "text":text
  };
  var options = {
    'method' : 'post',
    'contentType': 'application/json',
    // Convert the JavaScript object to a JSON string.
    'payload' : JSON.stringify(data)
  };
  var sentiment  = JSON.parse(UrlFetchApp.fetch(url, options).getContentText());

  return sentiment
}