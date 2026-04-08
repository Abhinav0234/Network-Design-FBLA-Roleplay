// ==================== Navigation ====================
const mobileToggle = document.querySelector('.mobile-toggle');
const navLinks = document.querySelector('.nav-links');
mobileToggle.addEventListener('click', () => navLinks.classList.toggle('open'));

document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => navLinks.classList.remove('open'));
});

// Active nav link on scroll
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
  const scrollY = window.scrollY + 120;
  sections.forEach(sec => {
    const top = sec.offsetTop, height = sec.offsetHeight, id = sec.getAttribute('id');
    const link = document.querySelector('.nav-links a[href="#' + id + '"]');
    if (link) {
      if (scrollY >= top && scrollY < top + height) link.classList.add('active');
      else link.classList.remove('active');
    }
  });
});

// ==================== Scroll Reveal ====================
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); } });
}, { threshold: 0.1 });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

// ==================== Accordions ====================
document.querySelectorAll('.accordion-header').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.parentElement;
    const isOpen = item.classList.contains('open');
    // Close siblings
    item.parentElement.querySelectorAll('.accordion-item').forEach(i => i.classList.remove('open'));
    if (!isOpen) item.classList.add('open');
  });
});

// ==================== Tabs ====================
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const group = btn.closest('.tab-section');
    group.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    group.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    group.querySelector('#' + btn.dataset.tab).classList.add('active');
  });
});

// ==================== Quiz ====================
const quizData = [
  { q: "Which OSI layer is responsible for routing and forwarding packets?", opts: ["Data Link Layer", "Network Layer", "Transport Layer", "Session Layer"], ans: 1 },
  { q: "What protocol translates domain names to IP addresses?", opts: ["DHCP", "FTP", "DNS", "SNMP"], ans: 2 },
  { q: "Which topology connects every device to every other device?", opts: ["Star", "Bus", "Ring", "Mesh"], ans: 3 },
  { q: "What port does HTTPS typically use?", opts: ["80", "21", "443", "3389"], ans: 2 },
  { q: "Which device operates at Layer 2 of the OSI model?", opts: ["Router", "Hub", "Switch", "Modem"], ans: 2 },
  { q: "What does DHCP stand for?", opts: ["Domain Host Control Protocol", "Dynamic Host Configuration Protocol", "Dynamic Hypertext Control Protocol", "Direct Host Configuration Protocol"], ans: 1 },
  { q: "Which protocol provides reliable, ordered delivery of data?", opts: ["UDP", "TCP", "ICMP", "ARP"], ans: 1 },
  { q: "What is the purpose of a firewall?", opts: ["Speed up network traffic", "Assign IP addresses", "Filter incoming/outgoing network traffic", "Convert digital to analog signals"], ans: 2 },
  { q: "What subnet mask provides 254 usable hosts?", opts: ["255.255.255.0", "255.255.0.0", "255.255.255.128", "255.255.255.192"], ans: 0 },
  { q: "Which wireless standard offers the fastest speeds?", opts: ["802.11a", "802.11g", "802.11n", "802.11ax (Wi-Fi 6)"], ans: 3 },
  { q: "What type of cable is MOST resistant to electromagnetic interference?", opts: ["Cat5e UTP", "Coaxial", "Fiber optic", "Cat6 STP"], ans: 2 },
  { q: "Which security model never implicitly trusts any user or device?", opts: ["Perimeter Security", "Zero Trust", "Defense in Depth", "Network Segmentation"], ans: 1 },
];

let currentQuiz = 0, quizScore = 0, quizAnswered = 0;
const quizContainer = document.getElementById('quiz-area');
const quizStatus = document.getElementById('quiz-status');

function renderQuiz() {
  if (currentQuiz >= quizData.length) {
    quizContainer.innerHTML = `<div class="quiz-result">
      <p style="color:var(--text-muted);margin-bottom:0.5rem;">Your Score</p>
      <div class="score">${quizScore}/${quizData.length}</div>
      <p style="color:var(--text-secondary);margin:1rem 0;">${quizScore >= 10 ? "Outstanding! You're ready to compete! 🏆" : quizScore >= 7 ? "Great job! Keep studying the areas you missed. 💪" : "Keep studying — review the sections above and try again! 📚"}</p>
      <button class="btn btn-primary" onclick="resetQuiz()">Try Again</button>
    </div>`;
    quizStatus.textContent = '';
    return;
  }
  const q = quizData[currentQuiz];
  quizStatus.textContent = `Question ${currentQuiz + 1} of ${quizData.length}`;
  quizContainer.innerHTML = `<div class="quiz-question">
    <h4>Q${currentQuiz + 1}. ${q.q}</h4>
    <div class="quiz-options">
      ${q.opts.map((o, i) => `<div class="quiz-option" data-idx="${i}">${o}</div>`).join('')}
    </div>
  </div>`;

  quizContainer.querySelectorAll('.quiz-option').forEach(opt => {
    opt.addEventListener('click', () => {
      const idx = parseInt(opt.dataset.idx);
      quizContainer.querySelectorAll('.quiz-option').forEach(o => {
        o.classList.add('disabled');
        if (parseInt(o.dataset.idx) === q.ans) o.classList.add('correct');
      });
      if (idx !== q.ans) opt.classList.add('wrong');
      else quizScore++;
      quizAnswered++;
      setTimeout(() => { currentQuiz++; renderQuiz(); }, 1200);
    });
  });
}

function resetQuiz() { currentQuiz = 0; quizScore = 0; quizAnswered = 0; renderQuiz(); }
renderQuiz();

// ==================== Flashcards ====================
const flashcards = [
  { front: "What is the OSI Model?", back: "A 7-layer conceptual framework that standardizes network communication: Physical, Data Link, Network, Transport, Session, Presentation, Application." },
  { front: "TCP vs UDP?", back: "TCP is connection-oriented, reliable, and ordered. UDP is connectionless, faster, but doesn't guarantee delivery. TCP is used for web/email; UDP for streaming/gaming." },
  { front: "What does a Router do?", back: "Routes packets between different networks using IP addresses. Operates at Layer 3 (Network) of the OSI model. Makes forwarding decisions based on routing tables." },
  { front: "What is Subnetting?", back: "Dividing a larger network into smaller sub-networks to improve performance and security. Uses subnet masks like 255.255.255.0 (/24) to define network boundaries." },
  { front: "Star Topology", back: "All devices connect to a central hub/switch. Easy to manage and troubleshoot. Single point of failure at the central device. Most common in modern LANs." },
  { front: "What is a VLAN?", back: "Virtual LAN — logically segments a physical network into separate broadcast domains. Improves security and performance without requiring separate physical infrastructure." },
  { front: "What is Zero Trust?", back: "A security model that requires verification for every access request, regardless of location. 'Never trust, always verify.' Minimizes attack surface through micro-segmentation." },
  { front: "DHCP Process", back: "DORA: Discover → Offer → Request → Acknowledge. Client broadcasts a discover message, server offers an IP, client requests it, server acknowledges the lease." },
  { front: "What is a VPN?", back: "Virtual Private Network — creates an encrypted tunnel over a public network. Provides secure remote access to a private network. Uses protocols like IPSec, OpenVPN, WireGuard." },
  { front: "Fiber vs Copper Cabling", back: "Fiber: uses light, faster (up to 100Gbps), immune to EMI, longer distances, more expensive. Copper: uses electrical signals, cheaper, easier to install, limited distance (~100m for Cat6)." },
  { front: "What is DNS?", back: "Domain Name System — translates human-readable domain names (google.com) to IP addresses (142.250.x.x). Uses port 53. Hierarchical with root servers, TLD servers, and authoritative servers." },
  { front: "What is Network Segmentation?", back: "Dividing a network into isolated zones to contain threats, improve performance, and enforce access control. Achieved through VLANs, subnets, and firewalls." },
];

let currentCard = 0;
const flashcard = document.getElementById('flashcard');
const cardFront = document.getElementById('card-front');
const cardBack = document.getElementById('card-back');
const cardCounter = document.getElementById('card-counter');

function renderCard() {
  const c = flashcards[currentCard];
  cardFront.innerHTML = `<p style="color:var(--accent-cyan);font-size:0.8rem;margin-bottom:1rem;">CLICK TO FLIP</p><h4>${c.front}</h4>`;
  cardBack.innerHTML = `<p style="color:var(--accent-emerald);font-size:0.8rem;margin-bottom:1rem;">ANSWER</p><p>${c.back}</p>`;
  flashcard.classList.remove('flipped');
  cardCounter.textContent = `${currentCard + 1} / ${flashcards.length}`;
}

flashcard.addEventListener('click', () => flashcard.classList.toggle('flipped'));
document.getElementById('card-prev').addEventListener('click', () => {
  currentCard = (currentCard - 1 + flashcards.length) % flashcards.length;
  renderCard();
});
document.getElementById('card-next').addEventListener('click', () => {
  currentCard = (currentCard + 1) % flashcards.length;
  renderCard();
});
renderCard();

// ==================== Progress Bars Animation ====================
const progressObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.querySelectorAll('.progress-fill').forEach(bar => {
        bar.style.width = bar.dataset.width;
      });
    }
  });
}, { threshold: 0.3 });
document.querySelectorAll('.progress-section').forEach(el => progressObserver.observe(el.parentElement));

// ==================== Smooth Scroll for CTA ====================
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    e.preventDefault();
    const target = document.querySelector(a.getAttribute('href'));
    if (target) target.scrollIntoView({ behavior: 'smooth' });
  });
});
