document.addEventListener('DOMContentLoaded', function() {
    // Get range sliders
    const slider1 = document.getElementById('slider1');
    const slider2 = document.getElementById('slider2');
    const slider3 = document.getElementById('slider3');
    const slider4 = document.getElementById('slider4');
    const slider5 = document.getElementById('slider5');
    const slider6 = document.getElementById('slider6');

    // Get values of number display elements
    const slider1Value = document.getElementById('slider1-value');
    const slider2Value = document.getElementById('slider2-value');
    const slider3Value = document.getElementById('slider3-value');
    const slider4Value = document.getElementById('slider4-value');
    const slider5Value = document.getElementById('slider5-value');
    const slider6Value = document.getElementById('slider6-value');

    // Display initial value
    slider1Value.textContent = slider1.value;
    slider2Value.textContent = slider2.value;
    slider3Value.textContent = slider3.value;
    slider4Value.textContent = slider4.value;
    slider5Value.textContent = slider5.value;
    slider6Value.textContent = slider6.value;

    // Add event listeners to update the value displays
    slider1.addEventListener('input', function () {
        slider1Value.textContent = slider1.value;
        
    });
    slider2.addEventListener('input', function () {
        slider2Value.textContent = slider2.value;
    });

    slider3.addEventListener('input', function () {
        slider3Value.textContent = slider3.value;
    });

    slider4.addEventListener('input', function () {
        slider4Value.textContent = slider4.value;
    });
    
    slider5.addEventListener('input', function () {
        slider5Value.textContent = slider5.value;
    });

    slider6.addEventListener('input', function () {
        slider6Value.textContent = slider6.value;
    });

    // Add event listeners to allow manual editing
    slider1Value.addEventListener('click', function() {
        const newValue = prompt('Enter a new value:', slider1.value);
        if (newValue!=null) {
            slider1.value = newValue;
            slider1Value.textContent = newValue;
        }
    });

    slider2Value.addEventListener('click', function() {
        const newValue = prompt('Enter a new value:', slider2.value);
        if (newValue!=null) {
            slider2.value = newValue;
            slider2Value.textContent = newValue;
        }
    });

    slider3Value.addEventListener('click', function() {
        const newValue = prompt('Enter a new value:', slider3.value);
        if (newValue!=null) {
            slider3.value = newValue;
            slider3Value.textContent = newValue;
        }
    });

    slider4Value.addEventListener('click', function() {
        const newValue = prompt('Enter a new value:', slider4.value);
        if (newValue!=null) {
            slider4.value = newValue;
            slider4Value.textContent = newValue;
        }
    });

    slider5Value.addEventListener('click', function() {
        const newValue = prompt('Enter a new value:', slider5.value);
        if (newValue!=null) {
            slider5.value = newValue;
            slider5Value.textContent = newValue;
        }
    });

    slider6Value.addEventListener('click', function() {
        const newValue = prompt('Enter a new value:', slider6.value);
        if (newValue!=null) {
            slider6.value = newValue;
            slider6Value.textContent = newValue;
        }
    });
})