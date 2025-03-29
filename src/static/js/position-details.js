async function getCandidate() {

    const candidateBtns = document.querySelectorAll(".candidate-btn");

    candidateBtns.forEach(element => {
        element.addEventListener("click", async function(e) {
            var candidateId = e.target.dataset.candidate;

            try {
                const response = await fetch(`/Candidates/GetCandidate/${candidateId}`);
                if (!response.ok) {
                    throw new Error('Candidate not found');
                }
                const candidate = await response.json();

                // Populate the modal with candidate data
                document.getElementById('candidatePosition').textContent = candidate.position;
                document.getElementById('candidateName').textContent = candidate.name;
                document.getElementById('candidateExperience').textContent = candidate.experience;
                document.getElementById('CandidateId').setAttribute("value", candidate.id);

                // Show the modal
                const candidateModal = new bootstrap.Modal(document.getElementById('candidateModal'));
                candidateModal.show();

            } catch (error) {
                console.error(error);
                alert('Failed to load candidate details.');
            }
        });
    });
}

async function setCandidateStatus() {

    const csform = document.getElementById('candidate-status-form');

    csform.addEventListener('submit', (e) => {
        e.preventDefault();

        const headers = {'X-CSRFToken': getCSRFToken()};
        var myModalEl = document.getElementById('candidateModal');
        var modal = bootstrap.Modal.getInstance(myModalEl);
        const form = e.target;
        const formData = new FormData(form);

        fetchPost(form.action, headers, formData)
            .then((data) => {
                modal.hide();
                csform.reset();
                document.getElementById("candidate-status").textContent = data.status;
                makeToast(data.success === true ? "Success" : "Error", data.message, data.success === true ? "success" : "danger");
            })
            .catch(error => console.error(error));
    });
    
}

document.addEventListener("DOMContentLoaded", function() {
    getCandidate();
    setCandidateStatus();
});