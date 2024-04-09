# 🤖 RAG LLM-based Chat Bot to Assist with Determining Fine Sum (RU)

### ⚙️ Tech Stack 
- Mistral, ChatGPT, GigaChat, E5
- torch, transformers, clickhouse_connect, nltk
- gradio

1. **Data Handling**: 
   - In `clickhouse/db.ipynb`, the text of the Russian Code of Administrative Offenses (КоАП РФ) is scanned and translated into txt, after which it is loaded into the ClickHouse database.
   
2. **Model Interaction**: 
   - In `inference.ipynb`, interaction with three models is implemented in notebook format: `IlyaGusev/saiga_mistral_7b_gguf`, ChatGPT (3.5 turbo), GigaChat.
   
3. **Graphical User Interface (GUI)**: 
   - In `gui.ipynb`, a graphical interface for communicating with three models is developed.

### 🚀 How to Run the Code 🚀
**For Windows**
1. Register an account on the ngrok official website.
2. Install ngrok.
3. Run `ngrok config add-authtoken <your auth token from ngrok website>`.
4. Run `ngrok http <your free static domain from ngrok> 80`.
5. Launch the server in LM Studio (for Mistral).
6. Create a `.env` file to store GigaChat and OpenAI keys.
7. Launch GUI.
8. Enjoy!

### 📈 Inference Examples 📈

<p align="center">
  <a href="https://ibb.co/p0XkJLb"><img src="https://i.ibb.co/h78TDmL/Screenshot-from-2024-04-09-14-20-59.png" alt="Screenshot-from-2024-04-09-14-20-59" border="0"></a>
</p>

<p align="center">
  <a href="https://ibb.co/9ympjLK"><img src="https://i.ibb.co/5sX1Vyp/Screenshot-from-2024-04-09-14-26-37.png" alt="Screenshot-from-2024-04-09-14-26-37" border="0"></a>
</p>

<p align="center">
  <a href="https://ibb.co/n0NHfky"><img src="https://i.ibb.co/4fn6MNL/Screenshot-from-2024-04-09-14-34-51.png" alt="Screenshot-from-2024-04-09-14-34-51" border="0"></a>
</p>

---
<p align="center">
  <img src="https://pbs.twimg.com/media/Etd-8eoXUAQACOb.jpg" alt="Image">
</p>

