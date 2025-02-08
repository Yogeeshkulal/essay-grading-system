
# **Automated Essay Grading System**  

This project is a **Flask-based web application** that allows users to upload formal letters (in `.txt` or `.pdf` format). The system uses **OpenAI's GPT API** to evaluate the letter and provide a grade along with suggestions for improvement.  

---

## **Features**  
✅ Upload `.txt` or `.pdf` files for grading  
✅ Uses **OpenAI GPT-3.5** to evaluate letters based on structure, grammar, and tone  
✅ Provides **grades (A, B, C, etc.)** with improvement suggestions  
✅ Simple web-based interface  

---

## **Installation**  

### **1. Clone the Repository**  
```sh
git clone https://github.com/Yogeeshkulal/essay-grading-system.git
cd essay-grading-system
```

### **2. Create a Virtual Environment (Optional but Recommended)**  
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### **3. Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4. Set Up OpenAI API Key**  
- Replace `"sk-your-openai-api-key"` in `app.py` with your **OpenAI API Key**.  
- Alternatively, you can set it as an environment variable:  
  ```sh
  export OPENAI_API_KEY="your_api_key"   # macOS/Linux
  set OPENAI_API_KEY="your_api_key"      # Windows
  ```

---

## **Usage**  

### **Run the Application**  
```sh
python app.py
```
This will start the **Flask server** at:  
📌 **http://127.0.0.1:5000/**  

### **Using the Web Interface**  
1. Open the web page in a browser.  
2. Upload a `.txt` or `.pdf` file containing your formal letter.  
3. Click **Submit** to get grading results.  

---

## **Project Structure**  

```
essay-grading-system/
│── app.py                 # Main Flask application  
│── requirements.txt        # Required dependencies  
│── static/  
│   ├── style.css          # Styles for the web page  
│   ├── script.js          # JavaScript for handling file uploads  
│── templates/  
│   ├── index.html         # Frontend HTML template  
│── README.md              # Project documentation  
│── temp/                  # Folder for storing uploaded files  
```

---

## **Technologies Used**  

- **Flask** – Web framework  
- **OpenAI GPT-3.5** – AI-based text analysis  
- **HTML/CSS/JavaScript** – Frontend design  
- **PyPDF2** – Extract text from PDF files  

---

## **To-Do & Future Improvements**  

✅ Enhance grading criteria for better feedback  
✅ Add support for more document formats (`.docx`)  
✅ Implement **user authentication** for saved results  
✅ Deploy the system using **Heroku / AWS / Render**  

--

---

### **Author**  
👤 **[Yogeesh ]**  
📧 Email: yogeeshkulal1234@gmail.com  
🔗 GitHub: [Yogeeshkulal](https://github.com/Yogeeshkulal)  

---

Let me know if you want any modifications! 🚀