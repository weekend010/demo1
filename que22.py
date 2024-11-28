#22

# Given values
TP = 90  # True Positives (cancer=yes, predicted=cancer=yes)
FP = 140  # False Positives (cancer=no, predicted=cancer=yes)
FN = 210  # False Negatives (cancer=yes, predicted=cancer=no)
TN = 9560  # True Negatives (cancer=no, predicted=cancer=no)

# Accuracy
accuracy = (TP + TN) / (TP + TN + FP + FN)

# Error Rate
error_rate = (FP + FN) / (TP + TN + FP + FN)

# Precision
precision = TP / (TP + FP)

# Recall (Sensitivity)
recall = TP / (TP + FN)

# Print results
print(f"Accuracy: {accuracy:.4f}")
print(f"Error Rate: {error_rate:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
