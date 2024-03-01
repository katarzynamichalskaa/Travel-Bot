# Travel-Bot

TravelBot is an open-source project designed to help users find budget-friendly flight options based on their pre-defined preferences. This project serves as a bot that actively monitors and retrieves information on cheap flights, delivering them directly to the user's email. Users can set preferences such as the duration of stay, the number of travelers, maximum budget, departure and destination locations.

## Features
- **Personalized Preferences:** Customize your flight search by specifying the length of your stay, the number of people traveling, maximum budget, and the departure/destination locations.
- **Automated Flight Monitoring:** The bot continuously monitors various flight databases and sources to find the best deals that match the user's preferences.
- **Email Notifications:** Receive updates directly in your email with a list of the cheapest flights that align with your chosen criteria.
## Implementation Details

- **Web Scraping with Requests:** TravelBot utilizes the Requests library to scrape relevant data from https://www.azair.eu/, ensuring accurate and up-to-date flight information.

- **Email Delivery with smtplib and email.mime:** To send personalized flight suggestions, the bot employs the smtplib library and email.mime module, allowing for seamless email communication with users.

- **Hosted on Replit:** TravelBot is hosted on Replit, providing a hassle-free and accessible platform for users to deploy and run the bot without the need for complex setup procedures.

## Usage 
Example e-mail returned by bot

![image](https://github.com/katarzynamichalskaa/Travel-Bot/assets/92379328/500bb6a1-9664-45b7-8917-ddc7036e9e0b)

