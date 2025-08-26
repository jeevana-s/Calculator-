function calculateAge() {
    const birthdateInput = document.getElementById('birthdate').value;
    const resultElement = document.getElementById('result');

    if (!birthdateInput) {
        resultElement.textContent = "Please enter a valid birthdate.";
        return;
    }

    const birthDate = new Date(birthdateInput);
    const today = new Date();

    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDifference = today.getMonth() - birthDate.getMonth();

    // Adjust age if the birthdate hasn't occurred yet this year
    if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }

    resultElement.textContent = `Your age is ${age} years.`;
}