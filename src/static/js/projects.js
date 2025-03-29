function projectTableHTML(data) {
    return `<tr>
                <td>
                    <div class="d-flex align-items-center">
                        <a href="/Projects/${data.id}/Edit"
                            class="fs-6 fw-bolder text-decoration-none mt-1">
                            ${data.name}
                        </a>
                    </div>
                </td>
                <td>
                    <span class="text-muted fw-bold fs-6 d-block mt-1">${data.status}</span>
                </td>
                <td class="pe-0 text-end">
                    <a class="btn btn-light text-muted fw-bolder btn-sm px-5" href="/Projects/${data.id}/Edit">
                        View
                    </a>
                </td>
            </tr>`;
}

function saveProject() {
    const projform = document.getElementById('save-project-form');
    
    projform.addEventListener("submit",  async function(e) {

        e.preventDefault();
        const headers = {'X-CSRFToken': getCSRFToken()};
        const projectsList = document.getElementById('projects-list');
        var formData = new FormData(this);
        var myModalEl = document.getElementById('saveProjectModal');
        var modal = bootstrap.Modal.getInstance(myModalEl);
        
        fetchPost(this.action, headers, formData)
            .then((data) => {
                modal.hide();
                projform.reset();
                makeToast("Success", data.message, "success");
                projectsList.insertAdjacentHTML("beforeend", projectTableHTML(data));
            })
            .catch(error => console.error(error));

    });
}

document.addEventListener('DOMContentLoaded', function() {
    // Initialize functions when the DOM is fully loaded
    saveProject();
});
