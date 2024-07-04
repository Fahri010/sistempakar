const fuzzy = require("fuzzylogic");

// Definisikan membership function untuk input gejala
const membershipFunctions = {
  jarang: (value) => fuzzy.triangle(value, 0, 20, 40),
  kadang: (value) => fuzzy.triangle(value, 20, 40, 60),
  sering: (value) => fuzzy.triangle(value, 40, 60, 80),
  sangatSering: (value) => fuzzy.triangle(value, 60, 80, 100),
};

// Definisikan input gejala dengan contoh nilai
const inputGejala = {
  C01: 100, //1
  C02: 0,
  C03: 0,
  C04: 100, //2
  C05: 0,
  C06: 0,
  C07: 60, //3
  C08: 0,
  C09: 0,
  C10: 0, //4
  C11: 100,
  C12: 0,
  C13: 100, //5
  C14: 0,
  C15: 0,
  C16: 0, //6
  C17: 100,
  C18: 0,
  C19: 70, //7
  C20: 25,
  C21: 50,
  C22: 30, //8
  C23: 40,
  C24: 60,
  C25: 80, //9
  C26: 30,
  C27: 50,
  C28: 90, //10
  C29: 30,
  C30: 60,
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

// Hitung gaya belajar berdasarkan input gejala dan aturan fuzzy
const learningStyle = determineLearningStyle(inputGejala, rules);

console.log(`Visual: ${learningStyle.visual}`);
console.log(`Auditori: ${learningStyle.auditori}`);
console.log(`Kinestetik: ${learningStyle.kinestetik}`);
