# API-INTEGRATION-DATA-VISUALIZATION-

COMPANY NAME:CODTECH IT SOLUTION PRIVATE LIMITED

NAME:KANIGA K

INTERN ID:CTIS0301

DOMAIN:PYTHON PROGRAMMING

DURATION:4 WEEKS

MENTOR:NEELA SANTHOSH

# API-INTEGRATION-DATA-VISUALIZATION-

This task focuses on integrating a public API with a Python backend and visualizing the fetched data in a meaningful way. The main data source used for this task is the OpenWeatherMap Public API, which provides real-time weather information such as temperature, humidity, and weather conditions for different cities across the world. OpenWeatherMap is a reliable and widely used public API that allows developers to access live environmental data using HTTP requests. In this project, the API is used to fetch current weather data for the city of Chennai by passing the city name and API key as query parameters.

The backend of the application is developed using Python Flask, which is a lightweight and flexible web framework. Flask is used to create API endpoints and handle HTTP requests and responses. The /weather endpoint is responsible for fetching data from the OpenWeatherMap API using the Requests library. Requests is a powerful Python library that simplifies sending HTTP requests and handling JSON responses. The API response is parsed to extract important values such as temperature and humidity, which are then returned as a JSON object. This confirms successful API integration and data retrieval.

For data visualization, the project uses Matplotlib, which is one of the most popular Python libraries for creating static graphs and charts. The fetched weather data is visualized using a bar chart that represents temperature and humidity values. This visual representation makes the data easier to understand and analyze compared to raw numerical values. The generated chart is saved as an image file in the static directory of the Flask project, which acts as the dashboard for this task. The dashboard provides a visual summary of the real-time weather data fetched from the API.

The frontend component of this project is minimal but functional. The Flask server provides a base route (/) that displays a simple message guiding users to the /weather endpoint. When users access the /weather route, they receive real-time weather data in JSON format, which can be consumed by any frontend application or tested directly through a browser. The static folder is used to store visualization outputs, following Flask’s standard project structure.

The tools and technologies used in this task include Python, Flask, Requests, Matplotlib, and Seaborn. All required dependencies are listed in the requirements.txt file to ensure easy installation and reproducibility. This task demonstrates a complete workflow of API integration, backend development, data processing, and visualization. Overall, it fulfills the task requirements by successfully fetching live data from a public API and presenting it through a visual dashboard, making it suitable for real-world data-driven applications.

#OUTPUT#
<img width="904" height="488" alt="Image" src="https://github.com/user-attachments/assets/919b5093-e513-4ceb-8e2f-c34451951c9f" />
