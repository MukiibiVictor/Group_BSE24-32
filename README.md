# Group_BSE24-32 Project

## Project Description
This is a simple yet comprehensive project designed to demonstrate and implement best practices for Continuous Integration (CI), Continuous Deployment (CD), and production-level monitoring. The project provides a full-stack web application that simulates a real-world scenario, incorporating **Django** for the backend and frontend setup using **Bootstrap**, **jQuery**, **Popper.js**, **Sass**, and **Webpack** with Loaders.

The main objective of this project is to enable developers and DevOps teams to understand and practice the key aspects of software delivery pipelines on a web application, including:

1. **Setting Up Continuous Integration (CI)**: Automating the testing and integration of code through CI tools.
2. **Continuous Deployment to Staging**: Deploying to a staging environment for testing and verification before production.
3. **Production Deployment and Monitoring**: Deploying the application to production and monitoring performance, security, and uptime.

---


## Installation
Follow these steps to set up the project locally:
1. Clone the repository: `git clone https://github.com/MukiibiVictor/Group_BSE24-32.git`
2. Navigate to the project directory: `cd repository-name`
3. Create and activate a virtual environment:For Windows(cmd) =>(CREATE)=> `python -m venv env` =>(ACTIVATE)=> `env\Scripts\activate`, For Windows(cmd) => `source env/bin/activate`
4. Install dependencies : `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start Django Development Server: `python manage.py runserver`

## Project Setup
- Initialize a Git repository: `git init`
- Set up remote on GitHub: `git remote add origin https://github.com/yourusername/Group_BSE24-X.git`


## Features of the web application
- User authentication (Sign up, login)
- Product display, shopping cart, order checkout, and payment forms.
- Responsive design
- Dark mode

## Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request.

 # Project Name

## Description
A brief description of your project.

## Production Environment Configuration

### Environment Variables
- `DATABASE_URL`: The URL for the PostgreSQL database.
- `SECRET_KEY`: The Django secret key.
- `DEBUG`: Should be `False` in production.
- `ALLOWED_HOSTS`: List of allowed hostnames.
- `AWS_ACCESS_KEY_ID`: AWS Access Key for S3 storage.
- `AWS_SECRET_ACCESS_KEY`: AWS Secret Key for S3 storage.

### Database Configuration
- **Database:** PostgreSQL
- **Version:** 12
- **Configurations:** SSL enabled, timezone set to UTC.

### Third-party Services
- **AWS S3:** For static and media file storage.
- **SendGrid:** For email delivery.
- **Stripe:** For payment processing.

### Application Settings
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: `['yourproductiondomain.com']`
- `STATIC_URL`: `/static/`
- `MEDIA_URL`: `/media/`
- `CACHES`: Redis configuration for caching.

### Dependencies
- `Django==3.2.5`
- `djangorestframework==3.12.4`
- `psycopg2-binary==2.9.1`
- `boto3==1.18.27`

### Deployment Settings
- **Buildpacks:** `heroku/python`
- **Custom Domains:** `yourproductiondomain.com`
- **SSL Certificates:** Enabled and managed by Heroku.


 

