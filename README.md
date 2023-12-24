# VChess

**VChess** is an online chess platform that allows users to play chess against each other in real-time. The project is divided into two main components: the backend and the frontend. They are Git submodules - essentially references (of commits) to other Git repositories to keep my backend and frontend code/commits seperate, while allowing them to be to be put in the same superproject.

## Features

- **Responsive UI:** User-friendly interface for seamless chess gameplay with high keyboard accessibility.
- **Real-time Chess:** Play chess against opponents in real-time.
- **Matchmaking:** Automatically find and pair players based on availability.
- **Analysis Mode:** Utilizes the Stockfish chess engine to run as a web worker to provide positions evaluation and move suggestions.
- **Puzzles:** A training mode to allow users to train their tactics on random chess puzzles.

## Getting Started

### Prerequisites

- Node.js and NPM installed on your machine.

### Installation

1. Clone the repository and update submodules:

   ```
   git clone --recursive https://github.com/tamnguyen820/VChess.git
   cd VChess
   git submodule update --init --recursive
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
- [Stockfish.js](https://github.com/nmrugg/stockfish.js): the chess engine this project uses for position analysis.