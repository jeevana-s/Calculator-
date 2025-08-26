const $display = document.querySelector('input[type="text"]');
const $buttons = document.querySelectorAll('input[type="button"]');

$buttons.forEach(($button) => {
    $button.addEventListener('click', () => {
        const value = $button.value;

        if (value === 'c' || value === 'C') { // Check for both lowercase and uppercase
            $display.value = '';
            return;
        }

        if (value === '=') {
            try {
                // Replace 'x' with '*' for multiplication
                const express = $display.value.replace(/x/g, '*');
                $display.value = eval(express);
            } catch (error) {
                $display.value = 'Error'; // Display error if eval fails
            }
            return;
        }

        $display.value += value; // Append the button value to the display
    });
});
// Event listeners to switch between calculators
document.getElementById('mathBtn').addEventListener('click', function() {
    document.getElementById('mathCalculator').style.display = 'block';
    document.getElementById('ageCalculator').style.display = 'none';
});

document.getElementById('ageBtn').addEventListener('click', function() {
    document.getElementById('ageCalculator').style.display = 'block';
    document.getElementById('mathCalculator').style.display = 'none';
});

// Math Calculator Function
function calculateMath() {
    const input = document.getElementById('mathInput').value;
    try {
        const result = eval(input); // Using existing code for math calculation
        document.getElementById('mathResult').textContent = `Result: ${result}`;
    } catch (error) {
        document.getElementById('mathResult').textContent = 'Invalid expression';
    }
}

// Age Calculator Function
function calculateAge() {
    const dobInput = document.getElementById('dobInput').value;
    if (!dobInput) {
        alert('Please enter your Date of Birth.');
        return;
    }
    const dob = new Date(dobInput);
    const today = new Date();
    let age = today.getFullYear() - dob.getFullYear();
    const monthDifference = today.getMonth() - dob.getMonth();
    if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < dob.getDate())) {
        age--;
    }
    document.getElementById('ageResult').textContent = `Your age is ${age} years.`;
}