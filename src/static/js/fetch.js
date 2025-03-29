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

// Example for GET
// fetchGet('https://api.example.com/data')
//     .then(data => console.log(data))
//     .catch(error => console.error(error));

// Example for POST
// fetchPost('https://api.example.com/data', { key: 'value' })
//     .then(data => console.log(data))
//     .catch(error => console.error(error));

// Example for PUT
// fetchPut('https://api.example.com/data/1', { key: 'updatedValue' })
//     .then(data => console.log(data))
//     .catch(error => console.error(error));

// Example for PATCH
// fetchPatch('https://api.example.com/data/1', { key: 'patchedValue' })
//     .then(data => console.log(data))
//     .catch(error => console.error(error));

// Example for DELETE
// fetchDelete('https://api.example.com/data/1')
//     .then(data => console.log(data))
//     .catch(error => console.error(error));