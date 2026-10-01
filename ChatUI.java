import java.awt.*;
import java.io.*;
import java.util.*;
import javax.swing.*;
import javax.swing.border.EmptyBorder;

public class ChatUI extends JFrame {

    private static final String FAQ_FILE = "faq.txt";
    private static final String NEWLY_LEARNED_FILE = "newly_learned.txt";

    private Map<String, String> faq = new HashMap<>();
    private Set<String> newlyLearned = new HashSet<>();

    private JTextArea chatArea;
    private JTextField inputField;
    private JButton sendButton;

    public ChatUI() {
        setTitle("Majestic Java ChatBot");
        setSize(600, 700);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        initUI();
        loadFAQsFromFile();
        loadNewlyLearned();

        appendBotMessage("Hello! Type 'bye' to exit.");
    }

    private void initUI() {
        // Main panel with padding and background color
        JPanel panel = new JPanel(new BorderLayout(10, 10));
        panel.setBackground(new Color(25, 25, 35));
        panel.setBorder(new EmptyBorder(15, 15, 15, 15));
        setContentPane(panel);

        // Chat display area
        chatArea = new JTextArea();
        chatArea.setEditable(false);
        chatArea.setLineWrap(true);
        chatArea.setWrapStyleWord(true);
        chatArea.setFont(new Font("Serif", Font.PLAIN, 16));
        chatArea.setBackground(new Color(15, 15, 25));
        chatArea.setForeground(Color.WHITE);
        JScrollPane scrollPane = new JScrollPane(chatArea);
        scrollPane.setBorder(BorderFactory.createLineBorder(new Color(70, 130, 180), 2));
        panel.add(scrollPane, BorderLayout.CENTER);

        // Input panel with field and button
        JPanel inputPanel = new JPanel(new BorderLayout(10, 10));
        inputPanel.setBackground(new Color(25, 25, 35));
        inputField = new JTextField();
        inputField.setFont(new Font("Serif", Font.PLAIN, 18));
        inputField.setBackground(new Color(40, 40, 60));
        inputField.setForeground(Color.WHITE);
        inputField.setCaretColor(Color.WHITE);
        inputPanel.add(inputField, BorderLayout.CENTER);

        sendButton = new JButton("Send");
        sendButton.setFont(new Font("Serif", Font.BOLD, 18));
        sendButton.setBackground(new Color(70, 130, 180));
        sendButton.setForeground(Color.WHITE);
        sendButton.setFocusPainted(false);
        inputPanel.add(sendButton, BorderLayout.EAST);

        panel.add(inputPanel, BorderLayout.SOUTH);

        // Send message when button clicked or Enter pressed
        sendButton.addActionListener(e -> sendMessage());
        inputField.addActionListener(e -> sendMessage());
    }

    private void appendUserMessage(String message) {
        appendColoredMessage("You: " + message, new Color(135, 206, 250));
    }

    private void appendBotMessage(String message) {
        appendColoredMessage("Bot: " + message, new Color(144, 238, 144));
    }

    private void appendColoredMessage(String message, Color color) {
        chatArea.setForeground(color);
        chatArea.append(message + "\n\n");
        chatArea.setCaretPosition(chatArea.getDocument().getLength());
        chatArea.setForeground(Color.WHITE); // reset to white after appending
    }

    private void sendMessage() {
        String userInput = inputField.getText().trim().toLowerCase();
        if (userInput.isEmpty()) return;

        appendUserMessage(userInput);
        inputField.setText("");

        if (userInput.equals("bye")) {
            appendBotMessage(faq.getOrDefault("bye", "Goodbye! Have a great day!"));
            saveFAQsToFile();
            saveNewlyLearned();
            disableChat();
            return;
        }

        if (faq.containsKey(userInput)) {
            if (newlyLearned.contains(userInput)) {
                // Ask if want to change response since newly learned
                int option = JOptionPane.showConfirmDialog(this,
                        "I currently respond with:\n\"" + faq.get(userInput) + "\"\nDo you want to change it?",
                        "Edit Response", JOptionPane.YES_NO_OPTION);

                if (option == JOptionPane.YES_OPTION) {
                    String newResponse = JOptionPane.showInputDialog(this, "What should I say instead?");
                    if (newResponse != null && !newResponse.trim().isEmpty()) {
                        faq.put(userInput, newResponse.trim());
                        appendBotMessage("Thanks! I've updated my response.");
                    } else {
                        appendBotMessage("No changes made.");
                    }
                } else {
                    appendBotMessage("Okay, I'll keep my response.");
                }
                newlyLearned.remove(userInput);
                saveFAQsToFile();
                saveNewlyLearned();
            } else {
                appendBotMessage(faq.get(userInput));
            }
        } else {
            // New input: learn response for first time
            String newResponse = JOptionPane.showInputDialog(this,
                    "I don't know how to respond to that. What should I say?");
            if (newResponse != null && !newResponse.trim().isEmpty()) {
                faq.put(userInput, newResponse.trim());
                newlyLearned.add(userInput);
                appendBotMessage("Got it! I'll remember that.");
                saveFAQsToFile();
                saveNewlyLearned();
            } else {
                appendBotMessage("Okay, maybe next time.");
            }
        }
    }

    private void disableChat() {
        inputField.setEnabled(false);
        sendButton.setEnabled(false);
    }

    private void loadFAQsFromFile() {
        File file = new File(FAQ_FILE);
        if (!file.exists()) {
            // Default FAQs
            faq.put("hi", "Hello! How can I help you?");
            faq.put("what is your name", "I'm a Java chatbot.");
            faq.put("how are you", "I'm doing great! What about you?");
            faq.put("good", "Well that's nice, wanna talk?");
            faq.put("bye", "Goodbye! Have a great day!");
            return;
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split("=", 2);
                if (parts.length == 2) {
                    faq.put(parts[0].trim().toLowerCase(), parts[1].trim());
                }
            }
        } catch (IOException e) {
            appendBotMessage("Failed to load FAQs from file.");
        }
    }

    private void saveFAQsToFile() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FAQ_FILE))) {
            for (Map.Entry<String, String> entry : faq.entrySet()) {
                writer.write(entry.getKey() + "=" + entry.getValue());
                writer.newLine();
            }
        } catch (IOException e) {
            appendBotMessage("Failed to save FAQs to file.");
        }
    }

    private void loadNewlyLearned() {
        File file = new File(NEWLY_LEARNED_FILE);
        if (!file.exists()) return;

        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = reader.readLine()) != null) {
                newlyLearned.add(line.trim().toLowerCase());
            }
        } catch (IOException e) {
            appendBotMessage("Failed to load newly learned inputs.");
        }
    }

    private void saveNewlyLearned() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(NEWLY_LEARNED_FILE))) {
            for (String input : newlyLearned) {
                writer.write(input);
                writer.newLine();
            }
        } catch (IOException e) {
            appendBotMessage("Failed to save newly learned inputs.");
        }
    }

    public static void main(String[] args) {
        // Use a nice modern look and feel
        try {
            UIManager.setLookAndFeel("javax.swing.plaf.nimbus.NimbusLookAndFeel");
        } catch (Exception ignored) {
        }

        SwingUtilities.invokeLater(() -> {
            ChatUI chatUI = new ChatUI();
            chatUI.setVisible(true);
        });
    }
}
