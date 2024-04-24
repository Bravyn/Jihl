
let state  = {};//game state


newGame();

function newGame() {
    //game state init
    state = {
        phase : "aiming", //can either be aiming, in flight or celebrating
        currentPlayer: 1,
        bomb: {
            x : undefined,
            y: undefined,
            velocity: {x : 0, y : 0},
        },
        buildings: generateBuildings(),
        // ...
    };

    initializeBombPosition();
    draw()
}


const canvas  = document.getElementById("game");
canvas.width  = window.innerWidth;
canvas.height = window.innerHeight;
const ctx = canvas.getContext("2d");

ctx.fillStyle = "blue";

ctx.fillRect(200, 200, 440, 320)



function draw(){
    //  ...

}

//Event handlers
// ...


function animate(timestamp) {
    // ..
}


function generateBuildings(){
    // ...
}

function initializeBombPosition(){
    // ....
}