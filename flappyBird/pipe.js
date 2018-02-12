function Pipe() {
    this.top = random(40, height - 200);
    let gap = 125;
    this.bottom = height - (gap + this.top);
    this.x = width;
    this.w = 20;
    this.speed = 2;

    this.highlight = false;

    this.hits = function(bird) {
        if (bird.y - 16 < this.top || bird.y + 16 > height - this.bottom) {
            if (bird.x > this.x && bird.x < this.x + this.w) {
                this.highlight = true;
                return true;
            }
        }
        this.highlight = false;
        return false;
    }

    this.show = function() {
        fill(0, 204, 0);
        if (this.highlight) {
            fill(255, 0, 0);
        }
        rect(this.x, 0, this.w, this.top);
        rect(this.x, this.top + gap, this.w, this.bottom);
    }

    this.through = function(bird) {
        return bird.x - bird.birdWidth === this.x;
    }

    this.update = function() {
        this.x -= this.speed;
    }

    this.offscreen = function() {
        return this.x < -this.w;
    }
}
