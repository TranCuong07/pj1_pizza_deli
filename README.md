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

#### Order Management Endpoints

- **`POST /order/order`**: Create a new order. Required fields include user ID, product ID, quantity, and delivery address.
- **`POST /order/order_all`**: Retrieve a list of all orders in the system. This may include filters for pagination or search.
- **`GET /order/order/{id}`**: Fetch details of a specific order by its ID.
- **`GET /order/user/order`**: Retrieve all orders placed by the authenticated user.
- **`PUT /order/order/update/{order_id}/`**: Update details of an existing order. You can modify fields such as product quantity or delivery address.
- **`PUT /order/order/status/{order_id}/`**: Update the status of an order (e.g., processing, shipped, delivered).
- **`DELETE /order/order/delete/{id}/`**: Delete a specific order by its ID.

### Authentication

| METHOD  | ROUTE                         | FUNCTIONALITY         |
| ------- | ----------------------------- | --------------------- |
| **GET** | `/auth/login/google`          | Login with Google     |
| **GET** | `/auth/login/google/callback` | Google Login Callback |
| **GET** | `/auth/refresh`               | Refresh Token         |

#### Authentication Endpoints

- **`GET /auth/login/google`**: Initiates the Google OAuth2 login process. Redirects the user to Google's authentication page.
- **`GET /auth/login/google/callback`**: Handles the callback from Google after authentication. Exchanges the authorization code for tokens and creates a session.
- **`GET /auth/refresh`**: Refreshes the JWT token for an authenticated user.

### Category Management

| METHOD  | ROUTE                               | FUNCTIONALITY            |
| ------- | ----------------------------------- | ------------------------ |
| **GET** | `/category/category`                | List Categories          |
| **GET** | `/category/product_category/{slug}` | Get Products by Category |
| **GET** | `/category/products`                | List All Products        |

#### Category Management Endpoints

- **`GET /category/category`**: Retrieves a list of all product categories available.
- **`GET /category/product_category/{slug}`**: Fetch products under a specific category identified by its slug.
- **`GET /category/products`**: Retrieve a list of all products available in the system.

### Product Management

| METHOD  | ROUTE                     | FUNCTIONALITY     |
| ------- | ------------------------- | ----------------- |
| **GET** | `/products/products`      | List All Products |
| **GET** | `/products/products/{id}` | Get Product by ID |

#### Product Management Endpoints

- **`GET /products/products`**: Retrieve a list of all products.
- **`GET /products/products/{id}`**: Fetch details of a specific product by its ID.

### Webhook

| METHOD  | ROUTE              | FUNCTIONALITY        |
| ------- | ------------------ | -------------------- |
| **POST** | `/webhook/webhook` | Handle Webhook Events |

#### Webhook Endpoints

- **`POST /webhook/webhook`**: Handles incoming webhook events. This could include notifications from payment gateways or other external systems.

## Schemas

| SCHEMA                  | DESCRIPTION                           |
| ----------------------- | ------------------------------------- |
| **HTTPValidationError** | Schema for handling validation errors |
| **OrderCreateModel**    | Schema for creating a new order       |
| **OrderModel**          | Schema representing the order model   |
| **OrderModelStatus**    | Schema for order status               |
| **ValidationError**     | Schema for validation error details   |
| **PaymentStatus**       | Schema for payment status notifications |
| **ProductModel**        | Schema representing the product model |
| **WebhookData**         | Schema for handling webhook events    |

