import java.util.Random;
import java.util.ArrayList;
import java.util.Scanner;
public class uno {
    private static ArrayList<String> hand = new ArrayList<String>();
    private static String currentcard = "red 1";
    static boolean running = true;
    public static void main(String[] args) {

        for (int i = 0; i < 7; i++) {
            hand.add(generatecard());
        }
        while(running){
            playerturn(currentcard);
            opponentturn(currentcard);
        }
    }
    public static String generatecard() {
        Random random = new Random();
        int colornum = random.nextInt(4);
        String color = "";
        switch (colornum) {
            case 0:
                color = "red";
                break;
            case 1:
                color = "blue";
                break;
            case 2:
                color = "green";
                break;
            case 3:
                color = "yellow";
                break;
        }
        int number = random.nextInt(10);
        return color + " " + String.valueOf(number);
    }
    public static void playerturn(String pastcard) {
        System.out.println("Current card: " + currentcard);
        ArrayList<String> pastprops = new ArrayList<String>();
        ArrayList<String> cardprops = new ArrayList<String>();
        for (int i = 0; i < hand.size(); i++) {
            System.out.println(hand.get(i));
        }
        System.out.print("Which card will you play? ");
        Scanner input = new Scanner(System.in);
        String card = input.nextLine();
        cardprops.add(card.split(" ")[0]);
        cardprops.add(card.split(" ")[1]);
        pastprops.add(pastcard.split(" ")[0]);
        pastprops.add(pastcard.split(" ")[1]);
        if (cardprops.get(0).equals(pastprops.get(0)) || cardprops.get(1).equals(pastprops.get(1))) {
            for (int i = 0; i < hand.size(); i++) {
                if (card.equals(hand.get(i))) {
                    hand.remove(card);
                    currentcard = card;
                    if(hand.size() == 0){
                        System.out.println("You won!");
                        running = false;
                    }
                }
            }
        } else {
            System.out.println("Card doesn't match.");
            hand.add(generatecard());
        }
    }
    public static void opponentturn(String pastcard){
        ArrayList<String> pastprops = new ArrayList<String>();
        pastprops.add(pastcard.split(" ")[0]);
        pastprops.add(pastcard.split(" ")[1]);
        Random random = new Random();
        int numorcol = random.nextInt(3);
        String color = "";
        int num = 0;
        switch(numorcol){
            case 0:
                num = random.nextInt(10);
                color = pastprops.get(0);
                break;
            case 1:
                num = random.nextInt(10);
                color = pastprops.get(0);
                break;
            case 2:
                int colornum = random.nextInt(4);
                switch (colornum) {
                    case 0:
                        color = "red";
                        break;
                    case 1:
                        color = "blue";
                        break;
                    case 2:
                        color = "green";
                        break;
                    case 3:
                        color = "yellow";
                        break;
                }
                num = Integer.parseInt(pastprops.get(1));
                break;
        }
        currentcard = color + " " + String.valueOf(num);
    }
}
