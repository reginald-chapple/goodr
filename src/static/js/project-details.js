function sendVolunteerRequest() {
    const vrform = document.getElementById('volunteer-request-form');

    vrform.addEventListener('submit', (e) => {
        e.preventDefault();

        const headers = {'X-CSRFToken': getCSRFToken()};
        var myModalEl = document.getElementById('volunteerRequestModal');
        var modal = bootstrap.Modal.getInstance(myModalEl);
        const form = e.target;
        const formData = new FormData(form);

        fetchPost(form.action, headers, formData)
            .then((data) => {
                modal.hide();
                vrform.reset();
                makeToast(data.success === true ? "Success" : "Error", data.message, data.success === true ? "success" : "danger");
            })
            .catch(error => console.error(error));
    });
}

document.addEventListener("DOMContentLoaded", function() {
    sendVolunteerRequest();
});