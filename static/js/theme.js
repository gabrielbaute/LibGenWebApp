document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';

    if (currentTheme === 'dark') {
        document.body.classList.add('dark-theme');
        toggleButton.textContent = 'Light Mode';
    }

    toggleButton.addEventListener('click', () => {
        document.body.classList.toggle('dark-theme');
        
        if (document.body.classList.contains('dark-theme')) {
            toggleButton.textContent = 'Light Mode';
            localStorage.setItem('theme', 'dark');
        } else {
            toggleButton.textContent = 'Dark Mode';
            localStorage.setItem('theme', 'light');
        }
    });
});
