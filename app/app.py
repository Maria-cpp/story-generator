import time
import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAsd9AE90gxmyHsrziKLl_7MxTCJLWWWMQ")
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Initialize dictionary


# Function to get random words
def generate_random_words(num_words):
    response = model.generate_content(f"Generate {num_words} random words for creative story writing")
    cleaned_words = [line.split(".")[1].strip() for line in response.text.split("\n") if line.strip()]

    # Convert the list into a string
    result = f"[{', '.join(cleaned_words)}]"
    return result


if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

#Display Form title 
st.title("Random Story Generator")


def role_to_streamlit(role):
     if role == "model":
          return "assistant"
     else:
          return role

for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)
        
prompt = st.chat_input("What can I do for you?")
prompt = "Story"
while True:  # Infinite loop until user explicitly stops
   
    if prompt:  # Check if user entered something
        st.chat_message("user").markdown(prompt)

        # Generate random words
        words = generate_random_words(5)
        prompt = f"Generate story using words {words}"
        st.chat_message("user").markdown(prompt)

        # Send request to Gemini for story generation (replace with your API call)
        response = st.session_state.chat.send_message(prompt)

        with st.chat_message("assistant"):
            st.markdown(response.text)

        if prompt.lower() == "stop":  # Allow user to stop the loop
            break

    time.sleep(30)

st.stop()


# Function to generate a story using the random words
# def generate_story(words):
    
#     story = f"Once upon a time, {', '.join(words[:-1])}, and {words[-1]} found themselves on an extraordinary adventure..."
#     return story

# Streamlit UI
# st.title("Story Generator Chatbot")
# st.write("Generate creative stories from random words!")

# # Input for number of words
# num_words = st.slider("Number of random words:", 3, 10, 5)

# if st.button("Generate Random Words"):
#     random_words = generated_random_word
#     st.write("Random Words:", random_words)

#     if st.button("Generate Story"):
#         story = generate_story(random_words)
#         st.subheader("Your Story:")
#         st.write(story)