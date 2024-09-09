const fetch = require('node-fetch');  // Ensure you have node-fetch installed if you're using fetch in Node.js

// Define an asynchronous function to fetch the data
async function getPlanetData() {
    try {
        const response = await fetch('https://swapi-api.alx-tools.com/api/planets/1/'); // Fetch the data
        const data = await response.json(); // Wait for the response to be parsed to JSON
        console.log(data); // Log the resolved data (now fully available)
    } catch (error) {
        console.error('Error fetching planet data:', error);
    }
}

// Call the async function
getPlanetData();
