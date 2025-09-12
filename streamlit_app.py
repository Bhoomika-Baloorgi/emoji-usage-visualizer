# streamlit_app.py
import streamlit as st
import re
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import emoji

st.set_page_config(page_title="Emoji Miner", layout="centered")

st.title("Emoji Miner — Chat Emoji Analysis")
st.write("Upload a WhatsApp/Telegram chat export (.txt) or a cleaned text file to analyze emoji usage.")

# Sidebar controls
st.sidebar.header("Settings")
top_n = st.sidebar.slider("Show top N emojis", min_value=1, max_value=30, value=5)
show_examples = st.sidebar.checkbox("Show sample messages for selected emoji", value=True)

uploaded = st.file_uploader("Upload chat export (.txt)", type=["txt"])

def extract_messages(text):
    """Try to strip common WhatsApp/Telegram timestamp + name prefixes, keep the message text."""
    lines = text.splitlines()
    messages = []
    # A forgiving regex that removes common prefixes like:
    # "12/09/2025, 18:30 - Name: message" or "2025-09-12 18:30 - Name: message"
    prefix_re = re.compile(r'^\[?\d{1,4}[-/\.]\d{1,2}[-/\.]\d{1,4}.*?[-–]\s*')  # remove leading timestamp part
    for line in lines:
        if not line.strip():
            continue
        no_prefix = prefix_re.sub('', line).strip()
        # Remove "Name: " at start if present
        no_name = re.sub(r'^[^:]{1,40}:\s+', '', no_prefix)
        if no_name:
            messages.append(no_name)
    return messages

def extract_emojis_from_text(s):
    """Use emoji.emoji_list if available; fall back to a basic regex if none found."""
    try:
        # emoji.emoji_list returns list of dicts like {'emoji': '😂', 'match_start': 12}
        found = emoji.emoji_list(s)
        return [d['emoji'] for d in found]
    except Exception:
        # fallback simple regex for common emoji ranges
        emoji_pattern = re.compile(
            "[" 
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F1E0-\U0001F1FF"  # flags (iOS)
            "\U00002700-\U000027BF"  # dingbats
            "]+", flags=re.UNICODE)
        return emoji_pattern.findall(s)

if uploaded:
    raw = uploaded.read().decode('utf-8', errors='ignore')
    messages = extract_messages(raw)
    st.success(f"Loaded {len(messages)} message lines (after cleaning).")

    # collect emojis
    all_emojis = []
    for m in messages:
        all_emojis.extend(extract_emojis_from_text(m))

    if not all_emojis:
        st.warning("No emojis found in the uploaded file. Try a different chat export or a file with emoji-containing lines.")
    else:
        counts = Counter(all_emojis)
        most = counts.most_common(top_n)
        df = pd.DataFrame(most, columns=["emoji", "count"])
        st.subheader("Top emojis")
        st.table(df)

        # Bar chart
        fig, ax = plt.subplots()
        ax.bar(df["emoji"].astype(str), df["count"])
        ax.set_xlabel("")
        ax.set_ylabel("Count")
        ax.set_title("Top emojis in chat")
        st.pyplot(fig)

        # Download CSV
        csv_bytes = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download counts as CSV", csv_bytes, file_name="emoji_counts.csv", mime="text/csv")

        # Show sample messages for one selected emoji
        if show_examples:
            emoji_choice = st.selectbox("Show sample messages containing:", options=[e for e,_ in most])
            if emoji_choice:
                samples = [m for m in messages if emoji_choice in m]
                st.write(f"Found {len(samples)} messages containing {emoji_choice}.")
                for s in samples[:10]:
                    st.write("- " + s)
else:
    st.info("Upload a chat `.txt` file on the left to start analysis.")
