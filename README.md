# Online PortfolioBuilder

Welcome to the **Online PortfolioBuilder**! This web application, built with Django, allows users to create a personalized portfolio by selecting from six unique designs. Users can input details such as name, education, work experience, skills, and more to generate a professional-looking portfolio website.

## Features

- **Six Design Templates:** Choose from six different templates to match your style and professional needs.
- **User-Friendly Input:** Easily enter your personal and professional details, including name, education, work experience, skills, and more.
- **Login and Registration:** Secure access with login and registration functionality.
- **Session-Based Security:** Pages are protected by sessions to prevent unauthorized access to the portfolio generation pages via direct URLs without logging in.
- **Responsive Design:** All templates are fully responsive, ensuring that your portfolio looks great on any device.
- **Customizable Options:** Simple and intuitive customization options to personalize the portfolio as per your preference.

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Templating Engine:** Django Templates
- **Authentication:** Django sessions for security

## How to Run the Application:

1. Navigate to the project directory:
    ```bash
    cd online-portfolio-maker
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run migrations:
    ```bash
    python manage.py migrate
    ```
4. Start the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and go to the given http link to access the application.

## Usage

1. **Register/Login:** First, register or log in to access the portfolio creation feature.
2. **Choose a Template:** Start by selecting one of the six available templates.
3. **Enter Your Details:** Fill in your personal and professional information.
4. **Generate Your Portfolio:** Once all details are filled out correctly, your professional portfolio webpage will be generated. Unauthorized users will not be able to access these pages via direct URLs.

Feel free to customize and modify the code to fit your needs!
