

const choices = ["មាន់", "ឃ្លោក", "ខ្លា", "ត្រី", "ក្ដាម", "បង្កង"];
const result = document.getElementById("result");
function game(){
    const randomGames = [];
    while (randomGames.length < 3) {
        const randomIndex = Math.floor(Math.random() * choices.length);
        const randomElement = choices[randomIndex];
        if (!randomGames.includes(randomElement)) {
            randomGames.push(randomElement);
        }
    }
    result.textContent=randomGames


}
