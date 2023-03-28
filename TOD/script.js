const truthList = [
  "What's the most embarrassing thing you've ever done?",
  "Have you ever lied to your best friend?",
  "What's your biggest fear?",
  "What's the craziest thing you've ever done?",
];

const dareList = [
  "Sing a song in public",
  "Do a handstand for 10 seconds",
  "Tell a joke in a silly voice",
  "Eat a spoonful of hot sauce",
];

const truthButton = document.getElementById("truth-button");
const dareButton = document.getElementById("dare-button");
const questionOutput = document.getElementById("question-output");

truthButton.addEventListener("click", () => {
  const randomTruth = truthList[Math.floor(Math.random() * truthList.length)];
  questionOutput.textContent = randomTruth;
});

dareButton.addEventListener("click", () => {
  const randomDare = dareList[Math.floor(Math.random() * dareList.length)];
  questionOutput.textContent = randomDare;
});


