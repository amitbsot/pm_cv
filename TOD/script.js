const truthList = [
  "What's the most embarrassing thing you've ever done?",
  "Have you ever lied to your best friend, and about what?",
  "What's your biggest fear?",
  "What's the craziest thing you've ever done?",
  "Have you ever thought about being intimate with your sex?",
  "Have you tried to make out with the same sex",
  "Finish the sentence; a perfect spouse is one who ___?",
  "What is your most cherished childhood memory?",
  "What was the worst phase of your life?",
  "If you could get rid of one law, what would it be?",
  "When during your life have you felt the most alive?",
  "What is the most humiliating thing to have happened to you?",
  "Describe your dream home.",
  "What would it be if you had only one movie to watch for the rest of your life?",
  "Do you prefer your partner to make you breakfast, lunch, or dinner?",
  "If you could pick a friend to switch lives with, who would you pick, and why?",
  "If you were to have children would you prefer all girls or all boys?",
  "Could you live in a tiny house or an RV for a year?",
  "What is the oddest food combination you have ever eaten or would like to try?",
  "What would be something you would do if you were elected president?", 
  ];

const dareList = [
  "Sing a song in public",
  "Do a handstand for 10 seconds",
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


