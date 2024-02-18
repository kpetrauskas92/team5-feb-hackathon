document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar');
    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    const currentMonth = currentDate.getMonth();

    let displayYear = currentYear;
    if (currentMonth > 1 && currentMonth < 8) { 
        displayYear += 1;
    }

    // Detect dark mode preference
    const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;

    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        initialDate: `${displayYear}-02-01`,
        headerToolbar: {
            start: '', // Remove left buttons
            center: 'title',
            end: '' // Remove right buttons
        },
        // Customize the month text format
        titleFormat: { year: 'numeric', month: 'long' }
    });
    calendar.render();

    // Apply dark mode specific styles if preferred
    if (prefersDarkMode) {
        document.querySelector('.fc-header-toolbar').style.color = 'black';
    }
});
