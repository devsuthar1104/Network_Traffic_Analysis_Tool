# Network Traffic Analysis Tool

## Overview

This project is a web-based tool for capturing and analyzing network traffic data. It allows users to input network traffic data, analyze it for anomalies, and display the results in a user-friendly interface.

## Features

- Capture network traffic data
- Input form for adding network traffic details
- Analyze network traffic for anomalies
- Display analysis results

## Technologies Used

- Django 5.0.6
- Channels (for asynchronous tasks)
- Pyshark (for packet capturing)
- Bootstrap (for styling)

## Prerequisites

- Python 3.12 or higher
- Django 5.0.6
- Pip (Python package installer)

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/devsuthar1104/network_analysis_tool.git
    cd network_analysis_tool
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv env
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```sh
        .\env\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source env/bin/activate
        ```

4. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

5. **Make migrations and migrate the database:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

1. **Add Network Traffic Data:**

    - Use the form on the homepage to input network traffic details such as source IP, destination IP, protocol, length, and additional info.
    - Click "Submit Traffic Data" to save the data.

2. **Analyze Traffic Data:**

    - Click on the "Analyze Traffic" button to start the analysis.
    - The results will be displayed on a new page, showing any detected anomalies.


## Contributing

Contributions are welcome! Please create a pull request with your changes, and make sure to include tests if applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- Thanks to the Django and Channels communities for their excellent frameworks and support.
- Inspired by various network analysis tools and tutorials available online.
