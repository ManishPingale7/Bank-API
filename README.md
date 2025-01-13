# Bank API Server

This project implements an API server to query and retrieve bank and branch information. The application has been deployed using **Django** and can be accessed via **REST API** endpoints.

## Project Setup

This API server was developed using **Django** to create a simple and efficient service for querying bank and branch details.

## API Endpoints

### 1. `/api/branch/<ifsc>`
- **Method**: `GET`
- **Description**: This endpoint returns detailed information about a specific branch based on the IFSC code.
- **Response**:
    ```json
    {
        "ifsc": "ZSBL0000331",
        "bank": {
            "id": 101,
            "name": "ZILA SAHAKRI BANK LIMITED GHAZIABAD"
        },
        "branch": "RAVALI KALA",
        "address": "VILL.RAVLIKALA,MURAD NAGAR",
        "city": "RAVLI",
        "district": "GHAZIABAD",
        "state": "UTTAR PRADESH"
    }
    ```

### 2. `/api/bank`
- **Method**: `GET`
- **Description**: This endpoint returns a list of banks.
- **Response**:
    ```json
    [
        {
            "id": 1,
            "name": "STATE BANK OF INDIA"
        },
        {
            "id": 2,
            "name": "PUNJAB NATIONAL BANK"
        }
    ]
    ```

## Test Cases

The application includes test cases to ensure the correctness of the API endpoints. Test cases include:
- Validating that the `/api/bank` endpoint returns a list of banks with the correct structure.
- Ensuring that the `/api/branch/ifsc` endpoint returns details of a specific branch based on the IFSC code.
- Handling invalid requests and error scenarios.

## Deployment

The API has been deployed on **Render**. You can access it through the following links:

- [Bank List Endpoint](https://bank-api-vyji.onrender.com/api/bank)
- [Branch Details by IFSC Endpoint](https://bank-api-vyji.onrender.com/api/branch/ifsc)

## Time Taken

The time taken to complete this assignment was approximately **2 days**.

## How to Run Locally

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python manage.py runserver
    ```
4. The server will start locally at `http://127.0.0.1:8000`.

## Conclusion

This project demonstrates the use of a **REST API** to query bank and branch data. The API is fully functional, with proper error handling, test cases, and deployment on Render.

---
