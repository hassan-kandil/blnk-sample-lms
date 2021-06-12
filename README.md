# blnk-sample-lms

## System Overview
The system manages loans and loan funds terms creation, update and delete in addition to loan applications submitted by customers and loan fund applications submitted by loan providers. A general workflow includes the bank personnel creating loan and loan funds terms which specify the properties of the loan or the loan fund; then, the loan provider can apply to a loan fund term and the customer can apply to a loan by submitting some additional info.  

## System Architecture & Technologies
The system is a client-side rendered single-page web application. The system can divided into 3 main components:
### Frontend (client):
- Built using Vuetify and Vuetify-Admin 
### Backend (server):
- A collection of APIs built using django rest framework (for APIs documentation see: https://documenter.getpostman.com/view/10061855/TzeTJUtt
- Can be divided into the following MVC architecture:
    - Model : django orm models which maps database tables onto python objects.
    - View: django rest framework serializers which maps models to JSON objects which are sent to the frontend to be rendered
    - Controller: django rest framework APIViews and ModelViewSets contains the APIs logic for different HTTP method types.
### Database:
- Postgresql Relational Database 

## System Features
### Authentication & Access Control
Authentication is implemented using Json Web Tokens (JWT) including the following features:
- Login (Token Creating)
- Refresh (Token Refreshing)
- Logout (Token Revoking)
- Role-Based Access Control (RBAC) is implemented using django permission classes
### Loans and Loan Funds Management
- Full support of Loans and Loan Funds CRUD operations by bank personnel (admins)

### Loan Applications Management
- Customers can create a loan application by selecting the loan term name and entering their personal details and requested loan amount and bank personnel can view and update the status and loan amounts of those applications.
- Calculation and presentation of loan amortization table by bank personnel and loan customers.
### Loan Fund Applications Management
- Loan providers can create a loan application by selecting the loan fund term name and entering the fund amount and bank personnel can view and update the status of those applications
- Calculation and presentation of loan amortization table by bank personnel and loan customers.

### Build & Environment
The development environment is containerized using docker containers and docker-compose where each main system component (client, server and database) is running in a docker container.
