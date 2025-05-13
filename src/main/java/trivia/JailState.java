package trivia;

public class JailState {
    enum State {
        IN, OUT
        , GOTOUT
//        , CAN_GET_OUT
    // perhaps it's easier for the brain to think of moving in a state in which you
    //    might eventually get out of jail if you answer the question correctly
    }
    // instead of getting it out and then sending the player back to jail

    private State state = State.OUT;

    State state() {
        return state;
    }

    void freeIf(boolean free) {
        if (!isJailed()) {
            state = State.OUT;
        } else if (free) {
            state = State.GOTOUT;
        }
    }

    void sendToJail() {
        state = State.IN;
    }

    boolean isJailed() {
        return state == State.IN;
    }
}
