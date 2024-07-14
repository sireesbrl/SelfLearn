document.addEventListener('DOMContentLoaded', () => {
    const visible = document.querySelector('.visible');
    const sidebar = document.querySelector('.sidebar');
    const content = document.querySelector('.content');
    const chatbot = document.querySelector('.chatbot');
    const app_burger = document.createElement('div');
    app_burger.className = 'app-burger';

    if (window.matchMedia("(max-width: 767px)").matches) {
        // Code for mobile view
        sidebar.className = 'col-12 sidebar';
        sidebar.style.display = 'none';
        content.className = 'col-12 content';
        chatbot.className = 'col-12 chatbot';

        app_burger.innerHTML = '<button style="border: none; background-color: transparent"><i class="fas fa-bars"></i></button>';
        visible.prepend(app_burger);

        app_burger.addEventListener('click', () => {
            if (sidebar.style.display === 'block') {
                sidebar.style.display = 'none';
            } else {
                sidebar.style.display = 'block';
            }
        });
    } else {
        // Code for desktop view
        app_burger.innerHTML = '<button style="border: none; background-color: transparent"><i class="fas fa-bars"></i> Chapters </button>';
        sidebar.prepend(app_burger);

        app_burger.addEventListener('click', () => {
            if (sidebar.style.display === 'block') {
                sidebar.style.display = 'none';
                content.className = 'col-9 content';
                chatbot.className = 'col-2 chatbot';
                app_burger.innerHTML = '<button style="border: none; background-color: transparent"><i class="fas fa-bars"></i></button>';
                visible.prepend(app_burger);
            } else {
                sidebar.style.display = 'block';
                app_burger.innerHTML = '<button style="border: none; background-color: transparent"><i class="fas fa-bars"></i> Chapters </button>';
                sidebar.prepend(app_burger);
                content.className = 'col-6 content';
                chatbot.className = 'col-3 chatbot';
            }
        });
    }
    
});