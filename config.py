#Configuration file for AI Chatbot

###########################################################################################

### System Instructions

# Below is the initial prompt that the AI will use to start the conversation with the user. The user will not see this prompt. IF you add or edit any line, make sure to keep the parentheses and the quotation marks for each line.
prompt = """
**Course Learning Assistant Instructions for General Biology**: As a learning assistant, help students grasp fundamental biology concepts by encouraging thoughtful inquiry, guiding them toward reliable scientific sources, and fostering independent problem-solving skills. Communicate respectfully, clarify misconceptions, maintain academic integrity, and highlight connections between classroom material and real-world biological applications.
"""

###########################################################################################

### Model Configuration

# The model_name refers to the name of the model you want to use. You can choose from the following models: 
ai_model = "gpt-4o-mini"

# Temperature refers to the randomness/creativity of the responses. A higher temperature will result in more random/creative responses. It varies between 0 and 1.
temperature = 0.1

# Max_tokens refers to the maximum number of tokens (words) the AI can generate. The higher the number, the longer the response. It varies between 1 and 2048.
max_tokens = 1000

# Frequency penalty parameter for the response. Higher penalty will result in more diverse responses. It varies between 0 and 1.
frequency_penalty = 0.5

# Presence penalty parameter for the response. Higher penalty will result in less repetitive responses. It varies between 0 and 1.
presence_penalty = 0.4

############################################################################################################

### UI Text

# Below is all the text you can customize for the app. Don't remove the quotations around the text. Don't change the variable names.

# The title of the app
app_title = "Biology Chatbot Template"

# The subtitle of the app
app_author = "by Keefe Reuther, Assistant Teaching Professor in the UC San Diego School of Biological Sciences"

# The user's instructions for the app
instructions = '''This is a basic chatbot template. Place user instructions here in markdown format.
'''

app_creation_message = "This app, its corresponding manuscript, and all documentation was authored, edited, and tested by Keefe Reuther and the members of the Reuther Lab - [https://reutherlab.biosci.ucsd.edu/](https://reutherlab.netlify.app/)"

app_repo_license_message = "It can be found at [https://github.com/The-Reuther-Lab/schema_study](https://github.com/The-Reuther-Lab/schema_study) and is distributed under the GNU GPL-3 License. If you are interested in creating your own version of this application for use in your classroom, please email kdreuther@ucsd.edu for more information."

warning_message = "**Generative AI can make errors and does not replace verified and reputable online and classroom resources.**"

