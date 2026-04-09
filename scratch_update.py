import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Navigation
nav_insert = """
    <li><a href="#planning">Planning</a></li>
    <li><a href="#troubleshooting">Diagnostics</a></li>
    <li><a href="#admin">Admin & DR</a></li>
"""
html = html.replace('<li><a href="#osi">OSI Model</a></li>', nav_insert + '    <li><a href="#osi">OSI Model</a></li>')

# 2. Add Planning & Cabling section before OSI
planning_section = """
  <!-- Planning & Cabling -->
  <section class="section" id="planning">
    <div class="section-header reveal">
      <div class="section-label">📐 Network Design</div>
      <h2 class="section-title">Planning & Cabling</h2>
      <p class="section-subtitle">Understanding the lifecycle of a network from requirements to physical wiring.</p>
    </div>
    <div class="grid-2 reveal">
      <div class="card">
        <h3>📋 The Network Design Process</h3>
        <p>A structured approach to ensure the network meets business objectives:</p>
        <ul style="padding-left:1.5rem; margin-top:0.5rem; color:var(--text-secondary); font-size:0.95rem;">
          <li><strong style="color:var(--text-primary);">1. Analyze Requirements:</strong> Gather functional (e.g., VoIP support), performance (e.g., high bandwidth), and security needs. Use traffic analysis surveys.</li>
          <li><strong style="color:var(--text-primary);">2. Planning:</strong> Finalize budget and perform risk assessments before major changes.</li>
          <li><strong style="color:var(--text-primary);">3. Logical Design:</strong> Architect IP addressing, switching, and routing protocols. Create a logical network diagram.</li>
          <li><strong style="color:var(--text-primary);">4. Physical Design:</strong> Select hardware, plan device placement (e.g., APs for wireless coverage), and define the physical topology schema.</li>
          <li><strong style="color:var(--text-primary);">5. Test & Document:</strong> Use simulation software. Create a network design proposal.</li>
          <li><strong style="color:var(--text-primary);">6. Implementation & Handoff:</strong> Install hardware. Client signs an acceptance document based on network documentation.</li>
          <li><strong style="color:var(--text-primary);">7. Continuous Improvement:</strong> Schedule periodic design reviews.</li>
        </ul>
      </div>
      <div class="card">
        <h3>🔌 Physical Implementation & Cabling</h3>
        <ul style="padding-left:1.5rem; margin-top:0.5rem; color:var(--text-secondary); font-size:0.95rem;">
          <li><strong style="color:var(--text-primary);">Twisted Pair (Copper):</strong> Uses RJ-45. <strong>Cat5e</strong> (1 Gbps), <strong>Cat6</strong> (10 Gbps, shorter distances, higher frequencies), <strong>Cat6a</strong> (10 Gbps). Susceptible to EMI unless shielded (STP).</li>
          <li><strong style="color:var(--text-primary);">Coaxial:</strong> Broadband internet. Uses F-type or BNC connectors.</li>
          <li><strong style="color:var(--text-primary);">Fiber Optic:</strong> Uses light. Immune to EMI. Consists of core, cladding (keeps light inside), buffer, and jacket. <strong>Single-mode</strong> (long distance, laser) vs <strong>Multi-mode</strong> (short distance, LED). Connectors: LC, SC, ST.</li>
        </ul>
        <h4 style="margin-top:1rem; font-size:1rem;">🏢 Wiring Systems</h4>
        <p style="color:var(--text-secondary); font-size:0.95rem;"><strong>Horizontal Wiring:</strong> Runs from telecom closet to wall plates in offices.<br><strong>Vertical (Backbone):</strong> Runs between floors to connect closets.</p>
      </div>
    </div>
  </section>
"""
html = html.replace('  <!-- OSI Model -->', planning_section + '\n  <!-- OSI Model -->')

# 3. Add Troubleshooting section before Security
troubleshooting_section = """
  <!-- Troubleshooting -->
  <section class="section tab-section" id="troubleshooting">
    <div class="section-header reveal">
      <div class="section-label">🛠️ Diagnostics</div>
      <h2 class="section-title">Troubleshooting & Issues</h2>
      <p class="section-subtitle">A systematic approach to identifying and fixing network faults.</p>
    </div>
    
    <div class="tab-nav reveal">
      <button class="tab-btn active" data-tab="tab-methodology">6-Step Methodology</button>
      <button class="tab-btn" data-tab="tab-tools">Diagnostic Tools</button>
      <button class="tab-btn" data-tab="tab-issues">Common Issues</button>
    </div>

    <div id="tab-methodology" class="tab-panel active reveal">
      <div class="grid-3">
        <div class="card">
          <div class="card-icon" style="background:rgba(59,130,246,0.15);color:var(--accent-blue);">1</div>
          <h3>Identify the Problem</h3>
          <p>Gather information, question users, and attempt to duplicate the issue.</p>
        </div>
        <div class="card">
          <div class="card-icon" style="background:rgba(16,185,129,0.15);color:var(--accent-emerald);">2</div>
          <h3>Establish a Theory</h3>
          <p>Start with the obvious (e.g., check physical connections, power) and establish a theory of probable cause.</p>
        </div>
        <div class="card">
          <div class="card-icon" style="background:rgba(139,92,246,0.15);color:var(--accent-purple);">3</div>
          <h3>Test the Theory</h3>
          <p>Test your theory to determine the exact cause of the problem.</p>
        </div>
        <div class="card">
          <div class="card-icon" style="background:rgba(245,158,11,0.15);color:var(--accent-amber);">4</div>
          <h3>Plan of Action</h3>
          <p>Establish a plan of action to resolve the problem and implement the solution safely.</p>
        </div>
        <div class="card">
          <div class="card-icon" style="background:rgba(6,182,212,0.15);color:var(--accent-cyan);">5</div>
          <h3>Verify Functionality</h3>
          <p>Verify full system functionality and implement preventive measures.</p>
        </div>
        <div class="card">
          <div class="card-icon" style="background:rgba(244,63,94,0.15);color:var(--accent-rose);">6</div>
          <h3>Document</h3>
          <p>Document your findings, actions taken, and final outcomes for future reference.</p>
        </div>
      </div>
    </div>
    
    <div id="tab-tools" class="tab-panel reveal">
      <div class="grid-2">
        <div class="card">
          <h3>💻 Command Line Utilities</h3>
          <ul style="padding-left:1.5rem; margin-top:0.5rem; color:var(--text-secondary); font-size:0.95rem;">
            <li><code>ping</code>: Tests connectivity using ICMP echo requests.</li>
            <li><code>tracert / traceroute</code>: Maps the routing path a packet takes.</li>
            <li><code>ipconfig / ifconfig</code>: Displays TCP/IP config values.</li>
            <li><code>ipconfig /displaydns</code>: Shows locally cached DNS entries.</li>
            <li><code>nslookup</code>: Queries DNS to resolve hostnames to IPs.</li>
            <li><code>netstat</code>: Displays active network connections/ports.</li>
            <li><code>ROMMON</code>: Low-level OS for password recovery on Cisco routers.</li>
          </ul>
        </div>
        <div class="card">
          <h3>🔧 Hardware Tools</h3>
          <ul style="padding-left:1.5rem; margin-top:0.5rem; color:var(--text-secondary); font-size:0.95rem;">
            <li><strong>Cable Tester:</strong> Verifies that a network cable is wired correctly and functioning physically.</li>
            <li><strong>Protocol Analyzer:</strong> Used to analyze packet loss, latency, and deep inspect traffic.</li>
            <li><strong>Loopback Plug:</strong> Tests Network Interface Cards (NICs) to ensure they can send and receive properly.</li>
          </ul>
        </div>
      </div>
    </div>

    <div id="tab-issues" class="tab-panel reveal">
      <div class="grid-3">
        <div class="card" style="border-left:3px solid var(--accent-rose);">
          <h3>APIPA Address</h3>
          <p>If a device shows an IP of <code>169.254.x.x</code>, it means it cannot reach the DHCP server to get a valid lease.</p>
        </div>
        <div class="card" style="border-left:3px solid var(--accent-amber);">
          <h3>DNS Failure</h3>
          <p>If you can ping a site by IP but not by its domain name, the DNS server is down or misconfigured.</p>
        </div>
        <div class="card" style="border-left:3px solid var(--accent-blue);">
          <h3>Permissions Issue</h3>
          <p>If a user can log into the network but cannot open a specific file, it's likely an ACL or sharing permission issue.</p>
        </div>
      </div>
    </div>
  </section>
"""
html = html.replace('  <!-- Security -->', troubleshooting_section + '\n  <!-- Security -->')

# 4. Add Admin section before Test Prep
admin_section = """
  <!-- Admin & Recovery -->
  <section class="section" id="admin">
    <div class="section-header reveal">
      <div class="section-label">⚙️ Management</div>
      <h2 class="section-title">Admin & Disaster Recovery</h2>
      <p class="section-subtitle">Keeping the network optimized, documented, and resilient against failures.</p>
    </div>
    <div class="accordion reveal">
      <div class="accordion-item open">
        <button class="accordion-header">📁 Asset & Resource Management <span class="icon">▼</span></button>
        <div class="accordion-body">
          <p><strong>Management Practices:</strong></p>
          <ul>
            <li><strong>Asset Management:</strong> Tracking physical hardware you own and its location.</li>
            <li><strong>Configuration Management:</strong> Recording OS versions and specific configs on switches/routers.</li>
            <li><strong>Change Management:</strong> Documenting upgrades and changes for compliance.</li>
            <li><strong>File Organization:</strong> Apply principle of least privilege. Manage disk quotas, NTFS permissions, and use file compression to save space.</li>
            <li><strong>FQDN (Fully Qualified Domain Name):</strong> The complete domain name (e.g., <code>server1.example.com</code>).</li>
          </ul>
        </div>
      </div>
      <div class="accordion-item">
        <button class="accordion-header">⚡ Optimization, VLANs & Tuning <span class="icon">▼</span></button>
        <div class="accordion-body">
          <ul>
            <li><strong>VLANs (802.1Q):</strong> Logically segment devices on the same broadcast domain regardless of physical switch location. Provides security and reduces broadcast traffic.</li>
            <li><strong>QoS (Quality of Service):</strong> Prioritizes critical traffic (like VoIP) over less critical data.</li>
            <li><strong>Load Balancing:</strong> Distributes traffic across multiple servers preventing single points of failure.</li>
            <li><strong>Baselining & Monitoring:</strong> Establishing normal activity baselines to identify anomalies (e.g., alert when CPU hits 85%).</li>
            <li><strong>Maintenance Types:</strong> Preventive (firmware upgrades), Corrective (replacing a failed switch), Predictive (identifying issues before they fail).</li>
          </ul>
        </div>
      </div>
      <div class="accordion-item">
        <button class="accordion-header">💾 Backup Strategies & Redundancy <span class="icon">▼</span></button>
        <div class="accordion-body">
          <p>The <strong>Archive Bit</strong> tells backup software if a file has changed.</p>
          <ul>
            <li><strong>Full Backup:</strong> Backs up everything, resets archive bit. (Slowest to run, fastest to restore).</li>
            <li><strong>Incremental:</strong> Backs up data changed since last backup, resets archive bit. (Fastest to run, slowest restore).</li>
            <li><strong>Differential:</strong> Backs up data changed since last full backup, DOES NOT reset archive bit.</li>
            <li><strong>Storage Tech:</strong> NAS (Network Attached Storage - file level) vs SAN (Storage Area Network - fast block level).</li>
            <li><strong>RAID:</strong> RAID 0 (Striping), RAID 1 (Mirroring), RAID 3 (Byte-level parity delay), RAID 5 (Distributed parity, tolerates 1 drive failure).</li>
            <li><strong>Redundancy Testing:</strong> Intentionally disconnecting primary lines to verify failover to backup systems.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
"""
html = html.replace('  <!-- Test Prep - Breakdown -->', admin_section + '\n  <!-- Test Prep - Breakdown -->')

# 5. Overwrite devices adding Server roles & NICs
devices_injection = """
      <div class="card">
        <h3>🖥️ Server Roles</h3>
        <p><strong>Domain/Directory:</strong> Manages authentication (Active Directory/Kerberos). <strong>File/Print:</strong> Central storage/spooling. <strong>Application:</strong> Business logic. <strong>Mail:</strong> SMTP/IMAP via Exchange/Postfix.</p>
      </div>
      <div class="card">
        <h3>💳 Network Interface Card (NIC)</h3>
        <p><strong>Layer 1/2</strong> — Physical hardware connecting units to the network. Every NIC has a unique, hardcoded MAC address burned into it by the manufacturer.</p>
      </div>
"""
html = html.replace('      <div class="card">\n        <h3>📊 Network Monitor / SNMP</h3>', devices_injection + '      <div class="card">\n        <h3>📊 Network Monitor / SNMP</h3>')

# 6. Add NAT and DHCP DORA to Protocols Tab Panel Services
services_update = """
            <tr><td><strong>DHCP (DORA)</strong></td><td><code>UDP 67/68</code></td><td><strong>Discover, Offer, Request, Acknowledge.</strong> Client broadcasts request, Server offers, Client broadcasts acceptance, Server ACKs.</td></tr>
            <tr><td><strong>NAT</strong></td><td>Layer 3</td><td>Translates private IPs to public. <strong>Inside Local</strong> (private IP) to <strong>Inside Global</strong> (public IP seen by outside world).</td></tr>
"""
html = html.replace('<tr><td><strong>DHCP</strong></td><td><code>UDP 67/68</code></td><td>Automatically assigns IP addresses, subnet masks, gateways, and DNS servers. DORA process.</td></tr>', '')
html = html.replace('<tr><td><strong>NAT</strong></td><td>Layer 3</td><td>Translates private IPs to public IPs. Conserves IPv4 addresses. Types: Static, Dynamic, PAT.</td></tr>', services_update)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html")

# Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

quiz_insert = """
  { q: "You can ping a server by its IP address, but not by its domain name. What is likely failing?", opts: ["The DHCP server", "The DNS server", "The default gateway", "The subnet mask"], ans: 1 },
  { q: "Which backup type backs up everything changed since the last full backup and does NOT reset the archive bit?", opts: ["Full Backup", "Incremental Backup", "Differential Backup", "Copy Backup"], ans: 2 },
  { q: "What is the 3rd step in the standard troubleshooting methodology?", opts: ["Identify the problem", "Establish a theory of probable cause", "Test the theory to determine the cause", "Establish a plan of action"], ans: 2 },
  { q: "A workstation has an IP address of 169.254.10.5. What does this indicate?", opts: ["It is on a Class C network", "It has successfully reached the router", "It cannot reach the DHCP server (APIPA)", "It is connected via VPN"], ans: 2 },
  { q: "In the DHCP DORA process, why is the 'Request' packet broadcasted?", opts: ["To find the MAC address", "So all other DHCP servers know the offer was accepted", "To bypass the firewall", "Because it does not know the server's IP"], ans: 1 },
"""
js = js.replace('  { q: "Which security model never implicitly trusts any user or device?", opts: ["Perimeter Security", "Zero Trust", "Defense in Depth", "Network Segmentation"], ans: 1 },', '  { q: "Which security model never implicitly trusts any user or device?", opts: ["Perimeter Security", "Zero Trust", "Defense in Depth", "Network Segmentation"], ans: 1 },' + quiz_insert)

js = js.replace('quizScore >= 10', 'quizScore >= 15')
js = js.replace('quizScore >= 7', 'quizScore >= 10')

flash_insert = """
  { front: "What is a PDU at Layer 4 (Transport)?", back: "Segment. It includes port numbers (e.g., 80, 443). At Layer 3 it is a Packet (IPs), and at Layer 2 it is a Frame (MACs)." },
  { front: "What is the difference between MAC and DAC?", back: "MAC (Mandatory Access Control) is strictest, OS restricts access based on labels/clearances. DAC (Discretionary Access Control) lets the data owner decide who has access." },
  { front: "What is the Archive Bit?", back: "A file attribute used by backup software. It indicates if a file has been modified since it was last backed up. Full and Incremental backups reset it; Differential does not." },
  { front: "What is a DMZ?", back: "Demilitarized Zone. A subnetwork exposing public-facing services (Web, Email) to the internet while keeping the internal LAN secure behind another firewall." },
  { front: "IPv4 Private Ranges", back: "Class A: 10.0.0.0 - 10.255.255.255 | Class B: 172.16.0.0 - 172.31.255.255 | Class C: 192.168.0.0 - 192.168.255.255. These are non-routable on the internet." },
"""
js = js.replace('  { front: "What is Network Segmentation?", back: "Dividing a network into isolated zones to contain threats, improve performance, and enforce access control. Achieved through VLANs, subnets, and firewalls." },', '  { front: "What is Network Segmentation?", back: "Dividing a network into isolated zones to contain threats, improve performance, and enforce access control. Achieved through VLANs, subnets, and firewalls." },' + flash_insert)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js")
