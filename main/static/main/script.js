console.log('Hello, world')

video = document.getElementById("video")
let body = document.body; // добавьте эту строку

function btn_video() {
    if(video) { // проверка на существование видео
        video.style.display = 'block';
    } else {
        console.error("Video element not found.");
    }
}

