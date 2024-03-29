import streamlit as st
import openai
# Set your OpenAI API key
openai.api_key = ''


def detect_bugs(code):
   try:
       response = openai.ChatCompletion.create(
           model="gpt-4",
           messages=[
               {"role": "system", "content": "You are a helpful assistant specialized in programming and code review."},
               {"role": "user", "content": f"Please analyze this Python code for potential bugs and vulnerabilities:\n\n{code}"}
           ],
           max_tokens=850
       )
       # Extracting and formatting the response
       if response.choices and response.choices[0].message:
           analysis_result = response.choices[0].message['content'].strip()
           return analysis_result
       else:
           return "No response from the model."
   except Exception as e:
       return str(e)

def generate_code(description):
   try:
       response = openai.ChatCompletion.create(
           model="gpt-4",
           messages=[
               {"role": "system", "content": "You are a helpful assistant."},
               {"role": "user", "content": f"Generate a code snippet for the following requirement:\n\n{description}"}
           ],
           max_tokens=500
       )
       return response.choices[0].message['content'].strip()
   except Exception as e:
       return str(e)

def summarize_documentation(doc_text):
   try:
       response = openai.ChatCompletion.create(
           model="gpt-4",
           messages=[
               {"role": "system", "content": "You are a helpful assistant."},
               {"role": "user", "content": f"Summarize the following technical documentation or code comments:\n\n{doc_text}"}
           ],
           max_tokens=500
       )
       return response.choices[0].message['content'].strip()
   except Exception as e:
       return str(e)
   
   # Function to handle code migration (stub for actual implementation)
# Function to handle code migration (stub for actual implementation)
def migrate_code(source_code, source_lang, target_lang):
   # Constructing the prompt for the AI
   response = openai.ChatCompletion.create(
       model="gpt-4",
       messages=[
               {"role": "system", "content": "You are a helpful assistant."},
               {"role": "user", "content": f"Translate this {source_lang} code to {target_lang}:\n\n{source_code}\n\n"}
           ],

       max_tokens=500
   )
   # Extracting the response
   migrated_code = response.choices[0].message['content'].strip()
   return migrated_code

def generate_test_cases(codebase):
   try:
       response = openai.ChatCompletion.create(
           model="gpt-4",
           messages=[
               {"role": "system", "content": "You are a helpful assistant."},
               {"role": "user", "content": f"Generate test cases and scenarios for the following codebase:\n\n{codebase}"}
           ],
           
           max_tokens=500
       )
       return response.choices[0].message['content'].strip()
   except Exception as e:
       return str(e)
   
def handle_code_chat(user_query):
   try:
       response = openai.ChatCompletion.create(
           model="gpt-4",
           messages=[
               {"role": "system", "content": "You are a helpful assistant specialized in programming and code-related queries."},
               {"role": "user", "content": user_query}
           ],
           
           max_tokens=500
       )
       # Extracting and formatting the response
       if response.choices and response.choices[0].message:
           chat_response = response.choices[0].message['content'].strip()
           return chat_response
       else:
           return "No response from the model."
   except Exception as e:
       return str(e) 


def generate_code(partial_code):
   try:
       # Constructing the prompt for code completion
       prompt = f"Here is a partial code snippet:\n\n{partial_code}\n\nComplete this code:"
       response = openai.ChatCompletion.create(
           model="gpt-4",
           messages=[
               {"role": "system", "content": "You are a helpful assistant."},
               {"role": "user", "content": prompt}
           ],
            # You can adjust this for more creativity or conservativeness in responses
           max_tokens=500  # Adjust as needed based on the average length of completions
       )
       # Extracting and formatting the response
       if response.choices and response.choices[0].message:
           completed_code = response.choices[0].message['content'].strip()
           return completed_code
       else:
           return "No completion generated."
   except Exception as e:
       return str(e)  
   
# Define your functions (detect_bugs, generate_code, etc.)
# Streamlit app interface
st.title('SDLC Enhancement with GENAI')
st.write("""
         ***Explore how GENAI transforms various stages of the Software Development Life Cycle including***
         - Code Generation
         - Bug Detection
         - Technical documentation summarization
         - Automated Testing
         - Code Migration
         """)



#st.sidebar.title('Choose a functionality')
option = st.sidebar.selectbox(
   '',
   ('Select...', 'Code Generation', 'Bug Detection', 'Summarize Technical Documentation and Code Comments', 'Automated Testing', 'Code Migration')
)

# Based on the option chosen, display the corresponding functionality
# Main page title and description
if option == 'Code Generation':  # Default view
   
   st.header('Code Generation')
   # Descriptive text with bullet points for Code Generation
   st.write("""
       - GENAI significantly speeds up the development process by generating code snippets and entire modules quickly. 
       - This reduces the time developers spend on routine coding tasks, allowing them to focus on more complex and creative aspects of software development.
   """)

   st.subheader("Generate Code Snippets")

   user_input_gen = st.text_input("Describe the functionality for which you need code:")
   if st.button('Generate Code', key='generate'):
       if user_input_gen:
           generated_code = generate_code(user_input_gen)
           st.write('Generated Code Snippet:')
           st.code(generated_code)
       else:
           st.warning('Please enter a description for code generation.')
   
   code_option = st.sidebar.selectbox(
       '',
       ('Select...','Code Chat', 'Code Completions')
   )
   if code_option == 'Code Chat':
       st.subheader("Code Chat")
       # Using columns for layout
       col1, col2 = st.columns(2)
       with col1:
           user_code = st.text_area("Paste your code here:", height=300)
       with col2:
           user_input_chat = st.text_area("Ask your question about the code:", height=300)
       if st.button('Generate Response', key='chat'):
           if user_code and user_input_chat:
               # Combine code and question for the chat response
               combined_input = f"Code:\n{user_code}\nQuestion:\n{user_input_chat}"
               chat_response = handle_code_chat(combined_input)
               st.write('Response:')
               st.write(chat_response)
           else:
               st.warning('Please enter both code and a question for code chat.')

   if code_option == 'Code Completions':
       st.subheader("Code Completions")
       # Using columns for layout
       col1, col2 = st.columns(2)
       with col1:
           user_input_code = st.text_area("Paste your partial code here:", height=300)
       with col2:
           # Placeholder for completed code
           completed_code_placeholder = st.empty()
       if st.button('Complete Code', key='complete'):
           if user_input_code:
               # Generate completed code
               completed_code = generate_code(user_input_code)
               # Display completed code in the second text box
               completed_code_placeholder.text_area("Completed Code:", completed_code, height=300)
           else:
               st.warning('Please enter some code to complete.')

    
               
   

   
elif option == 'Bug Detection':
   
   st.header('Bug Detection')
   st.write("""
       - GENAI significantly speeds up the process of identifying bugs by quickly analyzing code and pinpointing potential errors, which might be overlooked by human developers.
       - Generative AI can identify potential bugs or vulnerabilities. It effectively flags problematic code sections, highlights potential errors, and suggests improvements based on insights garnered from previous projects. This significantly reduces the time spent on manual code review and debugging.
   """)
   st.subheader("Detect Bugs in Your Code")
   user_input_bug = st.text_area("Enter your code here for bug detection:", height=300)
   if st.button('Detect Bugs', key='detect'):
       if user_input_bug:
           results = detect_bugs(user_input_bug)
           st.write('Detected Bugs and Vulnerabilities:')
           st.write(results)
       else:
           st.warning('Please input some code to analyze.')
   # Rest of the bug detection functionality
elif option == 'Summarize Technical Documentation and Code Comments':
   
   st.header('Summarize Technical Documentation and Code Comments')
   st.write("""
       - Generative AI, powered by natural language processing techniques, can understand and summarize technical documentation and code comments. It generates concise and accurate summaries, making it easier for developers to comprehend complex codebases and collaborate more effectively. 
   """)

   user_input_doc = st.text_area("Enter documentation or code comments for summarization:", height=300)
   if st.button('Summarize', key='summarize'):
       if user_input_doc:
           summary = summarize_documentation(user_input_doc)
           st.write('Summary of Documentation/Comments:')
           st.write(summary)
       else:
           st.warning('Please input some documentation or comments to summarize.')

elif option == 'Automated Testing':
    st.subheader("Automated Testing: Generate Test Cases and Scenarios")
    st.write("""
       - Generative AI facilitates the automation of testing procedures by generating test cases and scenarios. By analyzing the codebase and comprehending its behavior, the AI can generate a wide range of test inputs and expected outputs. This enhances test coverage and uncovers potential edge cases that manual testing might overlook.
   """)
   
   
   
    user_input_test = st.text_area("Enter your codebase to generate test cases:", height=300)
    if st.button('Generate Test Cases', key='test'):
       if user_input_test:
           test_cases = generate_test_cases(user_input_test)
           st.write('Generated Test Cases and Scenarios:')
           st.code(test_cases)
       else:
           st.warning('Please input a codebase to generate test cases.')
   # Code for Automated Testing functionality
   
# Code Migration functionality
elif option == 'Code Migration':
   st.header('Code Migration')
   st.write("Migrate code from one programming language to another.")
   # Dropdowns to select source and target languages
   source_lang = st.sidebar.selectbox('Select source language:', ('Python', 'JavaScript', 'Java', 'C++','ABAP'))
   target_lang = st.sidebar.selectbox('Select target language:', ('Python', 'JavaScript', 'Java', 'C++','ABAP'))
   # Text area for user to enter the code they wish to convert
   source_code = st.text_area("Enter the code you want to migrate:", height=300)
   if st.button('Migrate Code'):
       if source_code and (source_lang != target_lang):
           # Call the migrate_code function
           with st.spinner('Translating code...'):
               migrated_code = migrate_code(source_code, source_lang, target_lang)
           st.success('Code migration completed.')
           st.code(migrated_code)
       else:
           st.error('Please enter the code and make sure the source and target languages are different.')
           
