package trivia;

class QuestionDeck {
    private final String name;
    private int i = 0;

    QuestionDeck(String name) {
        this.name = name;
    }

    String pullQuestion() {
      String s = name + " Question " + i;
      i++;
      return s;
    }

    public String name() {
        return name;
    }
}
