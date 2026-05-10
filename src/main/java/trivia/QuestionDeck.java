package trivia;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

class QuestionDeck {
    static final int BOARD_SIZE = 12;
    static final int WINNING_COINS = 6;
    static final int QUESTIONS_PER_CATEGORY = 50;

    private static final String[] CATEGORIES = {"Pop", "Science", "Sports", "Rock", "Geography"};

    private static final Map<Integer, String> CATEGORY_BY_POSITION = new HashMap<>();
    static {
        CATEGORY_BY_POSITION.put(0, "Pop"); CATEGORY_BY_POSITION.put(4, "Pop"); CATEGORY_BY_POSITION.put(8, "Pop");
        CATEGORY_BY_POSITION.put(1, "Science"); CATEGORY_BY_POSITION.put(5, "Science"); CATEGORY_BY_POSITION.put(9, "Science");
        CATEGORY_BY_POSITION.put(2, "Sports"); CATEGORY_BY_POSITION.put(6, "Sports"); CATEGORY_BY_POSITION.put(10, "Sports");
        CATEGORY_BY_POSITION.put(3, "Geography"); CATEGORY_BY_POSITION.put(7, "Geography");
    }

    private final Map<String, LinkedList<String>> questions = new HashMap<>();

    QuestionDeck() {
        for (String cat : CATEGORIES) questions.put(cat, new LinkedList<>());
        for (int i = 0; i < QUESTIONS_PER_CATEGORY; i++) {
            questions.get("Pop").add("Pop Question " + i);
            questions.get("Science").add("Science Question " + i);
            questions.get("Sports").add("Sports Question " + i);
            questions.get("Rock").add("Rock Question " + i);
            questions.get("Geography").add("Geography Question " + i);
        }
    }

    void ask(String category) {
        System.out.println(questions.get(category).removeFirst());
    }

    String categoryFor(int position) {
        return CATEGORY_BY_POSITION.getOrDefault(position - 1, "Rock");
    }
}
