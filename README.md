# Decision_tree_chat_bot

This repository contains the code for a Korean multilayer chatbot. The chatbot operates based on a decision tree logic, where users are presented with a set of options and their choice determines the next layer of interaction.

## Features

- Multilayer chatbot with decision tree logic
- Interactive user interface with Korean language support
- Easy text customization for personalized interactions
- Static questions provided at the start for initial guidance
- `index.html` in the `template` folder for reflecting static questions
- Styling customization available in `style.css` located in the `static` folder
- Docker support for easy deployment and testing
- Accessible through a REST API using FastAPI

## Usage

To try out the chatbot locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   
# Run this command to build docker image
   `
   docker build -t chatbot .

# Run the Docker container:
   
   docker run -d -p 8000:8000 chatbot

Access the chatbot at http://localhost:8000

## Customization
To modify the chatbot's text and questions, update the appropriate files or variables in the code.
To change the styling of the chatbot, edit the style.css file located in the static folder.

## Adding Depth
If you want to add more layers of depth to the chatbot, you can modify the code accordingly.
The current design supports three layers, but you can extend it by making the necessary adjustments.

## Contributions
Contributions to this project are welcome. If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

## License
MIT License
