package trivia;

import java.util.ArrayList;
import java.util.List;

class PlayersAtTable {
    private final List<Player> table = new ArrayList<>();
    private int current = -1;

    void add(Player player) {
        table.add(player);
    }

    int count() {
        return table.size();
    }

    Player current() {
        return table.get(current);
    }

//    Player next() { // both a COMMAND + and a QUERY
//        current = (current + 1) % table.size();
//        return current();
//    }
    void startNextPlayerTurn() { //COMMAND
        current = (current + 1) % table.size();
    }
}
