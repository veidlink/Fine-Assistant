# RAG LLM-based Chat Bot to assist with determining fine sum (RU)

1. In `clickhouse/db.ipynb`, the text of the Russian Code of Administrative Offenses (КоАП РФ) is scanned and translated into txt, after which it is loaded into the ClickHouse database.
2. In `inference.ipynb`, interaction with three models is implemented in notebook format: `IlyaGusev/saiga_mistral_7b_gguf`, ChatGPT (3.5 turbo), GigaChat.
3. In `gui.ipynb`, a graphical interface for communicating with three models is developed.

### How to run code
**Windows**
1. Register an account on ngrok official website
2. Install ngrok
4. ```ngrok config add-authtoken <your auth token from ngrok website>```
5. ```ngrok http <your free static domain from ngrok> 80```
6. Launch the server in LM Studio (for Mistral)
7. Create .env file to store GigaChat and OpenAI keys.
8. Launch GUI
9. Enjoy

### Inference Examples

<p align="center">
  <a href="https://ibb.co/p0XkJLb"><img src="https://i.ibb.co/h78TDmL/Screenshot-from-2024-04-09-14-20-59.png" alt="Screenshot-from-2024-04-09-14-20-59" border="0"></a>
</p>

<p align="center">
  <a href="https://ibb.co/9ympjLK"><img src="https://i.ibb.co/5sX1Vyp/Screenshot-from-2024-04-09-14-26-37.png" alt="Screenshot-from-2024-04-09-14-26-37" border="0"></a>
</p>

<p align="center">
  <a href="https://ibb.co/n0NHfky"><img src="https://i.ibb.co/4fn6MNL/Screenshot-from-2024-04-09-14-34-51.png" alt="Screenshot-from-2024-04-09-14-34-51" border="0"></a>
</p>

