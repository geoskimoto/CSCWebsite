document.addEventListener('DOMContentLoaded', () => {
    const sections = [
        {
            id: 'home',
            content: '<h1>Welcome to Cascade Ski Club</h1><p>Founded in 1928 by Norwegian ski jumpers, Cascade Ski Club is one of America’s oldest ski clubs...</p>'
        },
        {
            id: 'rates',
            content: '<h2>Rates</h2><p>Bunk Rates (for Membership Rates click here)</p><ul><li>Adult Member: $20.-</li><li>Child Member (18 and younger): $12.-</li><li>Guests: $35.-</li><li>Private Room: $85.-</li></ul><p>Note: You need to be a member to stay at the lodge. Guests can try out the lodge once...</p>'
        },
        {
            id: 'membership',
            content: '<h2>Membership</h2><p>Cascade Ski Club (CSC) is a private, non-profit club dedicated to supporting affordable and accessible...</p>'
        },
        {
            id: 'amenities',
            content: '<h2>Lodge Amenities</h2><p>Members feel at home lounging on one of the couches in front of the cozy fireplace...</p>'
        },
        {
            id: 'history',
            content: '<h2>Club History</h2><p>With a tradition that is over 90 years old, Cascade Ski Club holds a special place in American Ski history...</p>'
        }
    ];

    let currentSectionIndex = 0;

    function loadMoreContent() {
        if (currentSectionIndex < sections.length) {
            const section = document.createElement('section');
            section.id = sections[currentSectionIndex].id;
            section.className = 'section';
            section.innerHTML = sections[currentSectionIndex].content;
            document.querySelector('main').appendChild(section);
            currentSectionIndex++;
        }
    }

    window.addEventListener('scroll', () => {
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
            loadMoreContent();
        }
    });

    loadMoreContent();  // Load the first section
});
