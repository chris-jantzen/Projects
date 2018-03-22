import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;

public class Simulation {
    public int runSimulation(ArrayList<Rocket> rockets) {
        int numRockets = rockets.size();
        int index = 0;
        while (index < rockets.size()) {
            if (!rockets.get(index).launch()) {
                rockets.add(new Rocket(rockets.get(index).maxWeight));
                numRockets++;
            }
            index++;
        }
        index = 0;
        while (index < rockets.size()) {
            if (!rockets.get(index).land()) {
                rockets.add(new Rocket(rockets.get(index).maxWeight));
                numRockets++;
            }
            index++;
        }
        if (rockets.get(0).maxWeight == 10000) {
            return numRockets * 100000000;
        }
        else if (rockets.get(0).maxWeight == 18000) {
            return numRockets * 120000000;
        }
        else return 0;
    }

    public ArrayList<Rocket> loadU2 (File file) throws FileNotFoundException {
        ArrayList<Item> items = populateFromFile(file);
        ArrayList<Rocket> rocket = new ArrayList<>();
        rocket.add(new U2());
        int index = 0;
        for (Item i : items) {
            if (rocket.get(index).canCarry(i)) {
                rocket.get(index).carry(i);
            }
            else {
                while (i.weight > 0) {
                    if (!rocket.get(index).canCarry(i)) {
                        Item temp = new Item();
                        temp.weight = rocket.get(index).maxWeight - rocket.get(index).currentWeight;
                        rocket.get(index).carry(temp);
                        i.weight -= temp.weight;
                        rocket.add(new U2());
                        index++;
                    }
                    else {
                        if (i.weight != 0) {
                            rocket.get(index).carry(i);
                            i.weight = 0;
                        }
                    }
                }
            }
        }
        return rocket;
    }

    public ArrayList<Rocket> loadU1 (File file) throws FileNotFoundException {
        ArrayList<Item> items = populateFromFile(file);
        ArrayList<Rocket> rocket = new ArrayList<>();
        rocket.add(new U1());
        int index = 0;
        for (Item i : items) {
            if (rocket.get(index).canCarry(i)) {
                rocket.get(index).carry(i);
            }
            else {
                while (i.weight > 0) {
                    if (!rocket.get(index).canCarry(i)) {
                        Item temp = new Item();
                        temp.weight = rocket.get(index).maxWeight - rocket.get(index).currentWeight;
                        rocket.get(index).carry(temp);
                        i.weight -= temp.weight;
                        rocket.add(new U1());
                        index++;
                    }
                    else {
                        if (i.weight != 0) {
                            rocket.get(index).carry(i);
                            i.weight = 0;
                        }
                    }
                }
            }
        }
        return rocket;
    }

    private static ArrayList<Item> populateFromFile(File file) throws FileNotFoundException {
        Scanner scan = null;
        ArrayList<String> object = new ArrayList<String>();
        ArrayList<String> mass = new ArrayList<String>();
        try {
            scan = new Scanner(file);
        } catch (Exception e) {
            System.out.println("Could not find file.");
        }
        String[] parts;
        while (scan.hasNextLine()) {
            parts = scan.nextLine().split("=");
            object.add(parts[0]);
            mass.add(parts[1]);
        }
        return populateItemArray(object, mass);
    }

    private static ArrayList<Integer> getIntegerArray(ArrayList<String> mass) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (String i : mass) {
            result.add(Integer.parseInt(i.trim()));
        }
        return result;
    }

    private static ArrayList<Item> populateItemArray(ArrayList<String> item, ArrayList<String> sMass) {
        ArrayList<Integer> mass = getIntegerArray(sMass);
        ArrayList<Item> items = new ArrayList<Item>();
        for (int i=0; i<item.size(); i++) {
            Item object = new Item();
            object.name = item.get(i);
            object.weight = mass.get(i);
            items.add(object);
        }
        return items;
    }
}
