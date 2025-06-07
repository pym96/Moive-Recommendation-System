# Movie Recommendation System

A full-stack movie recommendation system built with Flask (Python) backend and Vue.js frontend, featuring sentiment analysis using deep learning models and movie data from Douban.

## 🎬 Features

- **Movie Recommendation Engine**: Intelligent movie recommendations based on user preferences
- **Sentiment Analysis**: Deep learning-powered sentiment analysis of movie reviews using LSTM models
- **User Management**: User registration, authentication, and profile management
- **Movie Database**: Comprehensive movie information from Douban
- **Interactive Frontend**: Modern Vue.js interface with responsive design
- **File Upload/Download**: Support for various file types (images, documents)
- **RESTful API**: Well-structured API endpoints for seamless frontend-backend communication

## 🛠 Tech Stack

### Backend
- **Flask**: Python web framework
- **SQLAlchemy**: Database ORM
- **MySQL**: Database management system
- **Deep Learning**: LSTM models for sentiment analysis
- **Scrapy**: Web scraping framework
- **PaddlePaddle**: Deep learning framework

### Frontend
- **Vue.js**: Progressive JavaScript framework
- **Node.js**: JavaScript runtime environment

## 📋 Prerequisites

- Python 3.8.0
- Node.js v12.16.1
- MySQL Database
- Navicat (recommended for database management)

## 🚀 Installation & Setup

### 1. Database Setup

1. Install and configure MySQL database
2. Create a new database named `flask_douban_comment`
3. Import the database schema:
   ```bash
   # Using Navicat or MySQL command line
   # Import flask_douban_comment.sql file
   ```
4. Default database configuration:
   - **Port**: 3306
   - **Username**: root
   - **Password**: 123456

### 2. Backend Setup

1. Open the project in PyCharm or your preferred IDE

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Configure Python package index (optional, for faster downloads):
   ```bash
   pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
   ```

4. Upgrade pip and install dependencies:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Update database configuration in `Flask/app.py` if needed:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:your_password@localhost/flask_douban_comment'
   ```

6. Run the Flask application:
   ```bash
   cd Flask
   python app.py
   ```

   The backend server will start on `http://localhost:8081`

### 3. Frontend Setup

1. Navigate to the Vue.js frontend directory:
   ```bash
   cd vue
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   
   **For Node.js v17+ (recommended solution):**
   ```bash
   export NODE_OPTIONS="--openssl-legacy-provider"
   npm run serve
   ```
   
   **Or on Windows:**
   ```cmd
   set NODE_OPTIONS=--openssl-legacy-provider
   npm run serve
   ```
   
   **Alternative method - modify package.json:**
   ```bash
   npm run serve
   ```

   The frontend will be available at the URL displayed in the terminal (typically `http://localhost:8080`)

## 🌐 Usage

1. **Start the Backend**: Run `python app.py` in the Flask directory
2. **Start the Frontend**: Run `npm run serve` in the vue directory (with Node.js legacy provider if using Node.js v17+)
3. **Access the Application**: Open your browser and navigate to the frontend URL provided by the Vue.js development server

## 📁 Project Structure

```
Movie Recommendation System/
├── Flask/                          # Backend application
│   ├── api/                        # API endpoints
│   ├── base/                       # Base configurations and utilities
│   ├── models/                     # Database models
│   ├── algorithm/                  # Recommendation algorithms
│   ├── deeplearning/              # Deep learning models
│   └── app.py                      # Main Flask application
├── vue/                            # Frontend application
│   ├── src/                        # Vue.js source code
│   ├── public/                     # Public assets
│   └── package.json                # Node.js dependencies
├── scrapy/                         # Web scraping scripts
├── flask_douban_comment.sql        # Database schema
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## 🔧 API Endpoints

- **User Management**: `/user/*` - User registration, login, profile management
- **Movie Operations**: `/movie/*` - Movie data, recommendations, reviews
- **File Operations**: `/file/upload`, `/file/download/<filename>/` - File handling
- **Deep Learning**: `/deeplearning/senti_single` - Sentiment analysis

## 🤖 Machine Learning Features

The system includes advanced machine learning capabilities:

- **LSTM-based Sentiment Analysis**: Analyzes movie review sentiments
- **Recommendation Algorithm**: Provides personalized movie recommendations
- **Data Processing**: Automated data collection and preprocessing

## 🔒 Database Configuration

Update the database connection string in `Flask/app.py`:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@host:port/database_name'
```

## 🎯 Development

### Backend Development
- Main application file: `Flask/app.py`
- API routes: `Flask/api/`
- Database models: `Flask/models/`
- Deep learning models: `Flask/deeplearning/`

### Frontend Development
- Vue.js components: `vue/src/components/`
- Vue.js views: `vue/src/views/`
- API services: `vue/src/services/`

## 📝 License

This project is for educational and research purposes.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For any issues or questions, please check the configuration settings and ensure all dependencies are properly installed.

## 🛠 Troubleshooting

### Node.js Compatibility Issue

If you encounter the error `error:0308010C:digital envelope routines::unsupported` when running `npm run serve`, this is due to Node.js v17+ using OpenSSL 3.0. Here are the solutions:

**Solution 1: Use Legacy OpenSSL Provider (Recommended)**
```bash
# macOS/Linux
export NODE_OPTIONS="--openssl-legacy-provider"
npm run serve

# Windows
set NODE_OPTIONS=--openssl-legacy-provider
npm run serve
```

**Solution 2: Modify package.json (Permanent Fix)**
Update the `serve` script in `vue/package.json`:
```json
{
  "scripts": {
    "serve": "NODE_OPTIONS=--openssl-legacy-provider vue-cli-service serve"
  }
}
```

**Solution 3: Use Node Version Manager**
Install and use Node.js v12.16.1 as originally intended:
```bash
# Install nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Install and use Node.js v12.16.1
nvm install 12.16.1
nvm use 12.16.1
```

### Common Issues

1. **Database Connection Failed**: Verify MySQL is running and credentials are correct
2. **Port Already in Use**: Change the port in Flask app or Vue.js dev server
3. **Missing Dependencies**: Run `pip install -r requirements.txt` and `npm install`
4. **Python Version Issues**: Ensure you're using Python 3.8.0 as specified

---

**Note**: Make sure to update the database credentials and configuration according to your local setup before running the application. 