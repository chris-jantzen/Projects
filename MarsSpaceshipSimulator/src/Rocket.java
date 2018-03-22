import java.util.Random;

public class Rocket implements SpaceShip {

    public int currentWeight;
    public int maxWeight;

    public Rocket() {
    }

    public Rocket(int maxWeight) {
        this.maxWeight = maxWeight;
    }

    public boolean launch() {
        return true;
    }

    public boolean land() {
        return true;
    }

    public boolean canCarry(Item item) {
        return item.weight + currentWeight < maxWeight;
    }

    public void carry(Item item) {
        this.currentWeight += item.weight;
    }
}

class U1 extends Rocket {
    public U1() {
        maxWeight = 10000;
    }
    public boolean launch() {
        Random rand = new Random();
        int crash = (rand.nextInt(100) + 1) * (currentWeight / maxWeight);
        return crash >= 5 * (currentWeight / maxWeight);
    }
    public boolean land() {
        Random rand = new Random();
        int crash = (rand.nextInt(100) + 1) * (currentWeight / maxWeight);
        return crash >= 1 * (currentWeight / maxWeight);
    }
}

class U2 extends Rocket {
    public U2() {
        maxWeight = 18000;
    }
    public boolean launch() {
        Random rand = new Random();
        int crash = (rand.nextInt(100) + 1) * maxWeight;
        return crash <= 4 * currentWeight;
    }
    public boolean land() {
        Random rand = new Random();
        int crash = (rand.nextInt(100) + 1) * maxWeight;
        return crash <= 8 * currentWeight;
    }
}