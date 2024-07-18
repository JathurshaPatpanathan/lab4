document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const Length1 = document.getElementById('Length1').value;
    const Length2 = document.getElementById('Length2').value;
    const Length3 = document.getElementById('Length3').value;
    const Height = document.getElementById('Height').value;
    const Width = document.getElementById('Width').value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ Length1, Length2, Length3, Height, Width })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(err.error); });
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('result').innerText = 'Predicted Weight: ' + data.prediction;
    })
    .catch(error => {
        document.getElementById('result').innerText = 'Error: ' + error.message;
    });
});
