ENTRY = "I'm on vacation until Monday. My auto-reply is now a smaller, cheaper model that will tell you 'great question' and then hallucinate the answer."
assert ENTRY.count("\n") == 0 and len(ENTRY) <= 160

print(ENTRY)
