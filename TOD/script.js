const truthList = [
  "What's the most embarrassing thing you've ever done?",
  "Have you ever lied to your best friend, and about what?",
  "What's your biggest fear?",
  "What's the craziest thing you've ever done?",
  "Have you ever thought about being intimate with your sex?",
  "Have you tried to make out with the same sex",
  
];

const dareList = [
  "Sing a song in public",
  "Do a handstand for 10 seconds",
  "Tell a joke in wear something that your partner wants ones a silly voice",
  "Eat something sweet from your partner's privets",
  "Wear something that your partner Wants",
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


