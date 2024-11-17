const form = document.getElementById('contactForm');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Prepare API endpoint and request body
    const apiUrl = 'https://npv20xattg.execute-api.eu-west-1.amazonaws.com/default/AddContactInfo';
    const requestBody = JSON.stringify({
        name: name,
        email: email,
        message: message,
    });

    try {
        // Send POST request to the API Gateway
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: requestBody,
        });

        // Handle the response
        if (response.ok) {
            const result = await response.json();
            document.getElementById('responseMessage').innerText =
                result.message || 'Successfully submitted!';
        } else {
            const errorMessage = await response.text();
            document.getElementById('responseMessage').innerText =
                `Error: ${errorMessage || 'Something went wrong'}`;
        }
    } catch (error) {
        // Handle network or other unexpected errors
        console.error('Error submitting the form:', error);
        document.getElementById('responseMessage').innerText =
            'Error: Unable to send your message. Please try again.';
    }
});
