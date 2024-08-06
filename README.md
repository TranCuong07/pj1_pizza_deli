## PIZZA DELIVERY API

"This is a REST API for a Pizza delivery service built for learning, with a back end using FastAPI, SQLAlchemy, and PostgreSQL, and a front end currently being enhanced using React."

## ROUTES TO IMPLEMENT

| METHOD   | ROUTE                              | FUNCTIONALITY               | ACCESS      |
| -------- | ---------------------------------- | --------------------------- | ----------- |
| _POST_   | `/auth/signup/`                    | _Register new user_         | _All users_ |
| _POST_   | `/auth/login/`                     | _Login user_                | _All users_ |
| _POST_   | `/orders/order/`                   | _Place an order_            | _All users_ |
| _PUT_    | `/orders/order/update/{order_id}/` | _Update an order_           | _All users_ |
| _PUT_    | `/orders/order/status/{order_id}/` | _Update order status_       | _Superuser_ |
| _DELETE_ | `/orders/order/delete/{order_id}/` | _Delete/Remove an order_    | _All users_ |
| _GET_    | `/orders/user/orders/`             | _Get user's orders_         | _All users_ |
| _GET_    | `/orders/orders/`                  | _List all orders made_      | _Superuser_ |
| _GET_    | `/orders/orders/{order_id}/`       | _Retrieve an order_         | _Superuser_ |
| _GET_    | `/orders/user/order/{order_id}/`   | _Get user's specific order_ |
| _GET_    | `/docs/`                           | _View API documentation_    | _All users_ |

## How to run the Project

BE:

- Install Python
- Git clone the project with ` git clone https://github.com/TranCuong07/pj1_pizza_deli`
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Install the requirements with `pip install -r requirements.txt`
- Set Up your PostgreSQL database and set its URI in your `database.py`
- run the API
  ``uvicorn main:app`
  
FE:

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.



