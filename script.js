const form = document.querySelector("form");
const chatBox = document.getElementById("chat-box");
const speakBtn = document.getElementById("speak-btn");

function appendMessage(sender, message, image = "") {
  const msgDiv = document.createElement("div");
  msgDiv.classList.add("msg");

  let content = `<strong>${sender}:</strong> ${message}`;
  if (image) {
    content += `<br><img src="${image}" class="bot-image" />`;
  }

  msgDiv.innerHTML = content;
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;

  if (sender === "KarunyaBot") {
    const utterance = new SpeechSynthesisUtterance(message);
    speechSynthesis.speak(utterance);
  }
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const userInput = document.getElementById("user-input").value;
  if (!userInput.trim()) return;
  appendMessage("You", userInput);
  document.getElementById("user-input").value = "";

  const response = await fetch("/get", {
    method: "POST",
    body: new URLSearchParams({ msg: userInput }),
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });

  const data = await response.json();
  appendMessage("KarunyaBot", data.text, data.image);
});

speakBtn.addEventListener("click", () => {
  const recognition = new webkitSpeechRecognition() || new SpeechRecognition();
  recognition.lang = "en-IN";
  recognition.start();

  recognition.onresult = function (event) {
    const transcript = event.results[0][0].transcript;
    document.getElementById("user-input").value = transcript;
  };
});