import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Network Architectures details to Planning (Client-Server vs P2P)
architectures_content = """
      <div class="card" style="grid-column: span 2;">
        <h3>🔗 Network Architectures & Topologies</h3>
        <div class="grid-2" style="margin-top:1rem;">
          <div>
            <p><strong>Client-Server (Domain Controlled):</strong> Dedicated servers provide resources to clients. Essential for enterprises. Offers centralized security, backups, and high scalability.</p>
            <p style="margin-top:0.5rem;"><strong>Peer-to-Peer (P2P):</strong> All computers have equal status. Best for small environments (<10 users). Cheap but lacks centralized management.</p>
            <p style="margin-top:0.5rem; color:var(--text-secondary); font-size:0.9rem;"><em>Note: Legacy P2P like Gnutella was an older decentralized protocol used to search for shared resources.</em></p>
          </div>
          <div>
            <p><strong>Topologies Refresher:</strong></p>
            <ul style="padding-left:1.5rem; color:var(--text-secondary); font-size:0.95rem;">
              <li><strong>Star:</strong> Simplest, most cost-effective. Ideal for small firms sharing files/internet.</li>
              <li><strong>Mesh:</strong> Most redundancy, minimal downtime (ideal for retail/critical).</li>
              <li><strong>Scalability:</strong> A core principle regardless of topology to ensure easy expansion.</li>
            </ul>
          </div>
        </div>
      </div>
"""
# Insert at the end of the planning grid
html = html.replace('      </div>\n    </div>\n  </section>', '      </div>\n' + architectures_content + '    </div>\n  </section>', 1)


# 2. Add Implementation Testing and IP Addressing to Admin/Optimization
tuning_content = """
      <div class="accordion-item">
        <button class="accordion-header">🌐 IP Addressing, Segmenting & Testing <span class="icon">▼</span></button>
        <div class="accordion-body">
          <p><strong>IPv4 Private Address Ranges (RFC 1918):</strong> Non-routable internal IPs.</p>
          <ul>
            <li><strong>Class A:</strong> 10.0.0.0 to 10.255.255.255</li>
            <li><strong>Class B:</strong> 172.16.0.0 to 172.31.255.255</li>
            <li><strong>Class C:</strong> 192.168.0.0 to 192.168.255.255</li>
          </ul>
          <p style="margin-top:1rem;"><strong>Segmenting & Testing:</strong></p>
          <ul>
            <li><strong>Segmenting:</strong> Breaking a large network into smaller subnets to reduce broadcast traffic and increase speed. Routers (and sometimes Layer 3 switches) are used to route between these segments.</li>
            <li><strong>Logical Segmentation:</strong> Using VLANs to separate departments (e.g., HR and Accounting) on different broadcast domains.</li>
            <li><strong>Load Testing:</strong> Testing post-implementation to ensure the network handles live traffic loads.</li>
            <li><strong>Coverage Testing:</strong> Having users connect from various physical locations to map wireless signal strength.</li>
          </ul>
        </div>
      </div>
"""
# Insert after the Optimization item
html = html.replace('</button>\n        <div class="accordion-body">\n          <ul>\n            <li><strong>VLANs', '</button>\n        <div class="accordion-body">\n          <ul>\n            <li><strong>VLANs') # Just checking exists
if '<button class="accordion-header">⚡ Optimization, VLANs & Tuning' in html:
    # Find the end of this accordion item and insert the new one
    parts = html.split('<button class="accordion-header">💾 Backup Strategies & Redundancy')
    html = parts[0] + tuning_content + '\n      <div class="accordion-item">\n        <button class="accordion-header">💾 Backup Strategies & Redundancy' + parts[1]


# 3. Add Security details: Permissive/Restrictive, MAC/DAC, VPNs, SSL/TLS, Intranet/Extranet
security_updates = """
      <div class="accordion-item">
        <button class="accordion-header">🚧 Advanced Security & Access Control <span class="icon">▼</span></button>
        <div class="accordion-body">
          <ul>
            <li><strong>Firewall Policies:</strong> <em>Permissive</em> permits all except explicitly denied. <em>Restrictive</em> denies all except explicitly allowed (Best Practice).</li>
            <li><strong>DMZ:</strong> Subnetwork exposing external-facing services (Web/FTP) while keeping internal LAN secure behind a second firewall.</li>
            <li><strong>Intranet vs Extranet:</strong> Intranet is private for employees. Extranet securely shares part of operations with suppliers/partners.</li>
            <li><strong>Access Controls:</strong> <em>MAC (Mandatory Access Control)</em> is strictest; OS restricts by labels/clearances. <em>DAC (Discretionary)</em> lets data owners define access.</li>
            <li><strong>Remote Access:</strong> Always use secure protocols like SSH (port 22) instead of Telnet (port 23).</li>
            <li><strong>SSL/TLS:</strong> Encrypts data between web server and browser using Public Key Infrastructure (PKI) and certificates.</li>
            <li><strong>VPN Tunnels:</strong> Encrypted tunnels over public networks using protocols like PPTP or L2TP to provide secure remote access.</li>
            <li><strong>Dark Fiber:</strong> Fiber optic cable that has been laid but is not currently in use (unlit).</li>
          </ul>
        </div>
      </div>
"""
parts = html.split('<div class="accordion-item">\n        <button class="accordion-header">🏗️ Zero Trust Architecture')
if len(parts) == 2:
    html = parts[0] + security_updates + '<div class="accordion-item">\n        <button class="accordion-header">🏗️ Zero Trust Architecture' + parts[1]

# 4. Modify Disaster Recovery to mention Business Continuity separately
html = html.replace('<li><strong>3-2-1 Rule:</strong>', '<li><strong>Disaster Recovery vs Business Continuity:</strong> DR is technical steps to restore IT. BC is the broader plan to keep the business operational.</li>\n            <li><strong>3-2-1 Rule:</strong>')

# Also add Network Security Wheel to existing Security area
wheel_content = """
      <div class="accordion-item">
        <button class="accordion-header">🔄 Network Security Wheel <span class="icon">▼</span></button>
        <div class="accordion-body">
          <p>A continuous lifecycle model for security policy compliance. Phases:</p>
          <ul>
            <li><strong>Secure:</strong> Implement policies, firewalls, and patching.</li>
            <li><strong>Monitor:</strong> Watch for anomalous traffic and logs.</li>
            <li><strong>Test:</strong> Perform vulnerability scans and penetration testing.</li>
            <li><strong>Improve:</strong> Review results and refine the security posture.</li>
          </ul>
          <p style="margin-top:0.5rem; color:var(--text-secondary); font-size:0.9rem;"><em>Regular patching of network operating systems helps protect against newly discovered vulnerabilities.</em></p>
        </div>
      </div>
"""
parts = html.split('<div class="accordion-item">\n        <button class="accordion-header">🎯 Threat Mitigation')
if len(parts) == 2:
    html = parts[0] + wheel_content + '<div class="accordion-item">\n        <button class="accordion-header">🎯 Threat Mitigation' + parts[1]


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated HTML with complete study guide details.")
