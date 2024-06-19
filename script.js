let display = document.getElementById('display');

function appendToDisplay(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = '';
}

function calculate() {
    try {
        display.value = eval(display.value);
        clearAfterInterval();
    } catch (error) {
        display.value = 'Error';
        clearAfterInterval();
    }
}

function clearAfterInterval() {
    setTimeout(function() {
        clearDisplay();
    }, 3000); 
}
