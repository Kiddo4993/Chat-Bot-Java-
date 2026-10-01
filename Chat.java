import java.io.*;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Chat {
    private static Map<String, String> faq = new HashMap<>();
    private static Set<String> newlyLearned = new HashSet<>(); // inputs 
    private static final String FAQ_FILE = "faq.txt";
    private static final String NEWLY_LEARNED_FILE = "newly_learned.txt";
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        loadFAQsFromFile();
        loadNewlyLearned();

        System.out.println("ChatBot: Hello! Type 'bye' to exit.");
        while (true) {
            System.out.print("You: ");
            String userInput = scanner.nextLine().trim().toLowerCase();

            if (userInput.equals("bye")) {
                System.out.println("ChatBot: " + faq.getOrDefault("bye", "Goodbye!"));
                saveFAQsToFile();
                saveNewlyLearned();
                break;
            }

            if (faq.containsKey(userInput)) {
                if (newlyLearned.contains(userInput)) {
                    // Ask if want to change response since it's newly learned
                    System.out.println("ChatBot: I currently respond with: \"" + faq.get(userInput) + "\". Do you want to change it? (yes/no)");
                    String answer = scanner.nextLine().trim().toLowerCase();
                    if (answer.equals("yes")) {
                        System.out.println("ChatBot: What should I say instead?");
                        String newResponse = scanner.nextLine();
                        faq.put(userInput, newResponse);
                        System.out.println("ChatBot: Thanks! I've updated my response.");
                    } else {
                        System.out.println("ChatBot: Okay, I'll keep my response.");
                    }
                    newlyLearned.remove(userInput);
                    saveFAQsToFile();
                    saveNewlyLearned();
                } else {
                    //reply normally
                    System.out.println("ChatBot: " + faq.get(userInput));
                }
            } else {
                // new input
                System.out.println("ChatBot: I don't know how to respond to that. What should I say?");
                String newResponse = scanner.nextLine();
                faq.put(userInput, newResponse);
                newlyLearned.add(userInput);
                System.out.println("ChatBot: Got it! I'll remember that.");
                saveFAQsToFile();
                saveNewlyLearned();
            }
        }
    }

    private static void loadFAQsFromFile() {
        File file = new File(FAQ_FILE);
        if (!file.exists()) {
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
            System.out.println("ChatBot: Failed to load FAQs.");
        }
    }

    private static void saveFAQsToFile() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FAQ_FILE))) {
            for (Map.Entry<String, String> entry : faq.entrySet()) {
                writer.write(entry.getKey() + "=" + entry.getValue());
                writer.newLine();
            }
        } catch (IOException e) {
            System.out.println("ChatBot: Failed to save FAQs.");
        }
    }

    private static void loadNewlyLearned() {
        File file = new File(NEWLY_LEARNED_FILE);
        if (!file.exists()) return;

        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = reader.readLine()) != null) {
                newlyLearned.add(line.trim().toLowerCase());
            }
        } catch (IOException e) {
            System.out.println("ChatBot: Failed to load newly learned data.");
        }
    }

    private static void saveNewlyLearned() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(NEWLY_LEARNED_FILE))) {
            for (String key : newlyLearned) {
                writer.write(key);
                writer.newLine();
            }
        } catch (IOException e) {
            System.out.println("ChatBot: Failed to save newly learned data.");
        }
    }
}
