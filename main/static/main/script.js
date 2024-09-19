console.log('Hello, world')

var modal = document.getElementById('loginModal');
var btn = document.getElementById('btn_video');
var video = document.getElementById('video');

btn.addEventListener('click', function() {
    modal.style.display = 'block';
});
window.addEventListener('click', function(event) {
    if(event.target == modal) {
        modal.style.display = 'none';
        video.pause();
        video.currentTime = 0;
    }
});
