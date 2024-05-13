If we want to make the feedback form accessible to  customers who are located in different geographical locations without exposing the responses to them, we'll need to deploy the Flask app to a web server accessible over the internet. Additionally, we can implement authentication to ensure that only we can view the responses.

Here's a general outline of how we can achieve this:

1. Deploy the Flask App: Choose a web hosting service or platform where we can deploy  Flask app. Some popular options include Heroku, AWS (Amazon Web Services), Google Cloud Platform, and PythonAnywhere. Follow the deployment instructions provided by  chosen platform to upload  Flask app files and deploy the app.

2. Secure the Feedback Page: Implement authentication to restrict access to the feedback page. we can use Flask's built-in session management or integrate a third-party authentication solution like OAuth. This way, only authenticated users (such as self) will be able to access the feedback results.

3. Share the Feedback Form Link: Once the app is deployed and secured, share the link to the feedback form with  customers. They can access the form by visiting the provided URL in their web browsers.

4. View Responses: As the service provider, we can access the feedback responses by logging in to the deployed Flask app. Since we're authenticated, we'll have access to the results page where we can view the feedback submitted by customers.

By following these steps, we can make the feedback form accessible to  customers while ensuring that only we can view the responses.