# Pizza Delivery API - Version 1.0

**OpenAPI Specification:** [OAS 3.1](./openapi.json)  
**Description:** This REST API is designed for a Pizza Delivery Service, with a backend built using FastAPI, SQLAlchemy, and PostgreSQL. The frontend is being enhanced using React.

## Endpoints

### Order Management

| METHOD     | ROUTE                             | FUNCTIONALITY       |
| ---------- | --------------------------------- | ------------------- |
| **POST**   | `/order/order`                    | Place an Order      |
| **POST**   | `/order/order_all`                | List All Orders     |
| **GET**    | `/order/order/{id}`               | Get Order by ID     |
| **GET**    | `/order/user/order`               | Get User's Orders   |
| **PUT**    | `/order/order/update/{order_id}/` | Update an Order     |
| **PUT**    | `/order/order/status/{order_id}/` | Update Order Status |
| **DELETE** | `/order/order/delete/{id}/`       | Delete an Order     |

### Authentication

| METHOD  | ROUTE                         | FUNCTIONALITY         |
| ------- | ----------------------------- | --------------------- |
| **GET** | `/auth/login/google`          | Login with Google     |
| **GET** | `/auth/login/google/callback` | Google Login Callback |
| **GET** | `/auth/refresh`               | Refresh Token         |

### Category Management

| METHOD  | ROUTE                               | FUNCTIONALITY            |
| ------- | ----------------------------------- | ------------------------ |
| **GET** | `/category/category`                | List Categories          |
| **GET** | `/category/product_category/{slug}` | Get Products by Category |
| **GET** | `/category/products`                | List All Products        |

### Product Management

| METHOD  | ROUTE                     | FUNCTIONALITY     |
| ------- | ------------------------- | ----------------- |
| **GET** | `/products/products`      | List All Products |
| **GET** | `/products/products/{id}` | Get Product by ID |

## Schemas

| SCHEMA                  | DESCRIPTION                           |
| ----------------------- | ------------------------------------- |
| **HTTPValidationError** | Schema for handling validation errors |
| **OrderModel**          | Schema representing the order model   |
| **OrderModelStatus**    | Schema for order status               |
| **ValidationError**     | Schema for validation error details   |
