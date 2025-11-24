# Wallet Watcher Web

A web version of my [Wallet Watcher Android app](https://github.com/6SUPER6SONIC6/wallet-watcher-android) for checking Ethereum wallet balances and token holdings.

## Features

- Ethereum wallet balance checking
- Token holdings display with USD values
- Clean, responsive web interface

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

## Screenshots

![Wallet Watcher - Home](https://github.com/user-attachments/assets/869e6953-9a22-4949-9edc-2374b57f51ec)
![Wallet Watcher - Wallet Details](https://github.com/user-attachments/assets/3a490e08-3413-48f6-a24d-24817f9cca31)

## Data Source

Wallet data is fetched from the [Ethplorer API](https://github.com/EverexIO/Ethplorer/wiki/Ethplorer-API), which provides real-time Ethereum blockchain information, including wallet balances, token holdings, and market prices.

---

**Developer:** Vadym Tantsiura  
**Contact:** vadym.tantsiura@gmail.com | [@VTantsiura](http://t.me/VTantsiura)
