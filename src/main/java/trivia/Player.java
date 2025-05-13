package trivia;

// shallow immutable
record Player(
    String name,
    BoardLocation boardLocation,
    Purse purse,
    JailState jailState) {

  // Code Smell: attempt to encapsulate a record = you can't hide properties in them
  Player(String name) {
    this(name, new BoardLocation(), new Purse(), new JailState());
  }
}
