# MongoDB Atlas + Custom Logger Tutorial (Python)

##  Purpose

In real-world machine learning and data science projects, your training data will often reside on remote databases instead of your local machine. It's crucial to understand how to connect to these databases and retrieve data effectively. Additionally, as project structures become more complex (which they usually do), a proper logging system is essential to track program activities and quickly identify and debug issues.

This tutorial demonstrates both:
- **How to use MongoDB Atlas to import and access remote data**
- **How to implement a custom logger in Python to track activities and errors**

---
# MongoDB Atlas Setup + Python Integration

## 🔹 1. Create a MongoDB Atlas Account
- Go to: [https://www.mongodb.com/cloud/atlas/register](https://www.mongodb.com/cloud/atlas/register)
- Sign up or log in to your account.

## 🔹 2. Create a New Project
- Click **"New Project"**
- Name the project (e.g., `MyProject`)
- Click **"Create Project"**

## 🔹 3. Create a Free Cluster
Inside your project:
- Click **"Build a Database"**
- Choose **Shared (Free)** tier — this is the M0 plan
- Configure:
  - **Cloud Provider:** AWS / GCP / Azure
  - **Region:** Choose the one closest to you
  - **Cluster Name:** Use default `Cluster0` or rename it
- Click **"Create Cluster"**

>  *Note: Cluster setup may take a few minutes to finish.*

## 🔹 4. Create a Database User
- Navigate to **"Database Access"**
- Click **"Add New Database User"**
  - **Username:** e.g., `shakeeluetp`
  - **Password:** e.g., `Password123` (use a secure password)
- Save these credentials — you’ll use them in your Python code.

## 🔹 5. Add Your IP Address
- Go to **"Network Access"**
- Click **"Add IP Address"**
- Choose **"My Current IP Address"**
- Confirm and save.

## 🔹 6. Get Your Connection String
- Go to **"Clusters" → Cluster0 → Connect**
- Choose **"Connect Your Application"**
- Select **Python** and your version
- Copy the connection string. 
  Example:
  mongodb+srv://shakeeluetp:<password>@cluster0.xxxxx.mongodb.net/
  


##  Logger Setup

The logging functionality is implemented in the `logger.py` file.

### 🔹 Features:
- Automatically creates a `logs/` folder in your project directory.
- Generates separate `.log` files for each module that uses the logger.
- Flexible log levels: `INFO`, `WARNING`, `ERROR`, etc.

### 🔹 Usage:

- python
from logger import setup_logger
logger = setup_logger(__name__, level='INFO')
logger.info("This is an info message.")
logger.warning("This is a warning message.")

### 🔹 The setup_logger function:
- Accepts the module name and desired log level.
- Configures a logger with formatting and file handlers.
- Saves logs as logs/module_name.log.


###  File Descriptions

- **`logs/`**: Automatically created. Contains `.log` files per module to trace activities and errors.
- **`src/logger.py`**: Defines the `setup_logger()` function to generate and manage logs.
- **`src/mongo_connection.py`**: Contains logic to:
  - Establish a MongoDB Atlas connection.
  - Upload data from `train.csv` to the database.
  - Retrieve data back for use.
- **`src/main.py`**: The entry script, with the sole instruction:
  - import mongo_connection
- **`train.csv`**: A sample CSV file that will be sent to and retrieved from MongoDB.
- **`requirements.txt`**: Lists Python packages to install via `pip install -r requirements.txt`.
 **`.gitignore`**: Specifies files and directories that Git should ignore and not include in version control
- **`README.md`**: This file — contains setup steps, project structure, and instructions.


##  Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-url>
cd MangoDB_Python_Integration
```
### 2. Create and activate a virtual environment 
-  On Windows
   - python -m venv venv
   - venv\Scripts\activate

- On macOS/Linux
  - python3 -m venv venv
  - source venv/bin/activate

### 3. Install dependencies
- pip install -r requirements.txt

### 4. Run the application
- python src/main.py