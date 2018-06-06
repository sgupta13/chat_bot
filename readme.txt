readme.txt
----------
1) Install python 3.6
2) Install Anaconda 3
3) Use Jupyter notebook as editor and interpreter
4) Install rasa_nlu and other required libraries using the anaconda command prompt:

   pip install rasa_nlu
   pip install -r requirements_full.txt
   pip install -e .

5) Set up the processing pipeline for rasa_nlu by spaCY and sklearn, by executing the following commands from anaconda prompt:
   
   pip install rasa_nlu[spacy]
   python -m spacy download en_core_web_md

   Create a link for loading spaCY by using below command, please note that below command should be executed by running anaconda prompt as administrator:

   python -m spacy link en_core_web_md en

6) Put the GSUCSBot in rasa_nlu folder to make sure that the libraries are accessible to the modules.

7) Change directory to GSUCSBot on anaconda command prompt and run the following command to train the model:

   python -m rasa_nlu.train -c config.json

8) Run the following command to start the server:

   python -m rasa_nlu.server -c config.json -e luis

9) The server will start at port number 5000, to check if the server is running properly or not, open IE (Internet Explorer) browser window, and run the    following command:

   http://localhost:5000/parse?q=chair-person
   
   This command will display show the intent and the intent scores.

10) In anaconda command prompt, in directory GSUCSBot, execute the following command to start client:
   
    python client.py

11) The client will start running on port number 8080, to check if the client is running properly, open IE (Internet Explorer) browser window, and run the       following command:

    http://localhost:8080/

12) Start communicating with chatbot in the client chat window.


   