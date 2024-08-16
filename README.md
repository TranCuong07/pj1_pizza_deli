# Pizza Delivery API - Version 1.0

**OpenAPI Specification:** [OAS 3.1](./openapi.json)  
**Description:** This is a REST API for a Pizza Delivery Service built for learning, with a back end using FastAPI, SQLAlchemy, and PostgreSQL, and a front end currently being enhanced using React.

## Endpoints

### Order Management

| METHOD  | ROUTE                               | FUNCTIONALITY           |
|---------|-------------------------------------|-------------------------|
| **POST** | `/order/order`                     | _Place an Order_        |
| **POST** | `/order/order_all`                 | _List All Orders_       |
| **GET**  | `/order/order/{id}`                | _Get Order by ID_       |
| **GET**  | `/order/user/order`                | _Get User's Orders_     |
| **PUT**  | `/order/order/update/{order_id}/`  | _Update an Order_       |
| **PUT**  | `/order/order/status/{order_id}/`  | _Update Order Status_   |
| **DELETE** | `/order/order/delete/{id}/`      | _Delete an Order_       |

### Authentication

| METHOD  | ROUTE                               | FUNCTIONALITY             |
|---------|-------------------------------------|---------------------------|
| **GET**  | `/auth/login/google`               | _Login with Google_       |
| **GET**  | `/auth/login/google/callback`      | _Google Login Callback_   |
| **GET**  | `/auth/refresh`                    | _Refresh Token_           |

### Category Management

| METHOD  | ROUTE                                | FUNCTIONALITY             |
|---------|--------------------------------------|---------------------------|
| **GET**  | `/category/category`                | _List Categories_         |
| **GET**  | `/category/product_category/{slug}` | _Get Products by Category_|
| **GET**  | `/category/products`                | _List All Products_       |

## Schemas

| SCHEMA                | DESCRIPTION                                |
|-----------------------|--------------------------------------------|
| **HTTPValidationError** | _Schema for handling validation errors._ |
| **OrderModel**          | _Schema representing the order model._   |
| **OrderModelStatus**    | _Schema for order status._               |
| **ValidationError**     | _Schema for validation error details._   |
