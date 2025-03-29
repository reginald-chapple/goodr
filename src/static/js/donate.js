function makeDonation() {

    const donationForm = document.getElementById('donation-form');

    donationForm.addEventListener("submit",  async function(e) {
        e.preventDefault();

        const headers = {'X-CSRFToken': getCSRFToken()};

        var formData = new FormData(this);
        var myModalEl = document.getElementById('makeDonationModal');
        var modal = bootstrap.Modal.getInstance(myModalEl);

        fetchPost(this.action, headers, formData)
            .then((data) => {
                modal.hide();
                donationForm.reset();
                makeToast(data.success === true ? "Success" : "Error", data.message, data.success === true ? "success" : "danger");
            })
            .catch(error => console.error(error));
        
    });
}

document.addEventListener('DOMContentLoaded', function() {
    // Initialize functions when the DOM is fully loaded
    makeDonation();
});
