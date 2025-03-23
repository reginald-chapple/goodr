document.addEventListener("DOMContentLoaded", function () {
    const taskSearchInput = document.getElementById("task-template-search");
    const employeeSearchInput = document.getElementById("employee-search");
    const taskResultsDiv = document.getElementById("task-search-results");
    const employeeResultsDiv = document.getElementById("employee-search-results");

    let selectedTaskTemplate = null;
    let selectedEmployee = null;

    taskSearchInput.addEventListener("input", function () {
        let query = taskSearchInput.value.trim();
        if (query.length > 1) {
            fetch(`/tasks/task-template-search/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    taskResultsDiv.innerHTML = "";
                    data.forEach(item => {
                        let option = document.createElement("div");
                        option.textContent = item.name;
                        option.setAttribute("data-id", item.id);
                        option.classList.add("search-result");
                        option.onclick = function () {
                            selectedTaskTemplate = item.id;
                            taskSearchInput.value = item.name;
                            taskResultsDiv.innerHTML = "";
                        };
                        taskResultsDiv.appendChild(option);
                    });
                });
        }
    });

    employeeSearchInput.addEventListener("input", function () {
        let query = employeeSearchInput.value.trim();
    
        if (query.length > 1) {
            fetch(`/tasks/employee-search/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    employeeResultsDiv.innerHTML = "";
                    data.forEach(item => {
                        let option = document.createElement("div");
                        option.textContent = item.name;
                        option.setAttribute("data-id", item.id);
                        option.classList.add("search-result");
                        option.onclick = function () {
                            selectedEmployee = item.id;
                            employeeSearchInput.value = item.name;
                            employeeResultsDiv.innerHTML = "";
                        };
                        employeeResultsDiv.appendChild(option);
                    });
                });
        }
    });    

    document.getElementById("assign-task-btn").addEventListener("click", function () {
        if (!selectedTaskTemplate || !selectedEmployee) {
            alert("Please select both a Task Template and an Employee.");
            return;
        }

        fetch(`/tasks/create-task/${selectedTaskTemplate}/${selectedEmployee}/`, {
            method: "POST",
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        })
            .then(response => response.json())
            .then(data => {
                window.location.href = "/tasks/assign/"; // Reload page to show new task
            });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            let cookies = document.cookie.split(";");
            cookies.forEach(cookie => {
                let trimmed = cookie.trim();
                if (trimmed.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(trimmed.split("=")[1]);
                }
            });
        }
        return cookieValue;
    }
});
