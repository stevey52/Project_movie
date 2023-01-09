function toggleVideo(){
  const trailer = document.querySelector('.trailer');
  const video = document.querySelector('iframe');
  trailer.classList.toggle('active')
  video.currentTime = 0;
  video.pause();
}

function closeIframe(){
  const trailer = document.querySelector('.trailer')
  const frame = document.querySelector('iframe')
  trailer.classList.toggle('active')
  frame.parentNode.removeChild(frame)

}
