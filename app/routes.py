from flask import Blueprint, render_template, request, jsonify, session
from services.cognito_service import CognitoService 
from typing import Union, Tuple
from utils.cognito_utils import decode_cognito_jwt

# Define Flask Blueprints for different parts of the application
home_bp = Blueprint("home", __name__)
login_bp = Blueprint("login", __name__)
register_bp = Blueprint("register", __name__)
dashboard_bp = Blueprint("dashboard", __name__)

# Create an instance of CognitoService to interact with Amazon Cognito
cognito_service = CognitoService()  

@home_bp.route('/', methods=['GET'])
def home():
    """Render the default page"""
    return render_template("index.html")

@dashboard_bp.route('/dashboard', methods=['GET'])
def dashboard():
    """Render the dashboard page"""
    # Retrieve user_sub from the session
    user_sub = session.get('user_sub') 
    return render_template('dashboard.html', user_sub=user_sub)

@login_bp.route('/login', methods=['GET', 'POST'])
def login() -> Union[str, Tuple[str, int]]:
    """
    Render the login page for `GET` requests and handle user login for POST requests.

    Returns:
        - For `GET` requests, returns the rendered `HTML` template for the login page.
        - For `POST` requests:
            - If login is successful, returns a `JSON` response indicating success with a status code of `200`.
            - If an error occurs during login, returns a `JSON` response indicating failure with a status code of `400`.

    Raises:
        Exception: If an unexpected error occurs during user login.

    Example:
        To render the login page:
        ```python
        result = login()  # GET request
        ```

        To handle user login:
        ```python
        data = {
            'email': 'user@example.com',
            'password': 'Password#123',
        }
        result = login(request_data=data)  # POST request
        ```

    Note:
        - This function expects `JSON` data for `POST` requests. The `JSON` should contain 'email' and 'password' keys.
    """
    if request.method == 'POST':
        try:
            data = request.json
            email = data.get('email')
            password = data.get('password')

            # Call your CognitoService method for login here
            response = cognito_service.login_user(email, password)

            # Check if the Cognito response indicates a successful login
            if 'AuthenticationResult' in response:
                access_token = response['AuthenticationResult']['AccessToken']
                decoded_token = decode_cognito_jwt(access_token)
                user_sub = decoded_token.get('sub')

                # Set up user session
                session['user_sub'] = user_sub

                # Return a success message
                return jsonify({'success': True, 'message': 'User logged in successfully'}), 200
            
            # Handle login failure with a specific error message
            return jsonify({'success': False, 'message': 'Login failed. Please check your credentials.'}), 400
        
        # Handle other exceptions
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400

    return render_template("login.html")



@register_bp.route('/register', methods=['GET', 'POST'])
def register() -> Union[str, Tuple[str, int]]:
    """
    Render the registration page for `GET` requests and handle user registration for POST requests.

    Returns:
        - For `GET` requests, returns the rendered `HTML` template for the registration page.
        - For `POST` requests:
            - If registration is successful, returns a `JSON` response indicating success with a status code of `200`.
            - If an error occurs during registration, returns a `JSON` response indicating failure with a status code of `400`.

    Raises:
        Exception: If an unexpected error occurs during user registration.

    Example:
          To render the registration page:
            ```python
            result = register()  # GET request
            ```

          To handle user registration:
            ```python
            data = {
                'email': 'user@example.com',
                'password1': 'Password#123',
                'isTrainer': False
            }
            result = register(request_data=data)  # POST request
            ```

    Note:
        - This function expects `JSON` data for `POST` requests. The `JSON` should contain 'email', 'password1', and 'isTrainer' keys.
        - The 'isTrainer' key indicates whether the user is a Trainer. If present and `True`, the `user_type` is set to 'Trainer'; otherwise, it's set to 'Student'.
    """
    if request.method == 'POST':
        try:
            data = request.json  # Use request.json to handle JSON data
            email = data.get('email')
            password = data.get('password1')
            user_type = 'Trainer' if data.get('isTrainer') else 'Student'

            response = cognito_service.register_user(email, password, user_type)
            
            # Handle register response with a status code of 200
            return jsonify({'success': True, 'message': 'User registered successfully'}), 200
        except Exception as e:
            # Handle registration failure with a specific error message and a status code of 400
            return jsonify({'success': False, 'message': str(e)}), 400

    return render_template("register.html")

