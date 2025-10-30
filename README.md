# Flask002 - Professional Flask Application

A well-structured Flask REST API with modular architecture, service layer, and proper separation of concerns.

## 🏗️ Project Structure

```
Flask002/
├── backend/
│   ├── __init__.py           # Application factory
│   ├── config.py             # Configuration settings
│   ├── models/               # Database models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── todo.py
│   │   ├── feedback.py
│   │   ├── product.py
│   │   ├── post.py
│   │   └── booking.py
│   ├── routes/               # API endpoints
│   │   ├── __init__.py
│   │   ├── users.py
│   │   ├── todos.py
│   │   ├── feedback.py
│   │   ├── products.py
│   │   ├── posts.py
│   │   └── bookings.py
│   ├── services/             # Business logic layer
│   │   ├── user_service.py
│   │   ├── booking_service.py
│   │   └── product_service.py
│   └── utils/                # Helper functions
│       ├── __init__.py
│       ├── validators.py
│       └── response_helpers.py
├── instance/
│   └── site.db              # SQLite database
├── .env                     # Environment variables (not in git)
├── .env.example             # Environment template
├── .gitignore               # Git ignore file
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
└── README.md                # This file
```

## ✨ Features

- **Modular Architecture**: Organized code structure with clear separation
- **Service Layer**: Business logic separated from routes
- **Validation**: Input validation utilities
- **Environment Variables**: Secure configuration management
- **Error Handling**: Standardized error responses
- **CORS Enabled**: Ready for frontend integration
- **RESTful API**: Following REST best practices

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Flask002
   ```

2. **Create virtual environment**
   ```powershell
   python -m venv env
   .\env\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

The API will be available at `http://127.0.0.1:5000`

## 📡 API Endpoints

### Users
- `POST /user/` - Create user
- `GET /user/` - Get all users

### Bookings
- `POST /bookings/` - Create booking
- `GET /bookings/` - Get all bookings
- `GET /bookings/<id>` - Get booking by ID
- `PUT /bookings/<id>` - Update booking
- `DELETE /bookings/<id>` - Delete booking

### Products
- `POST /product/` - Create product
- `GET /product/` - Get all products

### Todos
- `POST /todos/` - Create todo
- `GET /todos/` - Get all todos

### Feedback
- `POST /feedback/` - Submit feedback
- `GET /feedback/` - Get all feedback

### Posts
- `POST /post/` - Create post
- `GET /post/` - Get all posts

## 🛠️ Configuration

Edit `.env` file for configuration:

```env
FLASK_ENV=development
FLASK_DEBUG=True
DATABASE_URI=sqlite:///site.db
SECRET_KEY=your-secret-key
```

## 📦 Dependencies

- **Flask** - Web framework
- **Flask-SQLAlchemy** - ORM for database
- **Flask-CORS** - Cross-Origin Resource Sharing
- **python-dotenv** - Environment variable management

## 🔒 Security Notes

- Change `SECRET_KEY` in production
- Use environment variables for sensitive data
- Never commit `.env` file to version control
- Consider using PostgreSQL in production instead of SQLite

## 🧪 Development

### Adding a New Model

1. Create model file in `backend/models/`
2. Add to `backend/models/__init__.py`
3. Create service in `backend/services/`
4. Create routes in `backend/routes/`
5. Register blueprint in `backend/__init__.py`

### Database Migrations

To reset the database:
```python
with app.app_context():
    db.drop_all()
    db.create_all()
```

## 📝 License

MIT License

## 👥 Contributing

Pull requests are welcome!
