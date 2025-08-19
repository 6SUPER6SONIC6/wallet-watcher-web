# Wallet Watcher Web

A Django web application for checking Ethereum wallet balances and token holdings. This project demonstrates full-stack web development skills using Django, PostgreSQL, and external API integration.

## About

This is a web version of my [Wallet Watcher Android app](https://github.com/6SUPER6SONIC6/wallet-watcher-android), created as a Django learning project to practice Python web development and showcase full-stack capabilities.

## Features

**Currently Implemented:**
- Ethereum wallet balance checking
- Token holdings display with USD values
- Clean, responsive web interface

**Planned:**
- User authentication and wallet saving
- Transaction history viewing  
- Search history functionality

## Technical Stack

- **Backend:** Django 5.2.5, Python 3.13
- **Database:** PostgreSQL  
- **Frontend:** Django Templates, HTML, CSS, JavaScript
- **API Integration:** Ethplorer API for blockchain data
- **Configuration:** Environment-based settings with python-decouple

## Architecture

The application follows Django's MVC pattern with:
- Models for data structure and database interaction
- Views handling business logic and API integration  
- Templates for user interface rendering
- PostgreSQL for data persistence
- External API integration for real-time blockchain data

## Setup

1. Clone the repository and create a virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables in `.env`:
   ```
   ETHPLORER_API_KEY=your-api-key
   SECRET_KEY=your-secret-key
   DEBUG=True
   DB_NAME=wallet_watcher_db
   DB_USER=your_db_user  
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```
4. Set up PostgreSQL database and run migrations
5. Start the development server: `python manage.py runserver`

## Skills Demonstrated

- Django web framework proficiency
- RESTful API integration and data parsing
- Environment-based configuration management
- MVC architecture implementation
- Frontend development with Django templates
- Python best practices and code organization

## Screenshots

![Wallet Watcher - Home](https://github.com/user-attachments/assets/869e6953-9a22-4949-9edc-2374b57f51ec)
![Wallet Watcher - Wallet Details](https://github.com/user-attachments/assets/3a490e08-3413-48f6-a24d-24817f9cca31)

## Data Source

Wallet data is fetched from the [Ethplorer API](https://github.com/EverexIO/Ethplorer/wiki/Ethplorer-API), which provides real-time Ethereum blockchain information, including wallet balances, token holdings, and market prices.

---

**Developer:** Vadym Tantsiura  
**Contact:** vadym.tantsiura@gmail.com | [@VTantsiura](http://t.me/VTantsiura)
