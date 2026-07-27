"""Task 9: Disease Diagnosis Program"""

print("Welcome to Jeshi Hospital")

# Patient details
name = input("Name: ")
gender = input("Gender: ")
age = input("Age: ")
residence = input("Place of residence: ")

symptom1 = input("Symptom 1: ").lower()
symptom2 = input("Symptom 2: ").lower()

pair = {symptom1, symptom2}

if pair == {"fever", "headache"}:
    diagnosis = "Typhoid"
elif pair == {"fever", "chills"}:
    diagnosis = "Malaria"
elif pair == {"cough", "chest pain"}:
    diagnosis = "Pneumonia"
elif pair == {"fatigue", "thirst"}:
    diagnosis = "Diabetes"
else:
    diagnosis = "Unrecognized symptom combination - please consult a doctor"

print("\n--- Diagnosis Report ---")
print(f"Patient: {name}, {gender}, {age}, {residence}")
print(f"Symptoms: {symptom1}, {symptom2}")
print(f"Diagnosis: {diagnosis}")