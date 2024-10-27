
const register_button = document.getElementById("register_button");
const login_button = document.getElementById("login_button");
const register_wrapper = document.getElementById("register_wrapper");
const login_wrapper = document.getElementById("login_wrapper");

register_button.onclick = function() {
    login_wrapper.style.display = "none";
    register_wrapper.style.display = "flex";

    register_button.style.backgroundColor = "gray";
    login_button.style.backgroundColor = "white";

    console.log("Open Register Window")
};

login_button.onclick = function() {
    register_wrapper.style.display = "none";
    login_wrapper.style.display = "flex";

    login_button.style.backgroundColor = "gray";
    register_button.style.backgroundColor = "white";

    console.log("Open Login window")
};

const host = "127.0.0.1";
const users_port = 8080;
const auth_port = 8081;
const messages_port = 8082;


const register_form = document.getElementById("register_form");
const login_form = document.getElementById("login_form");


register_form.addEventListener("submit", event => {
    event.preventDefault();

    const form_data = new FormData(register_form);

    fetch('http://'+host+'/users/create_user/', {
        method: "POST",
        body: form_data
    })
    .then(response => response.json())
    .then(result => console.log(result));
})

login_form.addEventListener("submit", event => {
    event.preventDefault();

    const form_data = new FormData(login_form);

    fetch('http://'+host+'/auth/login/', {
        method: "POST",
        body: form_data
    })
    .then(response => response.json())
    .then(result => console.log(result));
})
