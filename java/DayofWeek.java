import java.util.Scanner;

public class DayofWeek {

    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);

        System.out.println("Enter date");
        int d = console.nextInt();
        
        System.out.println("Enter month");
        int m = console.nextInt();

        System.out.println("Enter year");
        int y = console.nextInt();

        System.out.println("The day is: " + dayofweek(d, m, y));

        console.close();
    }

    public static String dayofweek(int d, int m, int y) 
    {
        int y0 = y - (14-m) / 12;
        int x0 = y0 + y0 / 4 - y0 / 100 + y0/400;
        int m0 = m + 12*((14-m)/12)- 2;
        int D = (d + x0 + 31*m0 / 12) % 7;

        if (D == 0) return "Sunday";
        else if (D == 1) return "Monday";
        else if (D == 2) return "Tuesday";
        else if (D == 3) return "Wednesday";
        else if (D == 4) return "Thursday";
        else if (D == 5) return "Friday";
        else if (D == 6) return "Saturday";
        
        return null;
    }
}
