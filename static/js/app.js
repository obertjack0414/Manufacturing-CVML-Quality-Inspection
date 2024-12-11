document.addEventListener("DOMContentLoaded", function () {
    const captureBtn = document.getElementById("capture-btn");
    const annotatedImage = document.getElementById("annotated-image");

    captureBtn.addEventListener("click", async () => {
        captureBtn.disabled = true;
        captureBtn.textContent = "Processing...";
        try {
            const response = await fetch("/capture-and-infer", { method: "POST" });
            if (!response.ok) throw new Error("Failed to fetch data from server");

            const data = await response.json();
            if (data.annotated_image_url) {
                annotatedImage.src = data.annotated_image_url;
            } else {
                throw new Error("No annotated image URL in response");
            }
        } catch (error) {
            console.error("Error during inference:", error);
        } finally {
            captureBtn.disabled = false;
            captureBtn.textContent = "Capture and Infer";
        }
    });
});


