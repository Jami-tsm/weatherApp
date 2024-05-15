# Weather App README

## Description:
This repository contains a simple weather application built using Python (Django framework), HTML, CSS, and integrating with the OpenWeatherMap API. The application allows users to view weather information for various cities by making API calls to retrieve real-time weather data.

## Features:
- **City Search**: Users can add cities to the list to view their weather information.
- **Real-time Weather Data**: The application fetches real-time weather data from the OpenWeatherMap API.
- **Responsive Design**: The application has been designed with a responsive layout, ensuring a seamless user experience across different devices.

## Installation:
1. Clone the repository to your local machine:
  - git clone https://github.com/your-username/weather-app.git
2. Navigate to the project directory:
  - cd weatherEnv

## Configuration:
1. Obtain an API key from OpenWeatherMap by signing up on their website: [OpenWeatherMap API](https://home.openweathermap.org/users/sign_up).
2. Replace the placeholder API key (`f743a61e7ada3bf0669ed715de4d2e6f`) in the `base_url` variable in `views.py` with your API key.

## Usage:
1. Start the Django development server:
  - python manage.py runserver
2. Open your web browser and navigate to `http://localhost:8000` to access the application.
3. Use the city search form to add cities and view their weather information.

## Contributing:
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## Credits:
- This project is built using the Django web framework.
- Weather data is fetched from the OpenWeatherMap API.
- The project utilizes Bootstrap for CSS styling.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact:
For any questions or feedback, please feel free to contact the project maintainer at [jameson.oliver.baker@gmail.com](mailto:jameson.oliver.baker@gmail.com).

## Disclaimer:
This application is for educational and demonstration purposes only. It should not be used in production environments without proper testing and validation. The developers are not responsible for any misuse or damages caused by the application.

