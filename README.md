# Travel-Bot

TravelBot is an open-source project designed to help users find budget-friendly flight options based on their pre-defined preferences. This project serves as a bot that actively monitors and retrieves information on cheap flights, delivering them directly to the user's email. Users can set preferences such as the duration of stay, the number of travelers, maximum budget, departure and destination locations.

## Features
- **Personalized Preferences:** Customize your flight search by specifying the length of your stay, the number of people traveling, maximum budget, and the departure/destination locations.
- **Automated Flight Monitoring:** The bot continuously monitors various flight databases and sources to find the best deals that match the user's preferences.
- **Email Notifications:** Receive updates directly in your email with a list of the cheapest flights that align with your chosen criteria.
## Implementation Details

- **Web Scraping with Selenium:** CheapFlightsBot utilizes the Selenium library and a web driver to scrape relevant data from various travel websites, ensuring accurate and up-to-date flight information.

- **Email Delivery with smtplib and email.mime:** To send personalized flight suggestions, the bot employs the smtplib library and email.mime module, allowing for seamless email communication with users.

- **Hosted on Replit:** CheapFlightsBot is hosted on Replit, providing a hassle-free and accessible platform for users to deploy and run the bot without the need for complex setup procedures.

## Usage 
Example e-mail returned by bot
![image](https://github.com/katarzynamichalskaa/Travel-Bot/assets/92379328/cbbeec0a-0bd2-42d7-8832-93aa70e18c24)
