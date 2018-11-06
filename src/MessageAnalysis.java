import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class MessageAnalysis {
    private static String[] loadFile(String filePath) {
        try {
            BufferedReader f = new BufferedReader(new FileReader(filePath));
            ArrayList<String> lines = new ArrayList<String>();

            String line;
            System.out.println("Loading in file...");
            while((line = f.readLine()) != null) {
                lines.add(line.toLowerCase());
            }
            System.out.println("Done!");
            f.close();
            java.util.Collections.sort(lines);
            return lines.toArray(new String[]{});
        } catch(FileNotFoundException e) {
            System.out.println("File does not exist!");
        } catch(IOException e) {
            System.out.println("Line does not exist!");
        }
        return new String[0];
    }

    public static void main(String[] args) {
        String[] messages = loadFile("data/Sanitized Files/MESSAGE_OUTPUT.txt");

        int LM = messages.length; //LM -> Last Message

        String ts = "butt";
        ts = ts.toLowerCase();

        int tsCount = 0;

        for(String s : messages) {
            if(s.equals(ts)) {
                tsCount++;
            }
        }
        System.out.println(LM);


    }
}
