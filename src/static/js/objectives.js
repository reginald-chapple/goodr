function objectivesListHTML(data) {
    const element = `<div class="col-12 p-2">
            <div class="border-bottom border-200 gx-0 flex-1 cursor-pointer pb-3">
                <div class="mb-1 mb-md-0 d-flex justify-content-between align-items-center lh-1">
                    <div>
                        <p for="item-1"
                            class="mb-1 mb-md-0 mb-xl-1 mb-xxl-0 fs-0 me-2 line-clamp-1 text-900 cursor-pointer">
                            <span class="fw-bold">${data.name}</span>
                            <span class="text-700 fs-0 mb-md-0 me-2 me-md-3 me-xl-2 me-xxl-3 mt-2 mb-0 d-block">
                                ${data.description}
                            </span>
                            <span class="text-700 fw-semibold fs--2 mb-md-0 me-2 me-md-3 me-xl-2 me-xxl-3 mt-2 mb-0 d-block">
                                ${data.created}
                            </span>
                        </p>
                    </div>
                    <div>
                        <button type="button" class="btn rounded-3 ms-auto btn-complementary-soft btn-sm mb-1">
                            <i class="bi bi-stopwatch"></i>
                        </button>
                            <button type="button" class="btn rounded-3 ms-auto btn-warning-soft btn-sm mb-1">
                            <i class="bi bi-pause-fill"></i>
                        </button>
                        <button type="button" class="btn rounded-3 ms-auto btn-danger-soft btn-sm mb-1">
                            <i class="bi bi-x-lg"></i>
                        </button>
                        <button type="button" class="btn rounded-3 ms-auto btn-primary-soft btn-sm mb-1">
                            <i class="bi bi-check-lg"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>`;

    return element;
}

function saveObjective() {
    const objForm = document.getElementById('save-objective-form');
    
    objForm.addEventListener("submit",  async function(e) {

        e.preventDefault();
        const headers = {'X-CSRFToken': getCSRFToken()};
        const objectivesList = document.getElementById('objectives-list');
        var formData = new FormData(this);
        var myModalEl = document.getElementById('saveObjectiveModal');
        var modal = bootstrap.Modal.getInstance(myModalEl);
        
        fetchPost(this.action, headers, formData)
            .then((data) => {
                modal.hide();
                objForm.reset();
                makeToast("Success", data.message, "success");
                objectivesList.insertAdjacentHTML("beforeend", objectivesListHTML(data));
            })
            .catch(error => console.error(error));
    });
}

function startObjective() {
    const startBtns = document.querySelectorAll("button[data-start-obj]");
    
    startBtns.forEach((btn) => {
        btn.addEventListener("click", e => {
            e.preventDefault();
            const objId = e.target.dataset.startObj;
            
            
        });
    })
}

document.addEventListener('DOMContentLoaded', function() {
    // Initialize functions when the DOM is fully loaded
    saveObjective();
});
