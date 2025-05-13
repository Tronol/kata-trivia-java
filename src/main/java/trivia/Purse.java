package trivia;

public class Purse {
    static final int COINS_TO_WIN = 6;
    private int coins = 0;

    // speculative
    void add(int coins) {
        this.coins += coins;
    }

    int coins() {
        return coins;
    }

    // boolean isWinner ???
}
