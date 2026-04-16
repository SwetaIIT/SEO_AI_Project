# Configuration Management

# Set the environment (development, testing, production)
environment = 'development'

# Database configuration
database_config = {
    'host': 'localhost',
    'port': 5432,
    'user': 'user',
    'password': 'password',
    'database_name': 'seo_ai_project'
}

# Logging configuration
log_file_path = '/var/log/seo_ai_project.log'
log_level = 'DEBUG'

# API keys
api_keys = {
    'google': 'YOUR_GOOGLE_API_KEY',
    'bing': 'YOUR_BING_API_KEY'
}

# Feature toggles
features = {
    'feature_x': True,
    'feature_y': False
}