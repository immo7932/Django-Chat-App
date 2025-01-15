
# Django Chat App

A real-time chat application built with Django. This project demonstrates how to build a modern chat system with features such as real-time messaging, user authentication, and chat rooms using Django and Django Channels.

## Features

- **Real-Time Messaging:** Experience instant messaging powered by WebSockets.
- **User Authentication:** Secure user registration and login.
- **Chat Rooms:** Create or join rooms for group conversations.
- **Responsive UI:** Designed to work on both desktop and mobile devices.

## Demo

*(https://immo7933.pythonanywhere.com/)*

## Prerequisites

- **Python 3.x:** Make sure you have Python installed.
- **Django:** The project is built using Django. (Tested with Django 3.x/4.x)
- **Django Channels:** For handling WebSocket connections.
- **Redis:** Used as a channel layer for Django Channels. (Optional if you plan to run WebSockets in development, but recommended for production.)


## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/immo7932/Django-Chat-App.git
   cd Django-Chat-App
   ```

2. **Create a Virtual Environment**

   It’s recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```


4. **Apply Migrations**

   Prepare your database by applying migrations:

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**

   Start the server with:

   ```bash
   python manage.py runserver
   ```

8. **Access the Application**

   Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to start chatting.

## Usage

- **User Account:** Sign up or log in to access chat rooms.
- **Chat Rooms:** After logging in, join an existing room or create a new one.
- **Messaging:** Enjoy real-time communication in your chosen chat room.


## Configuration

### Django Channels & Redis

This project uses Django Channels to manage WebSocket connections. In your `settings.py`, you should configure the channel layers. For example:

```python
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
```

Ensure that you have Redis installed and running if you plan to use the production-ready WebSocket handling.

### Static Files

Manage your static files using Django’s built-in static files app. For production, don’t forget to run:

```bash
python manage.py collectstatic
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to contribute new features, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django Channels](https://channels.readthedocs.io/en/latest/)

