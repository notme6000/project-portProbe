

document.getElementById('myButton').addEventListener('click', () =>{
    pywebview.api.on_button_pressed();
});

document.getElementById('portScanner').addEventListener('click', () =>{
    window.location.href = 'port.html';
});

document.getElementById('vulnScanner').addEventListener('click', () =>{
    window.location.href = 'vuln.html';
});

// document.getElementById('goHome').addEventListener('click', () =>{
//     window.location.href = 'index.html'
// });
