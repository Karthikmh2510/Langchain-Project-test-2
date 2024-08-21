Here, I am creting a ChatBot using open source LLM called gemini model.
I am using Langchain modules to create the project.


In api folder I have created app.py file
This file is responsible to create end-to-end application using langchain, uvicorn, and FastAPI to create the application.
We need to keep changing the port number for every run. Since, 1 port will be asigned for one run.
To run we need to use python app.py command
We need to innstall sse_starlettein order to view this.
I have added 2 routes: 1.Google Gemini for essay, 2. Ollama llama2 for poem.

In api folder I have created client.py file for client side display
This is front-end application side python file.
