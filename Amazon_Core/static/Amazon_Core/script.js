var slideInterval = 2000;

function getFigures() {
    return document.getElementById('ccc').getElementsByTagName('figure');
}

function moveForward() {
    var pointer;
    var figures = getFigures();
    for (var i = 0; i < figures.length; i++) {
        if (figures[i].className == 'sss') {
            figures[i].className = '';
            pointer = i;
        }
    }
    if (++pointer == figures.length) {
        pointer = 0;
    }
    figures[pointer].className = 'sss';
    setTimeout(moveForward, slideInterval);
}


function startPlayback() {
    setTimeout(moveForward, slideInterval);
}

startPlayback();