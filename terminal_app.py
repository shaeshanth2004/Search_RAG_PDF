from main import ask

print("--- Starting Application ---")

while True:
    question = input("Enter your question (or type 'exit' to quit): ")
    if question.lower() == 'exit':
        print("Exiting the application.")
        break

    try:
        answer = ask(question)
        print(f"Question: {question}")
        print(f"Answer:\n{answer}")
    except Exception as e:
        print(f"Error: {e}")
print("--- Application Ended ---")