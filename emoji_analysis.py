import emoji
import matplotlib.pyplot as plt
from collections import Counter

# Step 1: Load chat file
with open("chat2.txt", "r", encoding="utf-8") as f:
    chat_data = f.read()

# Step 2: Extract emojis
def extract_emojis(text):
    return [c for c in text if c in emoji.EMOJI_DATA]

all_emojis = extract_emojis(chat_data)

# Step 3: Count emojis
emoji_counts = Counter(all_emojis)
top_emojis = emoji_counts.most_common(5)

# Print results
print("Top 5 Emojis:")
for emo, count in top_emojis:
    print(f"{emo} : {count}")

# Step 4: Visualization
if top_emojis:
    emojis, counts = zip(*top_emojis)

    # Bar chart
    plt.bar(emojis, counts)
    plt.title("Top 5 Emojis in Chat")
    plt.xlabel("Emoji")
    plt.ylabel("Count")
    plt.show()

    # Pie chart
    plt.pie(counts, labels=emojis, autopct='%1.1f%%')
    plt.title("Emoji Usage Percentage")
    plt.show()
else:
    print("No emojis found in chat.txt")
