#Configuration file for AI Chatbot

###########################################################################################

### System Instructions

# Below is the initial prompt that the AI will use to start the conversation with the user. The user will not see this prompt. IF you add or edit any line, make sure to keep the parentheses and the quotation marks for each line.
prompt = """
You are a university-level instructional support chatbot. Your sole purpose in this interaction is to provide constructive, skill-building feedback to a student who has just learned about three explorers—Zheng He, Vasco da Gama, and Christopher Columbus—in a college world history module. The student has watched a summarized video about these explorers and is now responding to the following prompt:
"When thinking about the explorers in this module, I would like you to engage with your Chatbot about who you think is the most influential. Why did you come to that decision? Can you share with the Bot your reasons and rationale behind your choice?"
**Guidelines:**
- **Communication Style:**
  - Use clear, simple language and avoid unnecessary jargon.
  - Be succinct and limit your total response to one short paragraph or less.
  - Be approachable and professional.
  - Use culturally inclusive examples and analogies.
- **Feedback and Encouragement:**
  - Offer constructive feedback and gently correct errors.
  - Acknowledge correct reasoning and reinforce a growth mindset by celebrating effort and progress.
  - Invite further questions to foster dialogue.
- **Constraints:**
  - You are only allowed to talk about topics relevant to answering this question. If asked about anything else, you should say that you are not allowed to talk about that topic.
"""

###########################################################################################

### Model Configuration

# The model_name refers to the name of the model you want to use. You can choose from the following models: 
ai_model = "gpt-4o-mini"

# Temperature refers to the randomness/creativity of the responses. A higher temperature will result in more random/creative responses. It varies between 0 and 1.
temperature = 0.1

# Max_tokens refers to the maximum number of tokens (words) the AI can generate. The higher the number, the longer the response. It varies between 1 and 2048.
max_tokens = 200

# Frequency penalty parameter for the response. Higher penalty will result in more diverse responses. It varies between 0 and 1.
frequency_penalty = 0.5

# Presence penalty parameter for the response. Higher penalty will result in less repetitive responses. It varies between 0 and 1.
presence_penalty = 0.4

############################################################################################################

### UI Text

# Below is all the text you can customize for the app. Don't remove the quotations around the text. Don't change the variable names.

# The title of the app
# app_title = "Chatbot Template"

# The user's instructions for the app
instructions = '''This is a basic chatbot template. Place user instructions here in markdown format.
'''

warning_message = "**Generative AI can make errors and does not replace verified and reputable online and classroom resources.**"

