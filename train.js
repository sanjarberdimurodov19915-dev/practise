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
/* 
B-TASK (Nodejs)

Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.

MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/
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