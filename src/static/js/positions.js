function positionTableHTML(data) {
    var tableRow = ` <tr>
        <td scope="row">${data.title}</td>
        <td>${data.peopleNeeded}</td>
        <td>0</td>
        <td>0</td>
        <td>Open</td>
        <td>
            <div class="dropdown">
                <!-- Card share action menu -->
                <button class="icon-sm btn btn-primary-soft btn-block w-100" type="button" id="profileAction2" data-bs-toggle="dropdown"
                    aria-expanded="false">
                    <i class="bi bi-three-dots"></i>
                </button>
                <!-- Card share action dropdown menu -->
                <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="profileAction2">
                    <li>
                        <a class="dropdown-item" href="/Positions/${data.id}/Details">
                            <i class="bi bi-info-circle-fill fa-fw pe-2"></i>
                            Details
                        </a>
                    </li>
                    <li>
                        <a class="dropdown-item" href="#">
                            <i class="bi bi-pencil-square fa-fw pe-2"></i>
                            Edit
                        </a>
                    </li>
                    <li>
                        <hr class="dropdown-divider">
                    </li>
                    <li>
                        <a class="dropdown-item" href="#">
                            <i class="bi bi-trash fa-fw pe-2"></i>
                            Delete
                        </a>
                    </li>
                </ul>
            </div>
        </td>
    </tr>`;

    return tableRow;
}

function savePosition() {
    const positionForm = document.getElementById('position-form');
    
    positionForm.addEventListener("submit",  async function(e) {

        e.preventDefault();
        const headers = {'X-CSRFToken': getCSRFToken()};
        const positionsList = document.getElementById('positions-table');
        var formData = new FormData(this);
        var myModalEl = document.getElementById('savePositionModal');
        var modal = bootstrap.Modal.getInstance(myModalEl);
        
        fetchPost(this.action, headers, formData)
            .then((data) => {
                modal.hide();
                positionForm.reset();
                makeToast(data.success === true ? "Success" : "Error", data.message, data.success === true ? "success" : "danger");
                positionsList.insertAdjacentHTML("beforeend", positionTableHTML(data));
            })
            .catch(error => console.error(error));

    });
}

document.addEventListener('DOMContentLoaded', function() {
    // Initialize functions when the DOM is fully loaded
    savePosition();
});
