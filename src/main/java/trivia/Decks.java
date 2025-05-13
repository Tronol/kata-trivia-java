package trivia;

public class Decks {
    private final QuestionDeck[] questionDecks = {
        // Enum if you wouldn't have had created an object QuestionDeck with a string name
            new QuestionDeck("Rock"),
            new QuestionDeck("Pop"),
            new QuestionDeck("Science"),
            new QuestionDeck("Sports")
    };

    QuestionDeck deckAtBoardLocation(int location) {
        return questionDecks[location % questionDecks.length];
    }
}
