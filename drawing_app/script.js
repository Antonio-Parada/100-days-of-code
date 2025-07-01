document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('drawingCanvas');
    const ctx = canvas.getContext('2d');
    const colorPicker = document.getElementById('colorPicker');
    const brushSize = document.getElementById('brushSize');
    const clearCanvasBtn = document.getElementById('clearCanvas');
    const saveDrawingBtn = document.getElementById('saveDrawing');

    let isDrawing = false;
    let lastX = 0;
    let lastY = 0;

    // Set initial canvas size
    canvas.width = 800;
    canvas.height = 600;

    // Set initial drawing properties
    ctx.strokeStyle = colorPicker.value;
    ctx.lineWidth = brushSize.value;
    ctx.lineJoin = 'round';
    ctx.lineCap = 'round';

    function draw(e) {
        if (!isDrawing) return;
        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(e.offsetX, e.offsetY);
        ctx.stroke();
        [lastX, lastY] = [e.offsetX, e.offsetY];
    }

    canvas.addEventListener('mousedown', (e) => {
        isDrawing = true;
        [lastX, lastY] = [e.offsetX, e.offsetY];
    });

    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', () => isDrawing = false);
    canvas.addEventListener('mouseout', () => isDrawing = false);

    colorPicker.addEventListener('change', (e) => {
        ctx.strokeStyle = e.target.value;
    });

    brushSize.addEventListener('change', (e) => {
        ctx.lineWidth = e.target.value;
    });

    clearCanvasBtn.addEventListener('click', () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    });

    saveDrawingBtn.addEventListener('click', () => {
        const dataURL = canvas.toDataURL('image/png');
        const a = document.createElement('a');
        a.href = dataURL;
        a.download = 'my_drawing.png';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    });
});