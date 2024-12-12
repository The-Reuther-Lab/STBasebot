############################################################################################################
# Importing Libraries

import streamlit as st
import hmac
import config
from openai import OpenAI

############################################################################################################
# Password protection

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

############################################################################################################
# Streamlit app layout

# Set the page to wide or centered mode
st.set_page_config(layout="wide", 
                   page_title="Modular Chatbot",
                   page_icon=":lightbulb:",
                   initial_sidebar_state="collapsed"
                   )

# Streamlit app layout
# st.title(config.app_title)
# with st.expander("INSTRUCTIONS FOR STUDENTS:"):
#     st.markdown(config.instructions)

############################################################################################################


# Define a basic initial context at the beginning of your script
initial_context = {
    "role": "system",
    "content": config.prompt
}

# Initialize the OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Initialize the session state variables if they don't exist
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = config.ai_model

# Corrected initialization of display_messages:
if "display_messages" not in st.session_state:
    st.session_state["display_messages"] = [initial_context] 

# Get user input
prompt = st.chat_input("Type your message here...")

# Input for new messages
if prompt:
    # Ensure initial context is in the session state and then append user messages
    if not st.session_state["display_messages"]:
        st.session_state["display_messages"] = [initial_context]
    st.session_state["display_messages"].append({"role": "user", "content": prompt})

# Function to reset all chat-related session state
def reset_chat_history():
    st.session_state["display_messages"] = [initial_context]
    st.rerun()

# Main chat container
with st.container(border=False):
    # Display chat history in reverse order including new messages
    for message in st.session_state["display_messages"][1:]:
        if message["role"] == "user":
            with st.chat_message("user"):
                st.markdown(message["content"])
        else:
            with st.chat_message("assistant"):
                st.markdown(message["content"])

# Generate assistant's response and add it to the messages
    if prompt:
        with st.chat_message("assistant"):
            try:
                stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state["display_messages"]
                    ],
                    stream=True,
                    temperature=config.temperature,
                    max_tokens=config.max_tokens,
                    frequency_penalty=config.frequency_penalty,
                    presence_penalty=config.presence_penalty,
                )
                
                # Initialize an empty string to store the full response
                full_response = ""
                message_placeholder = st.empty()
                
                # Iterate through the stream to get each chunk
                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")
                
                # Replace the placeholder with the complete message
                message_placeholder.markdown(full_response)
                
                # Append the full response to the session state for display
                st.session_state["display_messages"].append(
                    {"role": "assistant", "content": full_response}
                )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Create a sidebar
with st.sidebar:
    st.markdown(config.warning_message, unsafe_allow_html=True)

    # Add Clear Chat History button to sidebar
    if st.button("Clear Chat History"):
        reset_chat_history()
    
    # Add license link with markdown
    st.markdown("---")  # Separator line
    st.markdown("""
        <small>Licensed under [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)</small>
        """, unsafe_allow_html=True)