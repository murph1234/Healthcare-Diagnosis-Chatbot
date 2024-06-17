# Healthcare Diagnosis Chatbot
# Architecture Diagram
![image](https://github.com/murph1234/Healthcare-Diagnosis-Chatbot/assets/98601458/211324dc-6ee5-485a-a395-86383733fd68)
# Snaps from the Website
![image](https://github.com/murph1234/Healthcare-Diagnosis-Chatbot/assets/98601458/2ebfed77-37d1-4b19-abd1-8a6f3068a8aa)

# Video description of the website
https://drive.google.com/file/d/15EnjcUKmwZq4ydldfE9FCiuZYPPgpQ_P/view?usp=sharing

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/murph1234/Healthcare-Diagnosis-Chatbot.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mchatbot python=3.8 -y
```

```bash
conda activate mchatbot
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

```


### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

```bash
# run the following command
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:8080
```


### Techstack Used:

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone


