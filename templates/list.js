function fetchPlayer() {
    fetch('/players', {
        method: 'GET',
    }).then(response => response.json())
        .then(players => {
            const playerTable = document.getElementById("player_table");
            const tbody = playerTable.getElementsByTagName('tbody')[0];
            tbody.innerHTML = '';

            players.forEach(player => {
                const row = document.createElement('tr');
                row.innerHTML = `
            <td>${player.username}</td>
            <td>${player.password}</td>
            <td>
                <button onclick="editPlayer(${player.id})">Edit</button>
                <button onclick="deletePlayer(${player.id})">Delete</button>
            </td>
            `;
                tbody.appendChild(row)

            })
        })
}

function createPlayer(){
    var username = document.getElementById('username').value
    var password = document.getElementById('password').value
    var data = { 
        'username' : username,
        'password' : password
    }
    fetch ('/players',{
        method : 'POST', 
        body : JSON.stringify(data),
        headers : {
            'Content-Type':'application/json'    //{}//

        }}).then(response=>response.text()
        ).then(response =>{
            if (response==='SUCCESS'){
                alert(response)
            }
            else {
                alert('ERROR')
            }
        })
    
}

function deletePlayer(id){
    fetch (`/players/delete/${id}`,{
        method : 'DELETE'
        }).then(response=>response.text()
        ).then(response =>{
            if (response==='SUCCESS'){
                alert(response)
            }
            else {
                alert('ERROR')
            }
        })
}

function editPlayer(id){
    var username = document.getElementById('username').value
    var password = document.getElementById('password').value
    var data = { 
        'username' : username,
        'password' : password
    }
    fetch (`/players/${id}`,{
        method : 'PUT',
        body : JSON.stringify(data),
        headers : {
            'Content-Type':'application/json'
        }}).then(response=>response.text()
        ).then(response =>{
            if (response==='SUCCESS'){
                alert(response)
            }
            else {
                alert('ERROR')
            }
        })
}




fetchPlayer()

