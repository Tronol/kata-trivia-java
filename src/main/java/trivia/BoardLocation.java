package trivia;

public class BoardLocation {
    private static final int TOTAL_LOCATIONS = 12;
    private int location = 0;

    // You just got a Bonu$: true meaingful semantic, OOP encapsulated
    void advance(int count) {
        location = (location + count) % TOTAL_LOCATIONS;
    }

    int location() {
        return location + 1;
    }
}
