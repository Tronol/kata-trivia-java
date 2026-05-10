package trivia;

class Player {
    final String name;
    int position = 0;
    int coins = 0;
    boolean inPenaltyBox = false;

    Player(String name) {
        this.name = name;
    }

    void advanceTo(int roll) {
        position += roll;
        if (position > QuestionDeck.BOARD_SIZE) position -= QuestionDeck.BOARD_SIZE;
    }

    void addCoin() {
        coins++;
    }

    void sendToPenaltyBox() {
        inPenaltyBox = true;
    }

    boolean hasWon() {
        return coins == QuestionDeck.WINNING_COINS;
    }
}
