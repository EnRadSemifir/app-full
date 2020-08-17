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

    myHeaders.append('Access-Control-Allow-Origin', '*')

    fetch('http://127.0.0.1:5000/api/users', {
        method: 'POST',
        body: JSON.stringify(user),
        headers: myHeaders
    }).then(resp => resp.json()).then(user => console.log(user))
}

document.querySelector('#registerForm').addEventListener('submit', submit)