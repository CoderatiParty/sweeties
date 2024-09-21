document.addEventListener("DOMContentLoaded", function() {
    const gridItems = document.querySelectorAll('.grid-item');
    const gridContainer = document.querySelector('.grid-container');

    const totalItems = gridItems.length;
    const gridStyle = window.getComputedStyle(gridContainer);
    const columns = gridStyle.gridTemplateColumns.split(' ').length;

    // Calculate the total number of rows
    const totalRows = Math.ceil(totalItems / columns);

    // Calculate the starting index of the last row
    const lastRowStartIndex = (totalRows - 1) * columns;

    // Get the last row items
    const lastRowItems = Array.from(gridItems).slice(lastRowStartIndex, totalItems);

    // Reset all grid items' bottom border color first
    gridItems.forEach(item => {
        item.style.borderBottom = '1px solid rgba(0, 0, 0, 0.8)';
    });

    // Change the bottom border color for only last row items
    lastRowItems.forEach(item => {
        item.style.borderBottom = '1px solid white';
    });
});