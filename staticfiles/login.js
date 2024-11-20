const username = document.getElementById("usernameInput");
const password = document.getElementById("passwordInput");
const button = document.getElementById("loginBtn");


button.addEventListener("click", (event) => {

    // Prevent form submission if validation fails
    event.preventDefault();

    console.log("I am triggre")
    // Check if both username and password are not empty
    if (username.value.trim() !== "" || password.value.trim() !== "") {
        const gmailRegex = /^[a-zA-Z0-9._%+-]+@gmail\.com$/;
        if (gmailRegex.test(username.value.trim())) {
            alert("Logged in");
            // window.location.assign("{% url 'signout' %}");
        }else{
            alert("Enter a valid username.");
        }
    } else {
        alert("Enter username and password");
        // Proceed with form submission or further logic here
    }
});
