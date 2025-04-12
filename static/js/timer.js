class Timer {
    constructor() {
        this.totalSeconds = 0;
        this.remainingSeconds = 0;
        this.isRunning = false;
        this.timerId = null;
        this.inputBuffer = "";

        this.canvas = document.getElementById('progressCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.playButton = document.getElementById('playButton');
        this.timeLabel = document.getElementById('timeLabel');

        this.setupEventListeners();
        this.resizeCanvas();
        this.drawProgress(1.0);
    }

    setupEventListeners() {
        window.addEventListener('resize', () => this.resizeCanvas());
        this.playButton.addEventListener('click', () => this.toggleTimer());
        document.addEventListener('keypress', (e) => this.handleKeyPress(e));
    }

    resizeCanvas() {
        this.canvas.width = this.canvas.offsetWidth;
        this.canvas.height = this.canvas.offsetHeight;
        this.drawProgress(this.remainingSeconds / this.totalSeconds || 1);
    }

    drawProgress(percentage) {
        const ctx = this.ctx;
        const width = this.canvas.width;
        const height = this.canvas.height;
        const padding = 20;
        
        ctx.clearRect(0, 0, width, height);
        
        // Background arc
        ctx.beginPath();
        ctx.arc(width/2, height/2, Math.min(width, height)/2 - padding, 0, 2 * Math.PI);
        ctx.fillStyle = '#222222';
        ctx.fill();
        
        // Progress arc
        if (percentage > 0) {
            ctx.beginPath();
            ctx.arc(width/2, height/2, Math.min(width, height)/2 - padding, 
                   -0.5 * Math.PI, (-0.5 + 2 * percentage) * Math.PI);
            ctx.lineTo(width/2, height/2);
            ctx.fillStyle = '#FFA500';
            ctx.fill();
        }
    }

    toggleTimer() {
        if (!this.isRunning && this.remainingSeconds > 0) {
            this.isRunning = true;
            this.playButton.textContent = "⏸";
            this.updateTimer();
        } else {
            this.isRunning = false;
            this.playButton.textContent = "▶";
            if (this.timerId) {
                clearTimeout(this.timerId);
            }
        }
    }

    updateTimer() {
        if (this.isRunning && this.remainingSeconds > 0) {
            this.remainingSeconds--;
            const minutes = Math.floor(this.remainingSeconds / 60);
            const seconds = this.remainingSeconds % 60;
            this.timeLabel.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
            
            const progress = this.remainingSeconds / this.totalSeconds;
            this.drawProgress(progress);
            
            this.timerId = setTimeout(() => this.updateTimer(), 1000);
        } else if (this.remainingSeconds <= 0) {
            this.isRunning = false;
            this.playButton.textContent = "▶";
            this.timeLabel.textContent = "00:00";
            this.drawProgress(1.0);
            // Play sound using Audio API
            const audio = new Audio('data:audio/wav;base64,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');
            audio.play();
        }
    }

    handleKeyPress(event) {
        if (/^\d$/.test(event.key)) {
            this.inputBuffer += event.key;
            if (this.inputBuffer.length >= 2) {
                const minutes = parseInt(this.inputBuffer);
                this.totalSeconds = minutes * 60;
                this.remainingSeconds = this.totalSeconds;
                const displayMinutes = Math.floor(this.remainingSeconds / 60);
                const displaySeconds = this.remainingSeconds % 60;
                this.timeLabel.textContent = 
                    `${String(displayMinutes).padStart(2, '0')}:${String(displaySeconds).padStart(2, '0')}`;
                this.inputBuffer = "";
                this.drawProgress(1.0);
            }
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new Timer();
});