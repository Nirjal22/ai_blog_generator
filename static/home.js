document.getElementById('generateButton').addEventListener('click', async () => {
    const input = document.getElementById("linkInput").value;

    if (!input) {
        alert("Please enter a valid YouTube link.");
        return;
    }

    // Trigger the backend with the YouTube link
    await sendLinkToBackend(input);
});

async function sendLinkToBackend(link) {
    const loadingIndicator = document.getElementById("loadingIndicator");
    const generatedContent = document.getElementById("generated_content");

    // Show a loading indicator while processing
    // loadingIndicator.style.display = 'block';

    try{
        
    }catch(error){console.log("some error");}

}