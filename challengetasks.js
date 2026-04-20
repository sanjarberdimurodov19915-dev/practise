// ANIMAL CHALLENGE
const animals = ["fox", "horse", "ant", "bird", "lion", "wolf", "deer", "bear", "frog", "hen", "mole", "duck", "goat", "dog", "cat", "bat", "cock", "cow"];

function findAnimals(animals, letter) {
    const searchLetter = letter.toLowerCase();
    return animals.filter(name => searchLetter.includes(name[0].toLowerCase()));
}


const result = findAnimals(animals, 'aw');
console.log(result);