document.addEventListener('DOMContentLoaded', function() {
    const deckContainer = document.getElementById('deck-container');
    const shuffleBtn = document.getElementById('shuffleBtn');

    let deck = [];
    const suits = ['♠', '♥', '♦', '♣'];
    const ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];

    function initializeDeck() {
        deck = [];
        for (const suit of suits) {
            for (const rank of ranks) {
                deck.push({ suit, rank });
            }
        }
        renderDeck();
    }

    function renderDeck() {
        deckContainer.innerHTML = '';
        deck.forEach(card => {
            const cardDiv = document.createElement('div');
            cardDiv.classList.add('card');
            cardDiv.textContent = `${card.rank}${card.suit}`;
            if (card.suit === '♥' || card.suit === '♦') {
                cardDiv.style.color = 'red';
            }
            deckContainer.appendChild(cardDiv);
        });
    }

    function fisherYatesShuffle(array) {
        let currentIndex = array.length,
            randomIndex;

        // While there remain elements to shuffle.
        while (currentIndex !== 0) {
            // Pick a remaining element.
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex--;

            // And swap it with the current element.
            [array[currentIndex], array[randomIndex]] = [
                array[randomIndex],
                array[currentIndex],
            ];
        }
        return array;
    }

    shuffleBtn.addEventListener('click', function() {
        fisherYatesShuffle(deck);
        renderDeck();
    });

    initializeDeck();
});