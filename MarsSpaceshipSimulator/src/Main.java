import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Simulation sim = new Simulation();
        File phase1 = new File("src/phase1.txt");
        File phase2 = new File("src/phase2.txt");
        ArrayList<Item> p1items = sim.populateFromFile(phase1);
        ArrayList<Item> p2items = sim.populateFromFile(phase2);

        ArrayList<Rocket> u1 = sim.loadU1(p1items);
        int u1price1 = sim.runSimulation(u1);

        u1 = sim.loadU1(p2items);
        int u1price2 = sim.runSimulation(u1);

        ArrayList<Rocket> u2 = sim.loadU2(p1items);
        int u2price1 = sim.runSimulation(u2);

        u2 = sim.loadU2(p2items);
        int u2price2 = sim.runSimulation(u2);

        System.out.printf("U1:\nPhase1: $%s\nPhase2: $%s\n\n", u1price1, u1price2);
        System.out.printf("U2:\nPhase1: $%s\nPhase2: $%s\n", u2price1, u2price2);
        }
}
