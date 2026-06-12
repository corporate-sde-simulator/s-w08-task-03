# Beginner Explanatory Guide: FINSERV-4255: Fix support ticket auto-classifier misrouting tickets

> **Task Type**: Service Task  
> **Domain/Focus**: Python fundamentals, Bug Fixing

---

## 1. The Goal (In-Depth Beginner Explanation)

### The Core Problem
The task at hand addresses a critical issue within the support ticket classification system used by the application. Currently, the system misroutes support tickets to the wrong teams due to two significant bugs. The first bug arises from the case sensitivity of keyword matching; for instance, the keyword "Payment" does not match "payment," leading to potential misclassification of tickets related to billing issues. This inconsistency can frustrate users and delay the resolution of their problems, as tickets may not reach the appropriate team promptly.

The second bug involves the priority scoring mechanism, where low-priority keywords are incorrectly assigned higher scores than critical ones. This flaw means that tickets marked as "urgent" or "critical" may be deprioritized in favor of less important issues, which can severely impact the efficiency of the support team. Fixing these bugs is essential not only for improving the accuracy of ticket routing but also for enhancing user satisfaction and operational efficiency within the support system.

### Jargon Buster (Key Terms Explained)
* **Keyword Matching**: This is a technique used in programming to find specific words or phrases within a larger body of text. For example, if a ticket mentions "payment," the system should recognize this keyword and classify the ticket under the billing team. If the keyword is not matched due to case sensitivity, the ticket may be misrouted.

* **Case Sensitivity**: This refers to the distinction between uppercase and lowercase letters in text. For instance, "Payment" and "payment" are treated as different strings in a case-sensitive system. This can lead to missed matches in keyword searches, causing errors in classification.

* **Priority Scoring**: This is a method used to assign importance levels to different keywords. In this context, keywords associated with critical issues should have higher scores than those related to minor concerns. For example, the keyword "outage" should be prioritized over "how to," ensuring that urgent tickets are addressed first.

* **Unit Tests**: These are small, automated tests designed to verify that individual parts of the code (like functions or methods) work as intended. They help ensure that changes made to the code do not introduce new bugs and that existing functionality remains intact.

### Expected Outcome
After implementing the necessary fixes, the ticket classification system should function correctly, accurately routing tickets to the appropriate teams based on the keywords present in the ticket's subject and body. 

**Before vs. After Comparison**:
- **Before**: A ticket with the subject "Payment issue" may be misrouted to the technical team due to case sensitivity, and a critical ticket may be deprioritized because it contains a low-priority keyword.
- **After**: The same ticket will be correctly classified under the billing team regardless of case, and critical tickets will be prioritized appropriately, ensuring that urgent issues are addressed promptly.

---

## 2. Related Coding Concepts & Syntax (50% Theory, 50% Practice)

### Concept 1: String Manipulation
#### 📘 Theoretical Overview (50%)
String manipulation is a fundamental concept in programming that involves modifying, analyzing, or processing text data. In the context of this task, string manipulation is crucial for implementing case-insensitive keyword matching. If we do not handle string manipulation correctly, we risk missing important keywords, leading to misclassification of tickets. 

Key mechanisms include:
- **Lowercasing**: Converting all characters in a string to lowercase to ensure uniformity when comparing strings.
- **Substring Search**: Checking if one string exists within another, which is essential for identifying keywords in ticket texts.

#### 💻 Syntax & Practical Examples (50%)
* **Language Syntax**:
  ```python
  # Example of converting a string to lowercase
  text = "Payment issue"
  lower_text = text.lower()  # Result: "payment issue"

  # Example of checking for a keyword
  if "payment" in lower_text:
      print("Keyword found!")
  ```

* **Real-World Application**:
  ```python
  def keyword_match(text: str, keyword: str) -> bool:
      # Convert both text and keyword to lowercase for case-insensitive matching
      return keyword.lower() in text.lower()

  # Example usage
  ticket_subject = "Payment Issue"
  print(keyword_match(ticket_subject, "payment"))  # Output: True
  ```

---

## 3. Step-by-Step Logic & Walkthrough

1. **Step 1: Locate and Analyze the Target File**
   * Navigate to the `ticketClassifier.py` file within the `s-w08-task-03` folder. This file contains the logic for classifying tickets based on keywords.
   * Focus on the `_match_team` and `_score_priority` methods, as these are where the bugs are located.

2. **Step 2: Input Verification & Validation**
   * Check for edge cases, such as empty strings or null values in the `subject` and `body` parameters. Ensure that the system can handle these gracefully without crashing.

3. **Step 3: Core Implementation / Modification**
   * Modify the `_match_team` method to implement case-insensitive keyword matching. Use the `lower()` method to convert both the text and keywords to lowercase before comparison.
   * Adjust the `_score_priority` method to ensure that the priority weights are correctly assigned, ensuring that critical keywords score higher than low-priority ones.

4. **Step 4: Output Verification & Testing**
   * After making the changes, run the unit tests located in `test_ticketClassifier.py` to verify that all tests pass. Ensure that the modifications do not break existing functionality.

---

## 4. Detailed Walkthrough of Test Cases

### Test Case 1: Standard / Success Case
* **Description**: This test checks if a ticket with a subject containing "Payment issue" is correctly classified under the billing team.
* **Inputs**:
  ```json
  {
    "subject": "Payment issue",
    "body": "I have a problem with my invoice."
  }
  ```
* **Step-by-Step Execution Trace**:
  1. The `classify` method receives the input values.
  2. The `_match_team` method processes the text, converting it to lowercase and checking for the keyword "payment."
  3. The keyword is found, and the team is classified as "billing."
  4. The final classification is returned, indicating the team and priority.

* **Expected Output**: 
  ```json
  {
    "team": "billing",
    "priority": "medium",
    "confidence": 1
  }
  ```

### Test Case 2: Edge Case / Validation Fail
* **Description**: This test checks how the system handles an empty input for the subject and body.
* **Inputs**:
  ```json
  {
    "subject": "",
    "body": ""
  }
  ```
* **Step-by-Step Execution Trace**:
  1. The `classify` method receives the empty input values.
  2. The `_match_team` method processes the text but finds no keywords, resulting in no team being matched.
  3. The execution falls back to the default team "general."
  4. The final classification is returned, indicating the fallback team and a default priority.

* **Expected Output**: 
  ```json
  {
    "team": "general",
    "priority": "medium",
    "confidence": 0
  }
  ```