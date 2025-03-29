function toastNotification(data) {
    const toastLiveExample = document.getElementById('liveToast')
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample);
    const toastBody = document.getElementById('toastBody');
    toastBody.innerHTML = data;
    toastBootstrap.show()
}

function notify() {
    const wsConnection = new signalR.HubConnectionBuilder()
        .withUrl("/notificationHub")
        .configureLogging(signalR.LogLevel.Information)
        .build();

    var _wsConnectionId = '';

    wsConnection.on('displayNotification',(data) => {
        toastNotification(data);
    });

    wsConnection.start()
        .then(function () {
            wsConnection.invoke('getConnectionId')
                .then(function (connectionId) {
                    _wsConnectionId = connectionId
                    console.log(_wsConnectionId)
                })
        })
        .catch(function (error) {
            console.log(error);
            //setTimeout(() => start(), 5000);
        })
}


document.addEventListener('DOMContentLoaded', function() {
    // Initialize functions when the DOM is fully loaded
    notify();
});