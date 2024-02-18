document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var iconPath = calendarEl.getAttribute('data-icon-path');
    var userDates = JSON.parse(calendarEl.getAttribute('data-events'));

    var prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        titleFormat: { year: 'numeric', month: 'long' },
        headerToolbar: {
            start: 'title',
            center: '',
            end: 'prev,next'
        },
        events: userDates,
        eventContent: function(arg) {
            var element = document.createElement('div');
            element.classList.add('event-icon');
            element.innerHTML = `<img src="${iconPath}" alt="Event Icon">`;
            return { domNodes: [element] };
        }
    });

    calendar.render();

    // Apply dark mode specific styles if preferred
    if (prefersDarkMode) {
        document.querySelector('.fc-header-toolbar').classList.add('dark-mode');
    }
});
