
window.onload = function () {
  document
    .getElementById("chat-form")
    .addEventListener("submit", function (event) {
      // Prevent the form from submitting and refreshing the page
      event.preventDefault();

      let userInput = document.getElementById("user-input").value;
      let url = `http://localhost:8080/palm2?user_input=${encodeURIComponent(userInput)}`;


      fetch(url)
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then((data) => {
          let content = data.content;
          let resultDiv = document.getElementById("result");
          resultDiv.innerHTML = content;
        })
        .catch((error) => {
          console.error("Error fetching PaLM response:", error);
          let resultDiv = document.getElementById("result");
          resultDiv.innerHTML = "Error fetching response. Please try again.";
        });
    });
};
