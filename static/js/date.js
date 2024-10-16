// Handles date display on base.html
function formatDate() {
    const date = new Date();

    // Array of weekday names
    const weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    
    // Array of month names
    const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

    // Get components of the date
    const weekday = weekdays[date.getDay()];      // Weekday (e.g., Friday)
    const day = date.getDate();                   // Day of the month (e.g., 20)
    const month = months[date.getMonth()];        // Month name (e.g., September)
    const year = date.getFullYear();              // Year (e.g., 2024)

    // Combine to form the desired format
    const formattedDate = `${weekday} ${day} ${month} ${year}`;
    
    // Display the date in the <p> element
    document.getElementById('date').textContent = formattedDate;
}

// Call the function when the page loads
formatDate();