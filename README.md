# MusicGeneration

Angular2 application for generating Salsa music through NLP concepts.

## Info

1.  `backend` directory contains the flask backend with the methods that do the generation process.

2.  `front` directory contains the angular2 frontend based on [angular-webpack-starter](https://github.com/AngularClass/angular2-webpack-starter)

## Usage

1.  Clone the repo

    ```bash
    git clone https://github.com/brayanrodbajo/MusicGeneration.git
    ```

2.  Install the backend related requirements and run. The following will start a flask-server on `localhost:8080`

    ```bash
    cd backend
    sh install.sh
    python3 run.py
    ```

3.  Install frontend related dependencies

    -   Easiest way to handle node related dependencies is to install [nvm](https://github.com/creationix/nvm)
    -   Once you have node installed, install the project's dependencies

    ```bash
    cd front

    # install project related dependencies
    npm install

    # run server
    npm run server
    ```

4.  Now navigate to `http://localhost:3000` 
