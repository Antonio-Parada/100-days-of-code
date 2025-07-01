// This is a placeholder for background script functionality.
// For a simple spoiler blocker, most logic resides in the content script.
// Background scripts can be used for: 
// - Handling browser actions (e.g., clicking the extension icon)
// - Managing settings
// - Making network requests not allowed from content scripts

console.log("Spoiler Blocker background script loaded.");

// Example: Listen for when the extension icon is clicked
chrome.action.onClicked.addListener((tab) => {
    console.log("Extension icon clicked!");
    // You could send a message to the content script here to toggle blurring
    // chrome.tabs.sendMessage(tab.id, { action: "toggleBlur" });
});
