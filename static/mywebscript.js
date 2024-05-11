let runAddition = () => {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);

    if (isNaN(num1) || isNaN(num2)) {
        alert("Please enter valid numerical values for num1 and num2.");
        return;
    }

    let result = num1 + num2;
    document.getElementById("system_response").innerHTML = "Result: " + result;
};

let runSubtraction = () => {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);

    if (isNaN(num1) || isNaN(num2)) {
        alert("Please enter valid numerical values for num1 and num2.");
        return;
    }

    let result = num1 - num2;
    document.getElementById("system_response").innerHTML = "Result: " + result;
};

let runMultiplication = () => {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);

    if (isNaN(num1) || isNaN(num2)) {
        alert("Please enter valid numerical values for num1 and num2.");
        return;
    }

    let result = num1 * num2;
    document.getElementById("system_response").innerHTML = "Result: " + result;
};
