document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('pathfindingCanvas');
    const ctx = canvas.getContext('2d');
    const startBtn = document.getElementById('startBtn');
    const resetBtn = document.getElementById('resetBtn');

    const COLS = 25;
    const ROWS = 25;
    const CELL_SIZE = 20;
    canvas.width = COLS * CELL_SIZE;
    canvas.height = ROWS * CELL_SIZE;

    let grid = [];
    let startNode = { row: 12, col: 5 };
    let endNode = { row: 12, col: 19 };
    let obstacles = [];

    function initializeGrid() {
        grid = Array(ROWS).fill(0).map(() => Array(COLS).fill(0));
        obstacles = [];
        // Add some random obstacles
        for (let i = 0; i < 70; i++) {
            const r = Math.floor(Math.random() * ROWS);
            const c = Math.floor(Math.random() * COLS);
            if (!((r === startNode.row && c === startNode.col) || (r === endNode.row && c === endNode.col))) {
                obstacles.push({ row: r, col: c });
                grid[r][c] = 1; // Mark as obstacle
            }
        }
        drawGrid();
    }

    function drawGrid() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                const x = c * CELL_SIZE;
                const y = r * CELL_SIZE;

                ctx.strokeStyle = '#ccc';
                ctx.strokeRect(x, y, CELL_SIZE, CELL_SIZE);

                if (grid[r][c] === 1) {
                    ctx.fillStyle = '#333'; // Obstacle
                    ctx.fillRect(x, y, CELL_SIZE, CELL_SIZE);
                } else if (r === startNode.row && c === startNode.col) {
                    ctx.fillStyle = 'green'; // Start
                    ctx.fillRect(x, y, CELL_SIZE, CELL_SIZE);
                } else if (r === endNode.row && c === endNode.col) {
                    ctx.fillStyle = 'red'; // End
                    ctx.fillRect(x, y, CELL_SIZE, CELL_SIZE);
                }
            }
        }
    }

    async function bfs() {
        const queue = [startNode];
        const visited = new Set();
        const parent = {};

        visited.add(`${startNode.row},${startNode.col}`);

        while (queue.length > 0) {
            const currentNode = queue.shift();

            if (currentNode.row === endNode.row && currentNode.col === endNode.col) {
                // Path found, reconstruct and draw
                let path = [];
                let curr = currentNode;
                while (curr) {
                    path.unshift(curr);
                    curr = parent[`${curr.row},${curr.col}`];
                }
                for (let i = 1; i < path.length - 1; i++) {
                    const node = path[i];
                    ctx.fillStyle = 'yellow';
                    ctx.fillRect(node.col * CELL_SIZE, node.row * CELL_SIZE, CELL_SIZE, CELL_SIZE);
                    ctx.strokeStyle = '#ccc';
                    ctx.strokeRect(node.col * CELL_SIZE, node.row * CELL_SIZE, CELL_SIZE, CELL_SIZE);
                    await new Promise(resolve => setTimeout(resolve, 50));
                }
                return;
            }

            const neighbors = [
                { row: currentNode.row - 1, col: currentNode.col }, // Up
                { row: currentNode.row + 1, col: currentNode.col }, // Down
                { row: currentNode.row, col: currentNode.col - 1 }, // Left
                { row: currentNode.row, col: currentNode.col + 1 }  // Right
            ];

            for (const neighbor of neighbors) {
                if (
                    neighbor.row >= 0 && neighbor.row < ROWS &&
                    neighbor.col >= 0 && neighbor.col < COLS &&
                    grid[neighbor.row][neighbor.col] !== 1 && // Not an obstacle
                    !visited.has(`${neighbor.row},${neighbor.col}`)
                ) {
                    visited.add(`${neighbor.row},${neighbor.col}`);
                    parent[`${neighbor.row},${neighbor.col}`] = currentNode;
                    queue.push(neighbor);

                    // Visualize visited nodes
                    if (!((neighbor.row === startNode.row && neighbor.col === startNode.col) || (neighbor.row === endNode.row && neighbor.col === endNode.col))) {
                        ctx.fillStyle = 'lightblue';
                        ctx.fillRect(neighbor.col * CELL_SIZE, neighbor.row * CELL_SIZE, CELL_SIZE, CELL_SIZE);
                        ctx.strokeStyle = '#ccc';
                        ctx.strokeRect(neighbor.col * CELL_SIZE, neighbor.row * CELL_SIZE, CELL_SIZE, CELL_SIZE);
                        await new Promise(resolve => setTimeout(resolve, 10));
                    }
                }
            }
        }
        console.log("No path found.");
    }

    startBtn.addEventListener('click', bfs);
    resetBtn.addEventListener('click', initializeGrid);

    initializeGrid();
});