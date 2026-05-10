package trivia;

import java.util.ArrayList;
import java.util.List;

// REFACTORED
public class Game implements IGame {
    private final List<Player> players = new ArrayList<>();
    private final QuestionDeck deck = new QuestionDeck();
    private int currentPlayer = 0;
    private boolean isGettingOutOfPenaltyBox;

    public boolean isPlayable() {
        return howManyPlayers() >= 2;
    }

    public boolean add(String playerName) {
        players.add(new Player(playerName));
        System.out.println(playerName + " was added");
        System.out.println("They are player number " + players.size());
        return true;
    }

    public int howManyPlayers() {
        return players.size();
    }

    private Player current() {
        return players.get(currentPlayer);
    }

    private void advancePosition(int roll) {
        current().advanceTo(roll);
        System.out.println(current().name + "'s new location is " + current().position);
        String category = deck.categoryFor(current().position);
        System.out.println("The category is " + category);
        deck.ask(category);
    }

    private void advanceTurn() {
        currentPlayer++;
        if (currentPlayer == players.size()) currentPlayer = 0;
    }

    public void roll(int roll) {
        System.out.println(current().name + " is the current player");
        System.out.println("They have rolled a " + roll);

        if (!current().inPenaltyBox) {
            advancePosition(roll);
            return;
        }

        boolean leavingBox = roll % 2 != 0;
        isGettingOutOfPenaltyBox = leavingBox;
        if (leavingBox) {
            System.out.println(current().name + " is getting out of the penalty box");
            advancePosition(roll);
        } else {
            System.out.println(current().name + " is not getting out of the penalty box");
        }
    }

    private boolean awardCoinAndCheckWin() {
        current().addCoin();
        System.out.println(current().name + " now has " + current().coins + " Gold Coins.");
        boolean winner = !current().hasWon();
        advanceTurn();
        return winner;
    }

    public boolean handleCorrectAnswer() {
        if (current().inPenaltyBox) {
            if (isGettingOutOfPenaltyBox) {
                System.out.println("Answer was correct!!!!");
                return awardCoinAndCheckWin();
            } else {
                advanceTurn();
                return true;
            }
        }
        System.out.println("Answer was correct!!!!");
        return awardCoinAndCheckWin();
    }

    public boolean wrongAnswer() {
        System.out.println("Question was incorrectly answered");
        System.out.println(current().name + " was sent to the penalty box");
        current().sendToPenaltyBox();
        advanceTurn();
        return true;
    }
}
