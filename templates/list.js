function fetchPlayer(){
    fetch('/players',{
        method:'GET',
    }).then(response=> response.json())
    .then(response=> {
        const playerTable = document.getElementById("player_table")
        const tbody = playerTable.getElementsByTagName('tbody')[0];

    })
}

function createPlayer(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var data = {"username":username, "password":password}
    alert(JSON.stringify(data));

    fetch('/players/add', {
        method: 'POST',
        body: JSON.stringify(data),
        headers:{
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.text())
    .then(response => {
        if (response === "SUCCESS"){
            alert(response)
        }
        else{
            alert(response)
        }
    })
}