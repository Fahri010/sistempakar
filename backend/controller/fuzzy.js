const fuzzy = require("fuzzylogic");

// Definisikan membership function untuk input gejala
const membershipFunctions = {
  jarang: (value) => fuzzy.triangle(value, 0, 20, 40),
  kadang: (value) => fuzzy.triangle(value, 20, 40, 60),
  sering: (value) => fuzzy.triangle(value, 40, 60, 80),
  sangatSering: (value) => fuzzy.triangle(value, 60, 80, 100),
};

// Definisikan aturan fuzzy
const rules = [
  {
    gejala: [
      "C01",
      "C04",
      "C07",
      "C10",
      "C13",
      "C16",
      "C19",
      "C22",
      "C25",
      "C28",
    ],
    output: "visual",
  },
  {
    gejala: [
      "C02",
      "C05",
      "C08",
      "C11",
      "C14",
      "C17",
      "C20",
      "C23",
      "C26",
      "C29",
    ],
    output: "auditori",
  },
  {
    gejala: [
      "C03",
      "C06",
      "C09",
      "C12",
      "C15",
      "C18",
      "C21",
      "C24",
      "C27",
      "C30",
    ],
    output: "kinestetik",
  },
];

// Fungsi untuk menghitung derajat keanggotaan
const calculateMembership = (value) => {
  if (value === null || value === undefined) {
    return { jarang: 0, kadang: 0, sering: 0, sangatSering: 0 };
  }
  return {
    jarang: membershipFunctions.jarang(value),
    kadang: membershipFunctions.kadang(value),
    sering: membershipFunctions.sering(value),
    sangatSering: membershipFunctions.sangatSering(value),
  };
};

// Fungsi untuk menentukan gaya belajar
const determineLearningStyle = (inputGejala, rules) => {
  const output = {
    visual: 0,
    auditori: 0,
    kinestetik: 0,
  };

  rules.forEach((rule) => {
    let minMembership = 1;

    rule.gejala.forEach((gejala) => {
      const membership = calculateMembership(inputGejala[gejala]);
      const maxMembership = Math.max(
        membership.jarang,
        membership.kadang,
        membership.sering,
        membership.sangatSering
      );
      minMembership = Math.min(minMembership, maxMembership);
    });

    output[rule.output] = Math.max(output[rule.output], minMembership);
  });

  return output;
};

// Fungsi untuk menerima input dari user
const getUserInput = () => {
  const inputGejala = {};
  const readline = require("readline");
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const questions = [
    "C01: ",
    "C02: ",
    "C03: ",
    "C04: ",
    "C05: ",
    "C06: ",
    "C07: ",
    "C08: ",
    "C09: ",
    "C10: ",
    "C11: ",
    "C12: ",
    "C13: ",
    "C14: ",
    "C15: ",
    "C16: ",
    "C17: ",
    "C18: ",
    "C19: ",
    "C20: ",
    "C21: ",
    "C22: ",
    "C23: ",
    "C24: ",
    "C25: ",
    "C26: ",
    "C27: ",
    "C28: ",
    "C29: ",
    "C30: ",
  ];

  const askQuestion = (index) => {
    if (index === questions.length) {
      rl.close();
      const learningStyle = determineLearningStyle(inputGejala, rules);
      printResult(learningStyle);
      return;
    }

    rl.question(questions[index], (answer) => {
      inputGejala["C" + (index + 1)] = parseFloat(answer);
      askQuestion(index + 1);
    });
  };

  askQuestion(0);
};

// Fungsi untuk mencetak hasil
const printResult = (learningStyle) => {
  console.log(`Visual: ${learningStyle.visual}`);
  console.log(`Auditori: ${learningStyle.auditori}`);
  console.log(`Kinestetik: ${learningStyle.kinestetik}`);
};

// Panggil fungsi untuk menerima input dari user
getUserInput();
