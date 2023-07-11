import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day1 {
    public static void main(String[] args) {
        try {
            File file = new File("day1.txt"); // Replace with the name of your file
            Scanner scanner = new Scanner(file);
            if (scanner.hasNextLine()) {
                String firstLine = scanner.nextLine();
                System.out.println(firstLine);
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}