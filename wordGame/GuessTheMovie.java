import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;
import java.util.Random;

public class GuessTheMovie {
    public static int getNumberOfMovies(Scanner scan) {
        int moviesCount = 0;
        while (scan.hasNextLine()) {
            String line = scan.nextLine();
            moviesCount++;
        }
        return moviesCount;
    }

    public static String pickMovie(File file, Scanner scan, int num) throws FileNotFoundException {
        try {
            scan = new Scanner(file);
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }
        Random rand = new Random();
        int randomNum = rand.nextInt(num)+1;
        String movie = "";
        for (int i=0; i<randomNum; i++) {
            movie = scan.nextLine();
        }
        return movie;
    }

    public static String setUpUnders(String movie) {
        String unders = "";
        for (int i=0; i<movie.length(); i++) {
            if (movie.charAt(i) != ' ') {
                unders += "_";
            }
            else {
                unders += " ";
            }
        }
        return unders;
    }

    public static boolean isWin() {
        for (char i: hidden) {
            if (i == '_') return false;
        }
        System.out.println("\nYou've Won!");
        return true;
    }

    public static char[] guessCharacter(char guess, String title) {
        boolean wasRight = false;
        for (int i = 0; i < title.length(); i++) {
            if (title.charAt(i) == guess) {
                hidden[i] = guess;
                wasRight = true;
            }
        }

        if (!wasRight) {
            incorrect[incorrectIndex++] = guess;
            wrong++;
        }
        return hidden;
    }

    public static void getGuess() {
        Scanner scan = new Scanner(System.in);
        System.out.print("\nYou have guessed " + wrong + " wrong letters: ");
        for (int i=0; i<incorrectIndex; i++) {
            System.out.printf("%s ", incorrect[i]);
        }
        System.out.println("\nGuess a letter: ");
        char g = scan.next().charAt(0);
        System.out.print("You are guessing: ");
        hidden = guessCharacter(g, movie);
        for (char i: hidden) System.out.printf("%s ", i);
        gameover = isWin();
    }

    static char[] hidden = null;
    static char[] incorrect = new char[10];
    static int incorrectIndex = 0;
    static int wrong = 0;
    static String movie = null;
    static boolean gameover = false;

    public static void main(String [] args) throws FileNotFoundException{
        File file = new File("./src/movies.txt");
        Scanner fileScan = null;
        try {
            fileScan = new Scanner(file);
        } catch (FileNotFoundException exception) {
            System.out.println("File not found.");
        }
        int numMovies = getNumberOfMovies(fileScan);
        movie = pickMovie(file, fileScan, numMovies);
        int lenMovieTitle = movie.length();
        String underScores = "";
        underScores = setUpUnders(movie);
        hidden = underScores.toCharArray();
        while (wrong < 10 && !gameover) {
            getGuess();
        }
        if (wrong == 10) {
            System.out.println("\nGame over, the movie was " + movie + ".");
        }
    }
}
