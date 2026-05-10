// ==============================
// 🎨 SAMARTH - Frontend JavaScript
// Supportive AI Mentor for Academic Results & Talent Hunting
// ==============================

document.addEventListener('DOMContentLoaded', function() {

    // Toast Notification System
    function showToast(message, type = 'success') {
        const toast = document.createElement('div');
        toast.className = `fixed bottom-5 right-5 px-6 py-3 rounded-xl text-white shadow-2xl z-50 flex items-center gap-2
                           ${type === 'success' ? 'bg-green-500' : type === 'error' ? 'bg-red-500' : 'bg-blue-500'}`;
        toast.innerHTML = `
            <span>${message}</span>
        `;
        document.body.appendChild(toast);

        setTimeout(() => {
            toast.style.transition = 'all 0.4s';
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(20px)';
            setTimeout(() => toast.remove(), 400);
        }, 3000);
    }

    // Auto-show flash messages from Flask
    const flashes = document.querySelectorAll('.flash');
    flashes.forEach(flash => {
        showToast(flash.textContent, flash.classList.contains('error') ? 'error' : 'success');
        flash.remove();
    });

    // Smooth scrolling for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Chatbot Send Message
    const chatForm = document.getElementById('chat-form');
    if (chatForm) {
        chatForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            const input = document.getElementById('chat-input');
            const message = input.value.trim();
            if (!message) return;

            // Add user message
            addChatMessage(message, 'user');
            input.value = '';

            // Show typing indicator
            const typing = document.getElementById('typing');
            if (typing) typing.classList.remove('hidden');

            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: message })
                });

                const data = await response.json();
                
                if (typing) typing.classList.add('hidden');
                addChatMessage(data.reply, 'bot');
            } catch (error) {
                if (typing) typing.classList.add('hidden');
                addChatMessage("Sorry, I'm having trouble responding right now.", 'bot');
            }
        });
    }

    // Add message to chat
    function addChatMessage(text, sender) {
        const chatContainer = document.getElementById('chat-messages');
        if (!chatContainer) return;

        const messageDiv = document.createElement('div');
        messageDiv.className = `flex ${sender === 'user' ? 'justify-end' : 'justify-start'} mb-4`;
        
        messageDiv.innerHTML = `
            <div class="${sender === 'user' ? 
                'bg-cyan-600 text-white' : 
                'bg-slate-700 text-white'} 
                max-w-[75%] rounded-2xl px-5 py-3">
                ${text}
            </div>
        `;
        chatContainer.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    // Practice Form AJAX
    const practiceForm = document.getElementById('practice-form');
    if (practiceForm) {
        practiceForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            
            try {
                const response = await fetch('/practice', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                
                // Display questions (you can enhance this)
                console.log("Practice Questions:", data);
                alert(data.message || "Questions generated successfully!");
            } catch (err) {
                alert("Error generating questions");
            }
        });
    }

    // Progress Bar Animation
    function animateProgress() {
        const progressBars = document.querySelectorAll('.progress-fill');
        progressBars.forEach(bar => {
            const width = bar.getAttribute('data-width') || 75;
            bar.style.width = width + '%';
        });
    }

    // Run animations when page loads
    setTimeout(animateProgress, 800);

    // Keyboard shortcut for chatbot (Ctrl + K)
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'k') {
            e.preventDefault();
            const chatInput = document.getElementById('chat-input');
            if (chatInput) chatInput.focus();
        }
    });

    console.log('%c✅ SAMARTH AI Loaded Successfully!', 'color: #22d3ee; font-size: 16px; font-weight: bold');
});