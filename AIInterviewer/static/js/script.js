const video = document.getElementById('video')


let totalTime = 0; // 总时间（秒）
let positiveScore = 0; // 积极情绪的初始分数
let negativeScore = 0; // 消极情绪的初始分数
const maxTotalScore = 18; // 最高总分
let timerInterval; // 定时器引用

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri('./AIInterviewer/models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('./AIInterviewer/models'),
  faceapi.nets.faceRecognitionNet.loadFromUri('./AIInterviewer/models'),
  faceapi.nets.faceExpressionNet.loadFromUri('./AIInterviewer/models')
]).then(startVideo);

function startVideo() {
  navigator.getUserMedia(
    { video: {} },
    stream => video.srcObject = stream,
    err => console.error(err)
  )
}

video.addEventListener('play', () => {
  const canvas = faceapi.createCanvasFromMedia(video);
  document.body.append(canvas);
  const displaySize = { width: video.width, height: video.height };
  faceapi.matchDimensions(canvas, displaySize);
  timerInterval = setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions();
    const resizedDetections = faceapi.resizeResults(detections, displaySize);
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
    faceapi.draw.drawDetections(canvas, resizedDetections);
    faceapi.draw.drawFaceLandmarks(canvas, resizedDetections);
    faceapi.draw.drawFaceExpressions(canvas, resizedDetections);

  }, 1000); // 1000 毫秒 = 1 秒
  })

