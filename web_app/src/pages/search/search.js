const users = [
    { lastname: 'Radnaï', firstname: 'Enzo', birth: "12/10/1989", },
    { lastname: 'Doe', firstname: 'John', birth: "99/99/9999", },
]

const searchUser = () => {
    const user = document.querySelector("#searchInput").value
    console.log('user : ', user)
}

const renderUsers = () => {
    const table = document.querySelector('#userTable')
    for (user of users) {
        const tr = table.insertRow()
        for (key in user) {
            let cell = tr.insertCell()
            cell.innerHTML = user[key]
        }
    }
}

document.querySelector("#searchButton").addEventListener('click', searchUser)
renderUsers()