# UserGuide: Learn to run _BabySearch!_

## an App made with Next.js (Frontend), Python (Backend), and MySQL (Database)

## Table of Contents

1. [Getting Started](#getting-started)
2. [Interacting with the App](#interacting-with-the-app)

## 1. Getting Started <a name="getting-started"></a>

### 1.1. System Requirements

Ensure that your device meets the following requirements:

- Internet connection.
- Modern web browser (e.g., Chrome, Firefox, Safari, Edge).
- Have [git](https://git-scm.com/downloads) installed to clone the project.
- Have [nodejs](https://nodejs.org/en/download) installed to install the necessary modules.
- Have [python](https://www.python.org/downloads/) installed to install the necessary libraries.
- Have [MySQL](https://www.apachefriends.org/es/index.html) installed to have data persistence, there are many alternatives, for example XAMPP is a good alternative since it is lightweight.
- Have [Docker](https://www.docker.com/get-started/) installed.

### 1.2. Installation Steps

Follow these steps to install and run the application:

#### Frontend Configuration (Next.js):

1. Open a terminal or command prompt on your computer, you can do this by putting 'cmd' in your operating system's file browser.
2. Navigate to the directory where you want to install the frontend, you can achieve this using the cd command until you reach the folder where you want to clone the project.
3. Run the following commands:
   ```bash
   git clone https://github.com/jcamilomolinar/VeRe-second-test.git  # Replace with the URL of the frontend repository
   cd frontend
   npm install  # Install the necessary dependencies
   npm run dev  # Start the frontend server
   ```
4. Open your web browser and go to http://localhost:9000 to access the application.

#### Backend Configuration (Next.js):

1. Open another terminal or command prompt on your computer.
2. Navigate to the directory where you clone the repository.
3. Run the following commands:
   ```bash
   cd backend
   pip install -r requirements.txt  # Install Python dependencies
   python index.py  # Start the backend server
   ```

#### Database Configuration (MySQL):

1. At this point it is only necessary to ensure that the database server is running through the graphical interface.

## 2. Navigating the Interface <a name="navigating-the-interface"></a>
