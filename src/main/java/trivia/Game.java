package trivia;

import java.util.Objects;

import static trivia.JailState.State.GOTOUT;
import static trivia.JailState.State.IN;

public class Game implements IGame {

  private final PlayersAtTable playersAtTable = new PlayersAtTable();
  private final Decks decks = new Decks();

  public boolean add(String playerName) {
    playersAtTable.add(new Player(playerName));
    int number = playersAtTable.count();

    log(playerName + " was added");
    log("They are player number " + number);
    return true;
  }

  public void roll(int roll) {
    playersAtTable.startNextPlayerTurn();
    Player currentPlayer = playersAtTable.current();

    logPlayer(" is the current player");
    log("They have rolled a " + roll);

    currentPlayer.jailState().freeIf(roll % 2 != 0);

    if (currentPlayer.jailState().state() == IN) {
      logPlayer(" is not getting out of the penalty box");
      return;
    }
    if (currentPlayer.jailState().state() == GOTOUT) {
      logPlayer(" is getting out of the penalty box");
    }
    currentPlayer.boardLocation().advance(roll);
    logPlayer("'s new location is " + currentPlayer.boardLocation().location());

    QuestionDeck questionDeck = decks.deckAtBoardLocation(currentPlayer.boardLocation().location());
    log("The category is " + questionDeck.name());
    log(questionDeck.pullQuestion());
  }

  public boolean handleCorrectAnswer() {
    Player currentPlayer = playersAtTable.current();

    if (currentPlayer.jailState().isJailed()) {
      return true;
    }
    log("Answer was correct!!!!");

    currentPlayer.purse().add(1);
    logPlayer(" now has " + currentPlayer.purse().coins() + " Gold Coins.");
    return currentPlayer.purse().coins() != Purse.COINS_TO_WIN;
  }

  public boolean wrongAnswer() {
    Player currentPlayer = playersAtTable.current();
    if (!currentPlayer.jailState().isJailed()) {
      log("Question was incorrectly answered");
      logPlayer(" was sent to the penalty box");
      currentPlayer.jailState().sendToJail();
    }
    return true;
  }

  @SuppressWarnings("java:S106")
  private void log(String text) {
    System.out.println(text);
  }

  private void logPlayer(String text) {
    log(playersAtTable.current().name() + text);
  }
}
