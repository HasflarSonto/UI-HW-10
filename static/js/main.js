// Common functionality for all pages
$(document).ready(function() {
    // Add active class to current page in navbar
    const currentPath = window.location.pathname;
    $('.nav-link').each(function() {
        if ($(this).attr('href') === currentPath) {
            $(this).addClass('active');
        }
    });

    // Handle form submissions
    $('form').on('submit', function(e) {
        e.preventDefault();
        const formData = $(this).serialize();
        // Add any common form handling logic here
    });
}); 