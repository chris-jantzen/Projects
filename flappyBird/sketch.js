let bird;
let pipes = [];
let score = 0;
let started = false;
let gameover = false;
let key = 0;

function setup() {
    createCanvas(400, 600);
    bird = new Bird();
    // pipes.push(new Pipe());
}

function draw() {
    background(0);

    bird.show();

    for (let i = pipes.length - 1; i >= 0; i--) {
        pipes[i].show();
        if (!gameover)
            pipes[i].update();
        if (pipes[i].hits(bird) && !gameover) {
            console.log("ded");
            endGame();
        }

        if (pipes[i].through(bird)) {
            document.getElementById("score").innerHTML = "Score: " + ++score;
        }

        if (pipes[i].offscreen()) {
            pipes.splice(i, 1);
        }
    }

    if (started) {
        bird.update();
    }

    if (frameCount % 80 == 0) {
        pipes.push(new Pipe());
    }
}

function endGame() {
    for (let x of pipes) {
        x.speed = 0;
    }
    bird.velocity = 0;
    bird.gravity = 0;
    bird.lift = 0;
    gameover = true;
}

function reset() {
    gameover = false;
    for (let i = pipes.length - 1; i >= 0; i--) {
        pipes.splice(i, 1);
    }
    started = false;
    setup();
}

function keyPressed() {
    if (!gameover) {
        if (key == " ") {
            started = true;
            bird.up();
        }
    }
    if (keyCode === ENTER) {
        reset();
    }
}
