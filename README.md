# Assessment Submission by Hardeep Kumar

## Info

There are two folders, 'back' for Backend and 'front' for Frontend.
Backend is written using FastAPI.
Frontend is written using Vue 3.

## Setup

## Backend

- cd to back
- create a virtual environment if needed. If using poetry then it will handle itself.
- Install dependencies using either poetry or pip

  ```sh
  poetry install
  # or
  pip install -r requirements.txt
  ```

- start server using `uvicorn app.main:app`

> # Note: the server must run on port 8000 or else frontend won't work

### Frontend

- cd to front
- use either yarn or npm to install dependencies

  ```sh
  yarn install
  # or
  npm install
  ```

- To start the server use `yarn dev` or `npm run dev`
- Open the url in browser
