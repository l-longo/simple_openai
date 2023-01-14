import openai
import streamlit as st

# Apply your own API key
openai.api_key = "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"

title = st.text_input('Ask me something', 'Who is the best football player of all the times?')

prompt = (title)

completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)

message = completions.choices[0].text
print(message)

st.write(message)
