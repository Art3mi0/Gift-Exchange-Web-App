// Test function for changing text
function testFunction() {
    document.getElementById("testText").innerHTML = "NANI";
}


let rrTable = [0, 0, 1, 0, 0, 0];
let count = 0;
/*
Test function for changing button properties.
Cares about two buttons. The left and right button.
Both buttons, when calling it, give them their id in order for this function to be reusable.
Pressing one button will disable and change the color of itself, and enable and change the color 
    of the other back to its default.
*/
function testFunction2(id) {
    const lButton = document.getElementById("btn_left");
    const rButton = document.getElementById("btn_right");
    const disColor = "rgb(245, 149, 149)";
    let defColor = lButton.style.backgroundColor;

    if (lButton.id == id){
        if (rrTable[count] == 1){
            document.getElementById("p1Text").style.color="red";
            document.getElementById("rrOutput").innerText="P1 DEAD";
        } else{
            document.getElementById("rrOutput").innerText="P1 safe... NEXT";
        }
        rButton.disabled = false;
        rButton.style.backgroundColor = lButton.style.backgroundColor;
        lButton.disabled = true;
        lButton.style.backgroundColor = disColor;
    } else{
        if (rrTable[count] == 1){
            document.getElementById("p2Text").style.color="red";
            document.getElementById("rrOutput").innerText="P2 DEAD";
        } else{
            document.getElementById("rrOutput").innerText="P2 safe... NEXT";
        }
        lButton.disabled = false;
        lButton.style.backgroundColor = rButton.style.backgroundColor;
        rButton.disabled = true;
        rButton.style.backgroundColor = disColor;
    }
    count = count + 1;
    //button.style.backgroundColor ="rgb(0,255,0)";
    document.getElementById(this.id).value = "???";
}

function resetFunction(){
    shuffleArray(rrTable);
    document.getElementById("p1Text").style.color="black";
    document.getElementById("p2Text").style.color="black";
    document.getElementById("rrOutput").innerText="Press button to start";
    count = 0;
    document.getElementById("btn_left").disabled=false;
    document.getElementById("btn_right").disabled=false;
    document.getElementById("btn_right").style.backgroundColor="white";
    document.getElementById("btn_left").style.backgroundColor="white";
}

/* Randomize array in-place using Durstenfeld shuffle algorithm */
function shuffleArray(array) {
    for (var i = array.length - 1; i >= 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

/*
TODO:
    -Database for users.
        *Upon entering casino page, we can see a list of users
        *Need to be able to add, delete, and chooses a user
        *Database should have: 
            -id (primary key, int, auto increment)
            -name (string, just first name)
            -money (int, auto set to 500 or whatever, should be able to go negative)
    -Roulette
        *For practice:
            -Have button and text above it
            -Have text input and slider next to it
            -Slider determines if red or black
            -On button press, random number and color picked
            -If number and color match enterd value and slider, user gains money, else, user loses money
            -Amount of money gained/lost static
            -because practice, have number range small like 1-10
        *For advanced:
            -Able to choose multiple numbers and color for 1 bet
                *could have system like with users
            -Maybe improve method for displaying/showing winning number
        *For beyond advanced:
            -Make entire roulette table
            -Make rng number thing display an animation of the number being selected
    
    -Russian Roulette
        *A list composed of 0 or 1. 0 indicates safe, 1 indicates blasted
        *Option for barrel size, and number of bullets
        *Design for two players
            -Just incorporate the two button example done.
            -Left is player, right is "the house"
        *If player won and in debt, reset money to starting amount,
            if won and not in debt, add starting amount of money to current player money
            if lost, delete player from db
    
    -Side Ideas
        *House money
            -All lost user money should be added to house money and displayed to users
            -default is starting user money
            -When someone wins, house money is subtracted
            -When playing russian roulette, users win entire house money if house not negative
            -When house is negative, users have a chance to be forced to play russian roulette when they try playing a different game
                *Have games be individual links
                *As long as house is not negative, when playing not russian roullete, users stay on page, else, they get returned to casino home
                *Now, when users try going to game, they can instead go to russian roullete. 
*/