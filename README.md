# summarizer-api

This is a simple backend project created using *FASTAPI* that can get both abstractive and extractive summary of a given paragraph.

## Setup Process

1. (optional) It is recommended but not necessary that you setup the project in a python virual environment instead of global environment. You can use either venv or conda environment for that. In order to create and activate virtual environment using venv:
   `$ python -m venv "name"`

    To activate a virtual environment created using venv:
	For windows:`$ /name/Scripts/activate `

    For UNIX:`$ /name/Bin/activate`

2. In order to install all the libraries necessary, run the following command:

    `$ pip install -r requirement.txt`

3. Start The server using:

    `$ uvicorn main:app --reload  `

    It might take very long to start the very first time, as it will download transformers ~ 1. 4GB, so be 	patient.


## APIs

### Abstactive Summary

API Endpoint: `http://127.0.0.1:8000/abstractive/`

[POST] Request Body:

```
{
    "body": "your paragraph here"
}
```

Response Body:

```
{
    "summary": "example response"
}
```

### Extractive Summary

API Endpoint: `http://127.0.0.1:8000/extractive/`

[POST] Request Body:

```
{
    "body": "your paragraph here"
}
```

Response Body:

```
{
    "summary": "example response"
}
```
