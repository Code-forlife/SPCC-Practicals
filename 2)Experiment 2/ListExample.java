import javax.swing.*;
import java.awt.*;

public class ListExample extends JFrame {

    public ListExample() {
        // Set up the JFrame
        setTitle("List Example");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 200);

        // Create a list model with some data
        DefaultListModel<String> listModel = new DefaultListModel<>();
        listModel.addElement("Item 1");
        listModel.addElement("Item 2");
        listModel.addElement("Item 3");
        listModel.addElement("Item 4");

        // Create a JList with the list model
        JList<String> myList = new JList<>(listModel);

        // Set up the layout
        setLayout(new BorderLayout());
        add(new JScrollPane(myList), BorderLayout.CENTER);

        // Display the JFrame
        setLocationRelativeTo(null);
        setVisible(true);
    }

    public static void main(String[] args) {
        // Run the GUI on the Event Dispatch Thread (EDT)
        SwingUtilities.invokeLater(() -> new ListExample());
    }
}
