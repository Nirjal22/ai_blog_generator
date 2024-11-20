// const username = document.getElementById("usernameInput");
// const password = document.getElementById("passwordInput");
// const button = document.getElementById("signupBtn");

// button.addEventListener("click", (event) => {
//     // Prevent form submission if validation fails
//     event.preventDefault();

//     // Check if both username and password are not empty
//     if (username.value.trim() !== "" && password.value.trim() !== "") {
//         const gmailRegex = /^[a-zA-Z0-9._%+-]+@gmail\.com$/;
        
//         // Validate Gmail address format and password length
//         if (gmailRegex.test(username.value.trim()) && password.value.length >= 6) {
//             alert("Registration successful!");
//             // Proceed to submit form or handle further logic, e.g., redirect to another page
//             // window.location.assign("{% url 'signout' %}");
//         } else {
//             alert("Enter a valid Gmail address and ensure password is at least 6 characters.");
//         }
//     } else {
//         alert("Please enter both username and password.");
//     }
// });
