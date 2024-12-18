# story-generator
Generating story automatically after some specific time span.

Linux users

clone the repository
go to the directory
cd story-generator 

code . this is used to open the folder in visual studio
#Steps For Virtual Environment 

create a virtual environment called venv_name

The command below will create a new folder called venv_name

python -m venv venv_name

NOTE: the virtual environment name can be anything (like banana). However, it is common practice to use just venv. This is handy when copying/pasting code snippets.

Hence, use the following command:

  python -m venv venv
NOTE: a message will appear (bottom right) asking to use the new environment, click 'Yes'.

Alternatively, choose from the list of environments (bottom left). The Python version should be listed with venv in parentheses, e.g.
 Python 3.9.1 64-bit ('venv')

 use the following command source .venv/bin/activate

 now run the file using 
python main.py
 
#Steps to run project using Docker

Installation Clone the Repository:

bash Copy code git clone https://github.com/Maria-cpp/story-generator.git cd chatbot Build the Docker Image:

bash Copy code docker build -t story-image . Run the Docker Container:

bash Copy code docker run -d -p 7860:7860 --name chatbot-container story-image Usage Once the Docker container is up and running, you can interact with the chatbot via its API or web interface:

Web Interface: Open a web browser and go to http://localhost:7860 to use the web interface Configuration You can customize the chatbot by modifying the configuration file config.yaml.