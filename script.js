const sampleTexts = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing is a fundamental skill that is useful in many jobs.",
    "Practice makes perfect, especially when it comes to typing.",
    "Python is a great language for building a variety of applications.",
    "Artificial Intelligence is changing the way we interact with technology.",
    "A journey of a thousand miles begins with a single step.",
    "Keep your face always toward the sunshine—and shadows will fall behind you.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Typing fast and accurately is a valuable skill in the digital world."
];

let startTime = null;
let selectedText = "";

function startTest() {
    document.getElementById("welcome").style.display = "none";
    document.getElementById("testArea").style.display = "block";

    selectedText = sampleTexts[Math.floor(Math.random() * sampleTexts.length)];
    document.getElementById("sampleText").innerText = selectedText;
    document.getElementById("typedText").value = "";
    document.getElementById("result").innerText = "";
    startTime = null;

    const textArea = document.getElementById("typedText");

    textArea.focus();

    // Reset Enter key listener
    textArea.removeEventListener("keydown", handleEnterKey);
    textArea.addEventListener("keydown", handleEnterKey);
}

function handleEnterKey(event) {
    if (event.key === "Enter") {
        event.preventDefault(); // Prevent newline
        calculateResults();
    } else if (!startTime) {
        startTime = new Date();
    }
}

function calculateResults() {
    const typedText = document.getElementById("typedText").value.trim();
    const endTime = new Date();
    const totalTime = (endTime - startTime) / 1000;
    const wordCount = typedText.split(/\s+/).length;
    const wpm = Math.round((wordCount / totalTime) * 60);

    let correctChars = 0;
    for (let i = 0; i < typedText.length; i++) {
        if (i < selectedText.length && typedText[i] === selectedText[i]) {
            correctChars++;
        }
    }

    const accuracy = Math.round((correctChars / selectedText.length) * 100);

    document.getElementById("result").innerText =
        `⏱ Time: ${totalTime.toFixed(2)}s | 📄 WPM: ${wpm} | ✅ Accuracy: ${accuracy}%`;

    document.getElementById("typedText").disabled = true;
}

function resetTest() {
    startTest();
}
