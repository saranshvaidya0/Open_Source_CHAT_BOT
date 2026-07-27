# 🤖 Open Source Chat Bot

A simple and beginner-friendly AI chatbot built with **Python, Streamlit, and Groq API**. This project demonstrates how to create and deploy an AI-powered chatbot using a clean and easy-to-understand implementation.

## 🚀 Live Demo

Try the chatbot online:

👉 **[Open Live Demo](https://openchatbotofsaransh.streamlit.app/)**

---

## 📌 About the Project

**Open Source Chat Bot** is a lightweight AI chatbot application designed to provide a simple interface for interacting with an AI model.

The application is built using **Streamlit** for the user interface and the **Groq API** for AI-powered responses.

The goal of this project is to provide a simple starting point for developers and students who want to learn how to build and deploy an AI chatbot.

---

## ✨ Features

* 🤖 AI-powered chatbot
* 💬 Simple and interactive chat interface
* ⚡ Fast AI responses using Groq API
* 🖥️ Built with Streamlit
* 🔐 Secure API key configuration using environment variables
* 🌐 Deployed using Streamlit Community Cloud
* 📱 Easy-to-use web interface
* 🧑‍💻 Beginner-friendly project structure

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Groq API**
* **python-dotenv**

---

## 📂 Project Structure

```text
Open_Source_CHAT_BOT/
│
├── .devcontainer/
│   └── ...
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/saranshvaidya0/Open_Source_CHAT_BOT.git
```

### 2. Navigate to the Project Directory

```bash
cd Open_Source_CHAT_BOT
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Add Your Groq API Key

Create a `.env` file in the root directory:

```text
GROQ_API_KEY=your_groq_api_key_here
```

> ⚠️ Never upload your `.env` file or your API key to GitHub.

### 6. Run the Application

Start the Streamlit application with:

```bash
streamlit run streamlit_app.py
```

The application will open in your browser.

---

## 🔑 Environment Variable

The application requires one API key:

| Variable       | Description                         |
| -------------- | ----------------------------------- |
| `GROQ_API_KEY` | API key used to access the Groq API |

For local development, store the key in a `.env` file.

For Streamlit Community Cloud deployment, add the key through **App Settings → Secrets**.

Example:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

---

## 🌐 Deployment

This project is deployed using **Streamlit Community Cloud**.

### Live Application

👉 **https://openchatbotofsaransh.streamlit.app/**

You can use the live application without installing anything locally.

---

## 📋 Requirements

The main Python dependencies are:

```text
streamlit
groq
python-dotenv
```

These dependencies are listed in `requirements.txt`.

---

## 🎯 Project Purpose

This project was created as a simple example for learning how to:

* Build an AI-powered application with Python
* Create an interactive UI using Streamlit
* Connect an application to the Groq API
* Manage API keys securely
* Deploy an AI application online
* Share an AI project through GitHub

---

## 🔮 Future Improvements

Possible future enhancements include:

* 💾 Persistent conversation history
* 🎨 Improved chatbot UI
* 🧠 Support for multiple AI models
* 📄 Chat export functionality
* 🔊 Voice input and output
* 🌍 Multilingual chatbot support
* 👤 User authentication
* 📊 Conversation analytics

---

## 🤝 Contributing

Contributions are welcome!

If you would like to improve this project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Open a Pull Request

---

## 📜 License

This project is open source and available for learning, development, and personal use.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**GitHub Repository:**
https://github.com/saranshvaidya0/Open_Source_CHAT_BOT

**Live Demo:**
https://openchatbotofsaransh.streamlit.app/

---

### 👨‍💻 Author

**Saransh Vaidya**

Built with ❤️ using Python, Streamlit, and Groq.
