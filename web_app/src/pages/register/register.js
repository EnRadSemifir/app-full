const submit = (event) => {
    event.preventDefault()
    const user = {}
    const form = event.target
    for (input of form) {
        if (input.id !== "") {
            user[input.id] = input.value
        }
    }

    const myHeaders = new Headers()
    myHeaders.append('Content-Type', 'application/json')

    fetch('http://192.168.99.100:5000/api/users/', {
        method: "POST",
        body: JSON.stringify(user),
        headers: myHeaders
    }).then(resp => resp.json()).then(user => console.log(user))
}

document.querySelector('#registerForm').addEventListener('submit', submit)