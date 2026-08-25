import config
from ollama import chat


## Intro: Project Athena. Verson 0.0.1 initialising...


print("=======================================")
print("=== Project " + config.APP_NAME + "                  ===")
print("=== Version: " + config.APP_VERSION + " initialising..." + " ===")
print("=== Author: " + config.AUTHOR + "                 ===")
print("=======================================")

running = True





while running:

    ## Stage 1: Ask opening question on launch.
    question = input("What is your question?")

    ## Get input 
    response = chat(
    model=config.LLM_MODEL, messages=[
        {
            "role": "user",
            "content": question
        }
    ],

    ## Stop qwen from thinking. Speeds response time.
    think=False
    )
    print(response.message.content)


