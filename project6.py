<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Jack's Typing Adventure</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      background: #f0f8ff;
    }
    h1 {
      color: #333;
    }
    #quote {
      font-size: 1.2em;
      margin-bottom: 20px;
      background: #eef;
      padding: 15px;
      border-radius: 8px;
    }
    textarea {
      width: 100%;
      height: 100px;
      font-size: 1em;
      padding: 10px;
      border: 2px solid #ccc;
      border-radius: 5px;
    }
    button {
      margin-top: 15px;
      padding: 10px 20px;
      font-size: 1em;
      cursor: pointer;
    }
    #results {
      margin-top: 20px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>Jack's Typing Adventure</h1>
  <div id="quote">"The quick brown fox jumps over the lazy dog."</div>
  <textarea id="typed-text" placeholder="Start typing here..."></textarea>
  <br />
  <button onclick="calculateResults()">Finish</button>
  <div id="results"></div>

  <script>
    const quote = document.getElementById("quote").innerText;
    let startTime;

    const textarea = document.getElementById("typed-text");
    textarea.addEventListener("focus", () => {
      if (!startTime) {
        startTime = new Date();
      }
    });

    function calculateResults() {
      const typedText = textarea.value;
      const endTime = new Date();
      const timeTakenInSeconds = (endTime - startTime) / 1000;

      const quoteWords = quote.trim().split(/\s+/);
      const typedWords = typedText.trim().split(/\s+/);
      let correctWords = 0;

      for (let i = 0; i < quoteWords.length; i++) {
        if (quoteWords[i] === typedWords[i]) {
          correctWords++;
        }
      }

      const accuracy = (correctWords / quoteWords.length) * 100;
      const wpm = (typedWords.length / timeTakenInSeconds) * 60;

      document.getElementById("results").innerHTML = `
        ⏱️ Time: ${timeTakenInSeconds.toFixed(2)} seconds<br>
        🧠 Accuracy: ${accuracy.toFixed(2)}%<br>
        🚀 Speed: ${wpm.toFixed(2)} WPM
      `;
    }
  </script>
</body>
</html>
