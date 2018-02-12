function Bird() {
    this.y = height / 2;
    this.x = 64;

    this.birdHeight = 32;
    this.birdWidth = 32;

    this.gravity = .6;
    this.lift = -15;
    this.velocity = 0;

    this.up = function() {
        this.velocity += this.lift;
    }

    this.show = function() {
        fill(255);
        ellipse(this.x, this.y, this.birdHeight, this.birdWidth);
    }

    this.update = function() {
        this.velocity += this.gravity;
        this.velocity *= 0.9;
        this.y += this.velocity;

        if (this.y > height) {
            this.y = height;
            this.velocity = 0;
        } else if (this.y < 0) {
            this.y = 0;
            this.velocity = 0;
        }
    }
}
