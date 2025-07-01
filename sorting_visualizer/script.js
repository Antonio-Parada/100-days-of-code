document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('sortingCanvas');
    const ctx = canvas.getContext('2d');
    const startSortBtn = document.getElementById('startSortBtn');
    const resetBtn = document.getElementById('resetBtn');

    const CANVAS_WIDTH = 800;
    const CANVAS_HEIGHT = 400;
    canvas.width = CANVAS_WIDTH;
    canvas.height = CANVAS_HEIGHT;

    const BAR_WIDTH = 5;
    let data = [];
    let isSorting = false;

    function initializeData() {
        data = [];
        for (let i = 0; i < CANVAS_WIDTH / BAR_WIDTH; i++) {
            data.push(Math.floor(Math.random() * CANVAS_HEIGHT) + 1);
        }
        drawBars();
    }

    function drawBars(highlightedIndices = []) {
        ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
        for (let i = 0; i < data.length; i++) {
            const barHeight = data[i];
            const x = i * BAR_WIDTH;
            const y = CANVAS_HEIGHT - barHeight;

            ctx.fillStyle = highlightedIndices.includes(i) ? 'red' : 'blue';
            ctx.fillRect(x, y, BAR_WIDTH, barHeight);
        }
    }

    async function bubbleSort() {
        isSorting = true;
        const n = data.length;
        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - i - 1; j++) {
                drawBars([j, j + 1]); // Highlight comparing bars
                await new Promise(resolve => setTimeout(resolve, 10)); // Small delay for visualization

                if (data[j] > data[j + 1]) {
                    [data[j], data[j + 1]] = [data[j + 1], data[j]]; // Swap
                }
            }
        }
        drawBars(); // Draw final sorted state
        isSorting = false;
    }

    startSortBtn.addEventListener('click', function() {
        if (!isSorting) {
            bubbleSort();
        }
    });

    resetBtn.addEventListener('click', function() {
        isSorting = false;
        initializeData();
    });

    initializeData();
});