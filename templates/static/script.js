document.getElementById('letter-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData();
    const fileInput = document.getElementById('letter-file');
    formData.append('letter_file', fileInput.files[0]);

    fetch('/grade', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        const gradingResult = document.getElementById('grading-result');

        if (data.grading_result) {
            gradingResult.textContent = data.grading_result;
            resultDiv.classList.remove('hidden');
        } else {
            gradingResult.textContent = `Error: ${data.error}`;
            resultDiv.classList.remove('hidden');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
