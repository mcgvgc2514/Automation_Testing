// These exercizes were inspired by w3schools Java tutorial

/* To run:
   - Navigate to the directory of this file in Terminal
   - run javac JavaTutorial.java
   - run java JavaTutorial
 */

public class JavaTutorial { // class name must be same as file name
    // Methods:
    static void myMethod(){
        System.out.println("myMethod just got executed!");
    }
    // Method parameters and arguments:
    static void myMethod2(String fname, int fnum) {
        System.out.println("myMethod2 calls: " + fname + fnum);
    }
    // Method return values:
    static int myMethod3(int x, int y) {
        return 5 + x + y;
    }
    public static void main(String[] args) {
        System.out.println("Hello World");
        System.out.println("Goodbye");
        // These two below should print on the same line.
        System.out.print("Hello");
        System.out.println("Goodbye");

        String name = "John";
        System.out.println("Hello " + name);

        int myNum = 14;
        myNum = 145;
        final int yourNum = 21; // "final" means that the variable can't be changed
        System.out.println(myNum);
        System.out.println(yourNum);

        // Different variable type examples:
        int theNum = 55;
        float myFloatNum = 5.32f;
        char myLetter = 'D';
        boolean myBool = true;
        String myText = "Hello";

        String addStrings = myText + name;
        System.out.println(addStrings);

        // Can declare multiple variables on same line:
        int x = 5, y = 6, z = 50;
        System.out.println(x + y + z);

        // Scientific numbers:
        float f1 = 35e3f;
        System.out.println(f1);

        // Division:
        System.out.println(x/y);
        // Modulus (returns the division remainder):
        System.out.println(x%y);
        // Operator applied to change the varaible:
        int f = 1;
        f += 10;
        System.out.println(f);

        /*  Logical Operators:
                 - And is &&
                 - Or is ||
                 - Not is !
        */

        // String length:
        String txt = ";alksdjf;ajweiofnaskddl;saf";
        System.out.println("The Length of the string is: " + txt.length());       
        
        // Find character in a string:
        String locateText = "Locate the index of 'fun' here!";
        System.out.println(locateText.indexOf("fun"));

        // .concat() method adds two strings together

        // How to put quotes in strings (put 1 \ before):
        String quoteText = "Here \'is\' how you \"use\" quotes\\slashes.";
        System.out.println(quoteText);

        /* Other backslash uses:
            - \n New line
            - \r Carriage return
            - \t Tab
            - \b Backspace
            - \f Form feed
        */

        // Math class / methods
        System.out.println("Maximum value: " + Math.max(1, 20));
        System.out.println("Minimum value: " + Math.min(1, 20));
        System.out.println("Square Root: " + Math.sqrt(64));
        System.out.println("Absolute value: " + Math.abs(-55.5));
        System.out.println("Random number: " + Math.random());

        // Get a random number between 0 and 100:
        int randomNum = (int)(Math.random() * 101);
        System.out.println("Random number between 0 and 100: " + randomNum);
        
        // If-else voting age code example:
        int myAge = 30;
        int votingAge = 18;

        if (myAge >= votingAge) {
            System.out.println("Can vote");
        } else {
            System.out.println("Not old enough");
        }

        // Shorthand version of above code:
        String result = (myAge >= votingAge) ? "Can vote" : "Not old enough";
        System.out.println(result);

        // Switch example:
        int day = 1;
        switch (day) {
            case 1:
                System.out.println("Sunday");
                break;
            case 2:
                System.out.println("Monday");
                break;
            case 3:
                System.out.println("Tuesday");
                break;
            case 4:
                System.out.println("Wednesday");
                break;
            case 5:
                System.out.println("Thursday");
                break;
            case 6:
                System.out.println("Friday");
                break;
            case 7:
                System.out.println("Saturday");
                break;
            default: 
                System.out.println("Pick a number from 1 through 7"); 
        }

        // While loop:
        int i = 0;
        while (i < 5) {
            System.out.println(i);
            i++;
        }

        // Do-while loop:
        i = 0;
        do {
            System.out.println(i);
            i++;
        } 
        while (i < 5);

        // For loop:
        for (i = -10; i < 5; i++) { // (executed 1 time; execution condition (while); executed after)
            System.out.println(i);
        }

        // For-each loop:
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"}; // This is an array
        for (String car : cars) {
            System.out.println(car);
        }

        // Continue statement skips to next iteration
        // The following code will skip printing 4:
        for (i = 0; i < 10; i++) {
            if (i == 4) {
                continue;
            }
            System.out.println(i);
        }

        // Change a specific element in an array:
        cars[0] = "Opel";
        System.out.println(cars[0]);

        // array.length property shows how many elements an array has
        System.out.println(cars.length);

        // Loop through an array
        for (i = 0; i < cars.length; i++) {
            System.out.println(cars[i]);
        }

        // Multidimensional arrays:
        int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
        System.out.println(myNumbers[1][2]);

        // Execute the previoulsy made methods:
        myMethod();
        myMethod2("Bob", 33);
        System.out.println(myMethod3(24,42));

        
    }
}