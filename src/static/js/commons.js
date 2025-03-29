// function loadCities(stateId) {
//     $('#CityId').empty();
//
//     $.ajax({
//         url: `/States/${stateId}/GetCities`,
//         success: (response) => {
//             console.log(response);
//             if (response != null && response != undefined && response.length > 0) {
//                 $('#CityId').attr('disabled', false);
//                 $('#CityId').append('<option value="-1">--Select City--</option>');
//                 $.each(response, (i, data) => {
//                     $('#CityId').append(`<option value="${data.id}">${data.name}</option>`);
//                 });
//             }
//             else {
//                 $('#CityId').attr('disabled', true);
//                 $('#CityId').append('<option value="-1">--No Cities found--</option>');
//             }
//         },
//         error: (error) => {
//             alert(error);
//         }
//     });
// }

function makeToast(header, body, messageType) {
    var toastContainer = `<div aria-live="polite" aria-atomic="true" class="position-relative">
        <div style="z-index: 1100;" class="toast-container position-fixed top-0 end-0 p-3">
            <div id="flashToast" class="toast show text-white bg-${messageType}" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="5000" data-bs-autohide="true">
                <div class="toast-header text-white bg-${messageType}">
                    <strong class="me-auto">${header}</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div id="flashToastBody" class="toast-body">
                    ${body}
                </div>
            </div>
        </div>
    </div>`;

    document.body.insertAdjacentHTML('afterbegin', toastContainer);
    const flashToast = document.getElementById('flashToast');
    const toast = bootstrap.Toast.getOrCreateInstance(flashToast);
    toast.show();
}

// function scrollTop(value) {
//     if (value !== undefined) {
//         // Set scroll position
//         document.documentElement.scrollTop = value;
//         document.body.scrollTop = value; // for Safari
//     } else {
//         // Get scroll position
//         return document.documentElement.scrollTop || document.body.scrollTop;
//     }
// }


function getCSRFToken() {
    let csrfToken = null;
    const cookies = document.cookie.split(';');
    cookies.forEach(cookie => {
        const [name, value] = cookie.trim().split('=');
        if (name === 'csrftoken') {
            csrfToken = value;
        }
    });
    return csrfToken;
}

async function fetchGet(url) {
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });
        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }
        return await response.json();
    } catch (error) {
        console.error('GET request failed', error);
        throw error;
    }
}

async function fetchPost(url, headers, data) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: headers,
            body: data,
        });
        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }
        return await response.json();
    } catch (error) {
        console.error('POST request failed', error);
        throw error;
    }
}

async function fetchPut(url, data) {
    try {
        const response = await fetch(url, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }
        return await response.json();
    } catch (error) {
        console.error('PUT request failed', error);
        throw error;
    }
}

async function fetchPatch(url, data) {
    try {
        const response = await fetch(url, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }
        return await response.json();
    } catch (error) {
        console.error('PATCH request failed', error);
        throw error;
    }
}

async function fetchDelete(url) {
    try {
        const response = await fetch(url, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
        });
        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }
        return await response.json();
    } catch (error) {
        console.error('DELETE request failed', error);
        throw error;
    }
}