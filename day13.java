import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class TestClass {

    private int a = 1;

    public void playMusic() {
        System.out.println("Playing Music...");
    }

    public void playMusic(String music) {
        System.out.println("Playing Music " + music);
    }

    public void showA() {
        System.out.println(a);
    }

    public int a() {
        return a;
    }
}

abstract class A {
    abstract public int b();
}

interface Innerday13 {
    int x = 10;
    int x();
    int y();
    // int y() {System.out.println("y");} - not possible 
}

enum Status {
    A(10), B(10), C;

    public int x;

    private Status() {}
    private Status(int x) {
        this.x = x;
    }
}

class day13 {

    public static void main(String args[]) {
        char lol = 'a';
        double x = 15.0;
        char y = (char) x;
        System.out.println(y);
        System.out.println((int) lol);
        System.out.println(lol);
        // System.out.println((char) 10);
        System.out.println(x + lol);
        System.out.println(lol);
        System.out.println("Hello World");

        byte test = 3;
        int test2 = 4;
        System.out.println(test + test2);
        boolean test3 = false;
        int test4 = test3 ? 1 : 0;
        System.out.println(test4 + test2);

        float a = 15.0f;
        var b = 10;
        System.out.println(a+b);

        byte c = 127;
        byte d = 2;
        System.out.println(c + d); // no overflow -> automatic casting
        int e = 127;
        System.out.println((byte) e);
        
        int f = switch(c) {
            case 127 -> {
                System.out.println(c);
                yield 1;
            }
            default -> 0;
        };

        System.out.println(f);

        int g = switch(c) {
            case 127 : 
                System.out.println(c);
                yield 1;
            
            default : 
                yield 0;
        };

        System.out.println(g);

        switch (g) {
            case 1:
                System.out.println("lolo");
                System.out.println("Lolo");
                break;
        
            default:
                break;
        }

        for (int i=0; i<5; i++) {
            System.out.println(String.format("Iteration %d%d", 0, i));
        }

        String h = Integer.toString(5);
        System.out.println(h);

        TestClass obj = new TestClass();
        obj.playMusic();
        obj.playMusic("Rammstein");

        int num[] = new int[4];
        System.out.println(Arrays.toString(num));

        int nums[][] = new int[3][4];
        System.out.println(Arrays.deepToString(nums));

        TestClass classes[] = new TestClass[5];
        System.out.println(Arrays.toString(classes));

        String m = "test";
        String n = "test";
        System.out.println(m.hashCode());
        System.out.println(n.hashCode());
        m = m + "1";
        System.out.println(m.hashCode());
        System.out.println(n.hashCode());

        obj.showA();
        System.out.println(obj.a());
        obj.toString();
        obj.hashCode();

        System.out.println(Innerday13.x);

        System.out.println(Status.A.toString());

        Innerday13 o = new Innerday13() {
            public int x() {return 1;}
            public int y() {return 2;}
        };

        System.err.println(o.y());

        final var p = 80;
        System.out.println(p);

        ArrayList<Integer> numbers = new ArrayList<Integer>();
        List<Integer> numbers2 = Arrays.stream(num).boxed().toList();
        List<Integer> numbers3 = Arrays.asList(1,2,3);
    }
}