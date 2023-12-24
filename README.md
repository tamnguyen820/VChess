# VChess

VChess is an online chess platform that allows users to play chess against each other in real-time. The project is divided into two main components: the frontend and the backend.

## Features

- **Real-time Chess:** Play chess against opponents in real-time.
- **Matchmaking:** Automatically find and pair players based on availability.
- **Responsive UI:** User-friendly interface for seamless chess gameplay with high keyboard accessibility.
- **WebSocket Communication:** Utilizes WebSocket and Socket.IO for real-time communication.

## Getting Started

### Prerequisites

- Node.js and NPM installed on your machine.

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/tamnguyen820/VChess.git
   cd VChess
   ```

2. Install dependencies for both frontend and backend:
    ```
    # Install backend dependencies
    cd backend
    npm install

    # Install frontend dependencies
    cd ../frontend
    npm install
    ```

### Usage
You will need 2 terminal tabs/instances:
1. Start the backend server:
    ```
    cd backend
    npm start
    ```

2. Start the frontend development server:
    ```
    cd frontend
    npm start
    ```

3. Open the application in your web browser at http://localhost:5173/

## License
This project is licensed under the MIT License - see the [LICENSE ](./LICENSE) for details.

## Acknowledgments
- [Lichess](https://lichess.org/): the project utilizes many assets from Lichess (board themes, piece sets, sounds, API, etc.)
