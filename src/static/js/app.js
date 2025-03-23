document.getElementById("toggleSidebar").addEventListener("click", function() {
    const sidebar = document.getElementById("sidebar");
    const toggleButton = document.getElementById("toggleSidebar");

    toggleButton.addEventListener("click", function() {
        sidebar.classList.toggle("show");
    });
});
