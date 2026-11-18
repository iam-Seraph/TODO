# TODO — Flask To-Do List

A small Flask web app with an HTML frontend and a text file for task storage. This is a beginner project.

## Layout

```text
TODO/
├── app.py                 # Flask server and routes
├── templates/index.html   # HTML frontend (Flask convention)
├── data/tasks.txt         # Existing saved tasks
├── requirements.txt
├── .gitignore
└── README.md
```

## Run

```bash
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 locally (or forward port 5000 privately in Codespaces).

Task data is loaded relative to this repository rather than the working directory. Note: `data/tasks.txt` is tracked in Git, so don't put private information there.
