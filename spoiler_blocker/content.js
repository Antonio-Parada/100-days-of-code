const spoilerKeywords = ["spoiler", "ending", "death", "killed", "revealed"];

function blurSpoilers(node) {
    if (node.nodeType === Node.TEXT_NODE) {
        let content = node.textContent;
        let originalContent = content;

        for (const keyword of spoilerKeywords) {
            const regex = new RegExp(`\\b${keyword}\\b`, 'gi');
            content = content.replace(regex, match => `<span class="spoiler-blurred">${match}</span>`);
        }

        if (content !== originalContent) {
            const span = document.createElement('span');
            span.innerHTML = content;
            node.parentNode.replaceChild(span, node);
        }
    } else if (node.nodeType === Node.ELEMENT_NODE) {
        if (node.tagName !== 'SCRIPT' && node.tagName !== 'STYLE') {
            for (const child of node.childNodes) {
                blurSpoilers(child);
            }
        }
    }
}

// Apply blurring to the entire body when the page loads
blurSpoilers(document.body);

// Add CSS for blurring
const style = document.createElement('style');
style.textContent = `
    .spoiler-blurred {
        filter: blur(5px);
        transition: filter 0.3s ease;
    }
    .spoiler-blurred:hover {
        filter: blur(0);
    }
`;
document.head.appendChild(style);
