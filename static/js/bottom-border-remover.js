document.addEventListener("DOMContentLoaded", function() {
    const gridItems = document.querySelectorAll('.grid-item');
    const gridContainer = document.querySelector('.grid-container');

    const totalItems = gridItems.length;
    const gridStyle = window.getComputedStyle(gridContainer);
    const columns = gridStyle.gridTemplateColumns.split(' ').length;

    // Calculate the starting index of the last row
    const lastRowStartIndex = Math.floor(totalItems / columns) * columns;

    // Get all items from the start index of the last row to the end
    const lastRowItems = Array.from(gridItems).slice(lastRowStartIndex);

    // Reset all grid items' bottom border color first
    gridItems.forEach(item => {
        item.style.borderBottom = '1px solid rgba(0, 0, 0, 0.8)';
    });

    // Change the bottom border color for only last row items
    lastRowItems.forEach((item, index) => {
        // Check if the item is in the last row
        if (lastRowStartIndex + index < totalItems) {
            item.style.borderBottom = '1px solid white';
        }
    });
});