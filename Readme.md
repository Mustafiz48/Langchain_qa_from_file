
# Langchain qa from file with openai 

This is a project to build a question answering application that can create knowledgebase from a given text file, generates embeddings and then using openai api, answer questions like Chat-GPT about that from that text.   

## Install Dependencies
First thing you need to do is to install required packages. Run the following command from terminal 

```
pip install -r requirements.txt
```
It will isntall required packages in your environment

## OpenAI API Key
Second thing you need to do is to create a ```.env``` file in same folder with main.py file. Inside the file, keep your openai api key as follows
```
OPEN_AI_API_KEY = "your api key here"
```
## Set the url and domain url
One last thing to is to set the path of the text file that you want to analyze. In ```main.py``` file, update "text_path" variable according to your text file path. 

## Run the application
Now you are good to go! Just run the main.py file from terminal. It will ask you for a question. Ask a question, it will generate answer based on the data from the text file. Note that, for the first time when you run the app, it will load the text file and create embedding. This may take some time based on the text file. 