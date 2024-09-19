console.log('Hello, world')

document.querySelectorAll('.btn_video').forEach(function(image, index) {
    image.addEventListener('click', function() {
        let videoSource = this.getAttribute('data-video-src');

        let modal = document.getElementById('modal_' + (index + 1));

        modal.querySelector('video').src = videoSource;

        modal.style.display = 'block';


        modal.onclick = function(event) {
            if (event.target === modal) {
                modal.style.display = 'none';
                modal.querySelector('video').pause();
            }
        };
    });
});


