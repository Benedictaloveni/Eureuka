document.getElementById('run-matlab').addEventListener('click', function() {
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;

    fetch('/run-matlab', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name, age: age, num1: num1, num2: num2 })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = `Halo ${name}, usia ${age}. Hasil kalkulasi: ${data.output}`;
    })
    .catch(error => console.error('Error:', error));
});
