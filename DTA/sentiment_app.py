import streamlit as st
import re
from textblob import TextBlob

# Text cleaning function (same as in the notebook)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# Streamlit app
def main():
    st.title("📝 Text Sentiment Analysis")
    st.markdown("Enter your text below to analyze its sentiment!")

    # Text input
    user_input = st.text_area("Enter your text:", height=100, placeholder="Type your text here...")

    if st.button("Analyze Sentiment", type="primary"):
        if user_input.strip():
            # Clean the text
            cleaned_text = clean_text(user_input)

            # Perform sentiment analysis
            analysis = TextBlob(cleaned_text)

            # Display results
            st.subheader("📊 Analysis Results")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Original Text:**")
                st.write(user_input)

            with col2:
                st.markdown("**Cleaned Text:**")
                st.write(cleaned_text)

            # Sentiment result
            st.markdown("---")
            st.subheader("🎯 Sentiment Analysis")

            polarity = analysis.sentiment.polarity

            if polarity > 0:
                sentiment = "Positive 😊"
                color = "green"
            elif polarity < 0:
                sentiment = "Negative 😞"
                color = "red"
            else:
                sentiment = "Neutral 😐"
                color = "blue"

            st.markdown(f"<h2 style='color: {color}; text-align: center;'>{sentiment}</h2>", unsafe_allow_html=True)

            # Detailed metrics
            st.markdown("**Detailed Metrics:**")
            col3, col4 = st.columns(2)

            with col3:
                st.metric("Polarity Score", f"{polarity:.3f}")

            with col4:
                subjectivity = analysis.sentiment.subjectivity
                st.metric("Subjectivity", f"{subjectivity:.3f}")

            # Progress bar for polarity
            st.markdown("**Polarity Visualization:**")
            if polarity >= -1 and polarity <= 1:
                # Normalize to 0-100 range for progress bar
                normalized_polarity = ((polarity + 1) / 2) * 100
                st.progress(normalized_polarity / 100)
                st.caption(f"Polarity ranges from -1 (very negative) to +1 (very positive). Current: {polarity:.3f}")

        else:
            st.warning("Please enter some text to analyze!")

    # Footer
    st.markdown("---")
    st.markdown("*Built with Streamlit and TextBlob*")

if __name__ == "__main__":
    main()