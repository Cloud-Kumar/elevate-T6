# Flask Personal Portfolio Website

This is a clean, responsive, and modern personal portfolio website built with Python's Flask web framework and styled with Tailwind CSS. It's designed to showcase projects, skills, and provide a functional contact form for potential employers or collaborators.

## ✨ Key Features

-   **Modern & Responsive UI**: Built with Tailwind CSS for a mobile-first, fully responsive design that looks great on all devices.
-   **Dynamic Backend**: Powered by Flask to handle routing and form submissions.
-   **Home Page**: A comprehensive single-page layout including:
    -   Hero section with a clear call-to-action.
    -   **About Me**: A section detailing skills and core technologies.
    -   **Featured Projects**: A grid showcasing key projects with descriptions and links.
    -   **Testimonials**: Social proof from colleagues and clients.
-   **Contact Page**:
    -   Displays contact information (email, location).
    -   A functional contact form that captures user name, email, and message.
    -   Displays a success message upon successful submission without a page refresh.
-   **Clean Code**: Well-structured and commented Python and HTML code for easy understanding and modification.

---

## 🛠️ Technologies Used

-   **Backend**:
    -   Python
    -   Flask
-   **Frontend**:
    -   HTML5
    -   Tailwind CSS
    -   JavaScript (for mobile menu & dynamic year)
-   **Libraries & Services**:
    -   Google Fonts (Poppins & Inter)
    -   Font Awesome (for icons)

---


## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python installed on your system.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/cloud-kumar/elevate-T4.git](https://github.com/cloud-kumar/elevate-T4.git)
    cd your-repo-name
    ```

2.  **Create a virtual environment (recommended):**
    ```sh
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    A `requirements.txt` file should contain the project's dependencies.
    ```
    # requirements.txt
    Flask
    ```
    Install it using pip:
    ```sh
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```sh
    flask run
    ```
    Or run the Python script directly:
    ```sh
    python app.py
    ```

5.  **Open your browser** and navigate to `http://127.0.0.1:5000` to see the website in action.

---

## ⚙️ Usage

-   The **Home Page** is accessible at the root URL (`/`). You can scroll to different sections or use the navigation links.
-   The **Contact Page** is at the `/contact` route.
-   When a user fills out the contact form and clicks "Send Message", the form data is sent via a `POST` request to the `/contact` endpoint.
-   The Flask backend in `app.py` receives this data and prints it to the console. In a production environment, this logic would be replaced with a function to send an email or save the message to a database.
-   The user is then shown a success message on the same page.

---

## 👤 Contact

**Aditya Singh Bagri**

-   **Email**: [Bagriaditya00@gmail.com](mailto:Bagriaditya00@gmail.com)
-   **Location**: Indore, Madhya Pradesh, India
-   **GitHub**: [@AuntMayBro](https://github.com/AuntMayBro)

![alt text](<Screenshot 2025-08-13 225948.png>) 

![alt text](<Screenshot 2025-08-13 225932.png>)