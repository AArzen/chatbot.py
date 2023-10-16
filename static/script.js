/**
 * Funkcija, ki sešteje dve števili.
 * @param {number} a - Prvo število.
 * @param {number} b - Drugo število.
 * @returns {number} - Vsota dveh števil.
 */
 // komentar
//function sestej(a, b) {
//    return a + b;
//}
//
//add(2,2)


/**
 * Izračuna povprečno vrednost treh števil.
 *
 * @param {number} a - Prvo število.
 * @param {number} b - Drugo število.
 * @param {number} c - Tretje število.
 * @returns {number} - Povprečna vrednost treh števil.
 *
 * @example
 * // Primer uporabe:
 * let rezultat = funkcija5(10, 20, 30);
 * console.log("Povprečna vrednost je:", rezultat);
 */
//function funkcija5(a, b, c) {
//    // Izračunaj vsoto treh števil
//    let vsota = a + b + c;
//
//    // Izračunaj povprečje
//    let povprecje = vsota / 3;
//
//    return povprecje;
//}

const chatLog = document.getElementById("chat-log");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");

sendButton.addEventListener("click", sendMessage);

function sendMessage() {
    const userMessage = userInput.value;
    if (userMessage === "") return;

    appendMessage("You", userMessage);

    fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `user_message=${encodeURIComponent(userMessage)}`
    })
    .then(response => response.json())
    .then(data => {
        const botResponse = data.response;
        appendMessage("ChatBot", botResponse);
    });

    userInput.value = "";
}

function appendMessage(sender, message) {
    const messageElement = document.createElement("div");
    messageElement.textContent = sender + ": " + message;
    chatLog.appendChild(messageElement);
}
