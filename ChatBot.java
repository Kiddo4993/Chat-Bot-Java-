import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class ChatBot {
    private static Map<String, String> faq = new HashMap<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        // Predefined FAQs
        faq.put("hi", "Hello! How can I help you?");
        faq.put("what is your name", "I'm a Java chatbot.");
        faq.put("how are you", "I'm doing great! What about you?");
        faq.put("good", "Well that's nice, wanna talk?");
        faq.put("bye", "Goodbye! Have a great day!");

        System.out.println("ChatBot: Hello! Type 'bye' to exit.");
        while (true) {
            System.out.print("You: ");
            String userInput = scanner.nextLine().trim().toLowerCase();

            if (userInput.equals("bye")) {
                System.out.println("ChatBot: " + faq.get("bye"));
                break;
            }

            if (faq.containsKey(userInput)) {
                System.out.println("ChatBot: " + faq.get(userInput));
            } else {
                System.out.println("ChatBot: I don't know how to respond to that. What should I say?");
                String newResponse = scanner.nextLine();
                faq.put(userInput, newResponse);
                System.out.println("ChatBot: Got it! I'll remember that.");
            }
        }
    }
}
