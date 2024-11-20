// index page
const generate = document.getElementById("generateButton");
const input = document.getElementById("linkInput");
const loadingIndicator = document.getElementById("loadingIndicator");

if (generate !== null) {
    generate.addEventListener("click", () => {
        // Check if input is non-empty and contains a YouTube URL
        if (input && input.value.trim() !== "") {
            // A basic YouTube link validation (contains "youtube.com" or "youtu.be")
            const youtubeRegex = /^(https?\:\/\/)?(www\.)?(youtube|youtu)\.(com|be)\/.+$/;
            if (youtubeRegex.test(input.value.trim())) {
                alert("Valid YouTube link");
            } else {
                alert("Invalid YouTube link! Please enter a valid YouTube URL.");
            }
        } else {
            alert("Please enter a valid link!");
        }
    });
} else {
    alert("Generate button not found!");
}

