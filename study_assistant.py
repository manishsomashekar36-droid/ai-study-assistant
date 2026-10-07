print("🤖 AI Student Study Assistant")
print("=" * 40)

topic = input("Enter the topic you want to study: ")
difficulty = input("Enter difficulty (Easy/Medium/Hard): ")

print("\n📚 AI Study Assistant")
print("-" * 40)
print("Topic:", topic)
print("Difficulty:", difficulty)

print("\n🧠 Recommended Study Plan:")

if difficulty.lower() == "easy":
    print("1. Learn the basic concepts.")
    print("2. Read simple examples.")
    print("3. Practice 5 basic questions.")

elif difficulty.lower() == "medium":
    print("1. Review the fundamentals.")
    print("2. Study important concepts and examples.")
    print("3. Practice 10 questions.")
    print("4. Try a small practical problem.")

elif difficulty.lower() == "hard":
    print("1. Review advanced concepts.")
    print("2. Study real-world applications.")
    print("3. Solve challenging problems.")
    print("4. Build a small project.")
    print("5. Test your understanding without notes.")

else:
    print("Please enter Easy, Medium, or Hard.")

print("\n💡 AI Tip:")
print(f"Spend at least 30 minutes practicing {topic} today.")

print("\n✅ Keep learning and improving!")
