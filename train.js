/*
MITASK-E

Savol: Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh"
*/
// Masalaning yechimi:
// function getReverse(word) {
//     let newWord = "";
//     for (let i = word.length - 1; i >= 0; i--) {
//         newWord += word[i];
//     }
//     return newWord;
// }
// const word = "hello"
// const result = getReverse(word);
// console.log(result)

// function getReverse(name) {
//     let b = ""
//     for (x of name) {
//         b = x + b
//     }
//     return b
// }
// console.log(getReverse("Kelly"))

/*
MITASK-D

Savol: Shunday function tuzingki unga integerlardan iborat array pass bolsin va
function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.

// Masalaning yechimi:
function getHighestIndex(array1) {
    let max = 0;
    for (let i = 0; i < array1.length; i++) {
        if (array1[i] > array1[max]) {
            max = i;
        }
    }
    return max;
}

const result = [5, 21, 12, 21, 8];
console.log(getHighestIndex(result));
*/

/*
MITASK-C

Savol: Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;

// Masalaning yechimi:
function checkContent(word1, word2) {
    if (word1.length !== word2.length) {
        return false;
    }
    let sorted1 = word1.split('').sort().join('');
    let sorted2 = word2.split('').sort().join('');
    return sorted1 === sorted2;
}

console.log(checkContent('sanjar', 'ranjas'));
*/

/*
MITASK-B

Savol: Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.

MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.

// Masalaning yechimi:

function countDigits(text) {
    let count = 0;
    for (let i = 0; i < text.length; i++) {
        if (text[i] >= '0' && text[i] <= "9") {
            count++;
        }
    }
    return count;
}

const result = countDigits("oohfks743bh4thtb5hb5t5h4brrjej2");
console.log(result);
*/

/* MITASK-A

Savol: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/
// Masalaning yechimi:
/*
function countLetter(letter, word) {
    let count = 0;

    for (let i = 0; i < word.length; i++) {
        if (word[i] === letter) {
            count++;
        }
    }

    return count;
}

console.log(countLetter("i", "intercontinental"));
console.log(countLetter("s", "samarqand"));
*/

