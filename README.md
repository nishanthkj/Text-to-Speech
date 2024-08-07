

## Running the Application Locally

1. **Activate the virtual environment** (if you created one):

    ```sh
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Run the application:**

    ```sh
    python app.py
    ```

3. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

Here's the full updated README file:

---

# Text-to-Speech Flask Application

This is a simple Flask application that provides a basic web interface. The application can be extended to include functionalities like converting text to speech using the gTTS library.

## Features

- Basic web interface with Flask.

## Requirements

- Python 3.12+
- Flask

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/nishanthkj/Text-to-Speech.git
    cd Text-to-Speech
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```sh
    python3.12 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Running the Application Locally

1. **Activate the virtual environment** (if you created one):

    ```sh
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Run the application:**

    ```sh
    python app.py
    ```

3. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

## Project Structure

```
Text-to-Speech/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Author

Nishanth K J

---

