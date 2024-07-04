const fuzzy = require("fuzzylogic");

// Definisikan membership function untuk input gejala
const membershipFunctions = {
  jarang: (value) => fuzzy.triangle(value, 0, 20, 40),
  kadang: (value) => fuzzy.triangle(value, 20, 40, 60),
  sering: (value) => fuzzy.triangle(value, 40, 60, 80),
  sangatSering: (value) => fuzzy.triangle(value, 60, 80, 100),
};

// Definisikan membership function untuk output gaya belajar
const learningStyles = {
  lemah: (value) => fuzzy.triangle(value, 0, 20, 40),
  sedang: (value) => fuzzy.triangle(value, 20, 40, 60),
  kuat: (value) => fuzzy.triangle(value, 60, 80, 100),
};

// Definisikan input gejala (contoh nilai)
const inputGejala = {
  C01: 75, // Updated based on the example scenario
  C02: null,
  C03: null,
  C04: null,
  C05: 60,
  C06: null,
  C07: 75,
  C08: null,
  C09: null,
  C10: null,
  C11: 50,
  C12: null,
  C13: 85,
  C14: null,
  C15: null,
  C16: 80,
  C17: null,
  C18: null,
  C19: 70,
  C20: null,
  C21: null,
  C22: null,
  C23: null,
  C24: 60,
  C25: null,
  C26: null,
  C27: 50,
  C28: 90,
  C29: null,
  C30: null,
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

// Bagian ini belum menjalankan perhitungan dan belum menghasilkan output
// Anda bisa menambahkan kode berikut untuk menjalankan perhitungan dan mendapatkan hasil

const learningStyle = determineLearningStyle(inputGejala, rules);

console.log(`Visual: ${learningStyle.visual}`);
console.log(`Auditori: ${learningStyle.auditori}`);
console.log(`Kinestetik: ${learningStyle.kinestetik}`);
