# Serverless Web Application with AWS Pipeline

This repository hosts a modern, minimalist web application designed to capture contact form submissions and process them using an AWS serverless architecture. It leverages AWS Lambda, API Gateway, and a CI/CD pipeline for seamless deployment.

---

## Features

- **Responsive Web Design**: Built using HTML, CSS, and JavaScript for a clean and modern look.
- **Serverless Integration**: Processes form submissions through an API Gateway connected to AWS Lambda.
- **Continuous Integration and Deployment (CI/CD)**: Automatically deploys updates using an AWS pipeline.
- **Error Handling**: Comprehensive client-side error handling for robust performance.

---

## Project Structure

- **`index.html`**: The main HTML file containing the web application's structure and a contact form.  
  - Features a responsive design and minimalistic styling for a professional user experience.

- **`style.css`**: Custom CSS to style the application.  
  - Includes consistent spacing, modern typography, and hover effects for buttons.

- **`script.js`**: Handles the client-side logic to send form submissions to AWS Lambda via API Gateway.  
  - Uses `fetch` to make POST requests and dynamically display success/error messages.

---

## AWS Integration

The web application integrates with AWS services as follows:

1. **API Gateway**:
   - Endpoint: `https://npv20xattg.execute-api.eu-west-1.amazonaws.com/default/AddContactInfo`
   - Handles incoming HTTP POST requests from the contact form.

2. **AWS Lambda**:
   - Processes the contact form data submitted via the API Gateway.

3. **AWS CodePipeline**:
   - Automatically deploys changes from this repository to the AWS infrastructure.
   - Ensures a streamlined development workflow.

---

## Getting Started

### Prerequisites
- An AWS account with the required permissions for Lambda, API Gateway, and CodePipeline.
- Node.js and npm (for local development if needed).
- A text editor like VSCode.

### Deployment Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/myServerlessWebApp.git
   cd myServerlessWebApp

	2.	Ensure the .gitignore file excludes sensitive information (e.g., .env files).
	3.	Push changes to your connected GitHub repository:

git add .
git commit -m "Initial commit"
git push origin main


	4.	The AWS pipeline will automatically deploy the changes to the configured AWS services.

Usage

	1.	Open the web application in your browser.
	2.	Fill out the contact form with your name, email, and message.
	3.	Submit the form to send the data to the backend serverless architecture.
	4.	A success or error message will appear dynamically below the form.

Technologies Used

	•	Frontend: HTML5, CSS3, JavaScript
	•	Backend: AWS Lambda (Serverless Function)
	•	API Management: AWS API Gateway
	•	CI/CD: AWS CodePipeline

Future Enhancements

	•	Add unit tests for form validation and API integration.
	•	Expand the pipeline to include staging and production environments.
	•	Integrate with an AWS DynamoDB to store form submissions persistently.

License

This project is licensed under the MIT License. See the LICENSE file for details.
