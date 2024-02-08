import javax.swing.*;
import java.awt.*;
import java.util.HashMap;
import java.util.Map;

class DFAPanel extends JPanel {

    private Map<String, Point> statePositions;
    private Map<String, Map<Character, String>> transitions;

    public DFAPanel(Map<String, Point> statePositions, Map<String, Map<Character, String>> transitions) {
        this.statePositions = statePositions;
        this.transitions = transitions;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Draw states
        for (String state : statePositions.keySet()) {
            Point position = statePositions.get(state);
            g.drawOval(position.x - 20, position.y - 20, 40, 40);
            g.drawString(state, position.x - 5, position.y + 5);
        }

        // Draw transitions
        for (String fromState : transitions.keySet()) {
            Map<Character, String> transitionMap = transitions.get(fromState);
            Point fromPosition = statePositions.get(fromState);

            for (char symbol : transitionMap.keySet()) {
                String toState = transitionMap.get(symbol);
                Point toPosition = statePositions.get(toState);

                drawArrow(g, fromPosition, toPosition);
                g.drawString(String.valueOf(symbol), (fromPosition.x + toPosition.x) / 2, (fromPosition.y + toPosition.y) / 2);
            }
        }
    }

    private void drawArrow(Graphics g, Point from, Point to) {
        int arrowSize = 8;

        g.drawLine(from.x, from.y, to.x, to.y);

        double angle = Math.atan2(to.y - from.y, to.x - from.x);
        int x1 = (int) (to.x - arrowSize * Math.cos(angle - Math.PI / 6));
        int y1 = (int) (to.y - arrowSize * Math.sin(angle - Math.PI / 6));
        int x2 = (int) (to.x - arrowSize * Math.cos(angle + Math.PI / 6));
        int y2 = (int) (to.y - arrowSize * Math.sin(angle + Math.PI / 6));

        g.drawLine(to.x, to.y, x1, y1);
        g.drawLine(to.x, to.y, x2, y2);
    }
}

public class DFAGenerator extends JFrame {

    public DFAGenerator(Map<String, Map<Character, Character>> transitionTable) {
        setTitle("DFA Visualization");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Extract states and transitions from the transition table
        Map<String, Point> statePositions = new HashMap<>();
        Map<String, Map<Character, String>> transitions = new HashMap<>();

        int x = 100;
        int y = 100;
        int angle = 0;

        for (String state : transitionTable.keySet()) {
            statePositions.put(state, new Point(x + (int) (Math.cos(Math.toRadians(angle)) * 100),
                    y + (int) (Math.sin(Math.toRadians(angle)) * 100)));

            angle += 120;
        }

        for (String fromState : transitionTable.keySet()) {
            Map<Character, Character> transitionMap = transitionTable.get(fromState);
            Map<Character, String> mappedTransitions = new HashMap<>();

            for (char symbol : transitionMap.keySet()) {
                Character toState = transitionMap.get(symbol);
                mappedTransitions.put(symbol, String.valueOf(toState));
            }

            transitions.put(fromState, mappedTransitions);
        }

        DFAPanel dfaPanel = new DFAPanel(statePositions, transitions);
        add(dfaPanel, BorderLayout.CENTER);

        setSize(800, 600);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    public static void main(String[] args) {
        // Example transition table
        Map<String, Map<Character, Character>> transitionTable = new HashMap<>();
        transitionTable.put("A", Map.of('a', 'B', 'b', 'C'));
        transitionTable.put("B", Map.of('a', 'A', 'b', 'C'));
        transitionTable.put("C", Map.of('a', 'B', 'b', 'A'));

        SwingUtilities.invokeLater(() -> new DFAGenerator(transitionTable));
    }
}
